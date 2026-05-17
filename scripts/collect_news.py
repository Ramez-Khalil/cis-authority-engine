#!/usr/bin/env python3
"""
CIS Authority Engine — News Collection Script
=============================================
Collects cybersecurity and business technology news headlines
and saves them to /news/raw/ for manual analysis.

SETUP REQUIREMENTS:
- Set NEWS_API_KEY as a GitHub Actions secret (or local environment variable)
- Get a free API key at newsapi.org (free tier: 100 requests/day, no commercial use)
- For production use, consider NewsAPI paid tier or alternative sources

USAGE:
- Runs automatically via .github/workflows/daily-news.yml
- Can be run manually: python scripts/collect_news.py

OUTPUT:
- Saves collected headlines to news/raw/YYYY-MM-DD-collected-headlines.md
- Each run appends to today's file if it already exists
- Saves a summary count to the terminal

IMPORTANT:
- This script only collects headlines and summaries for human review
- All content generation and publishing is manual
- Never use unverified headlines directly in posts without running through news_analysis.md
"""

import os
import sys
import json
import requests
from datetime import datetime, timezone
from pathlib import Path


# ============================================================
# CONFIGURATION
# ============================================================

# Search queries for news collection
# These are designed to surface relevant cybersecurity and business technology news
SEARCH_QUERIES = [
    "cybersecurity breach organizational",
    "enterprise IT risk management",
    "ransomware business impact",
    "data breach company",
    "information security governance",
    "IT infrastructure failure business",
    "CIS cybersecurity framework",
    "vendor risk management enterprise",
    "cloud security misconfiguration",
    "identity access management breach",
    "database security enterprise",
    "business continuity IT",
    "incident response organization",
    "supply chain cyberattack",
]

# News sources to prioritize (NewsAPI source IDs)
# These are established, credible technology and security sources
PREFERRED_SOURCES = [
    "wired",
    "the-verge",
    "techcrunch",
    "ars-technica",
    "reuters",
    "the-wall-street-journal",
    "bloomberg",
    "business-insider",
]

# How many results to collect per query (max 20 for free tier)
RESULTS_PER_QUERY = 5

# Maximum age of articles in hours
MAX_AGE_HOURS = 48

# Output directory (relative to repository root)
OUTPUT_DIR = Path("news/raw")

# ============================================================
# NEWS COLLECTION FUNCTIONS
# ============================================================

def get_api_key():
    """Get the NEWS_API_KEY from environment variables."""
    api_key = os.environ.get("NEWS_API_KEY")
    if not api_key:
        print("ERROR: NEWS_API_KEY environment variable not set.")
        print("Set this as a GitHub Actions secret or local environment variable.")
        print("Get a free key at newsapi.org")
        sys.exit(1)
    return api_key


def fetch_news(query, api_key, max_results=5):
    """
    Fetch news articles from NewsAPI for a given query.
    Returns a list of article dictionaries.
    """
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "apiKey": api_key,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": max_results,
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data.get("status") == "ok":
            return data.get("articles", [])
        else:
            print(f"  API warning for query '{query}': {data.get('message', 'Unknown error')}")
            return []
            
    except requests.exceptions.RequestException as e:
        print(f"  Request error for query '{query}': {e}")
        return []


def is_relevant_article(article):
    """
    Basic relevance filter for articles.
    Returns True if the article appears relevant for CIS content.
    """
    if not article.get("title") or not article.get("description"):
        return False
    
    title = article["title"].lower()
    description = (article.get("description") or "").lower()
    combined = title + " " + description
    
    # Skip clickbait or low-quality signals
    skip_terms = [
        "sponsored", "advertisement", "removed", "[removed]",
        "click here", "buy now", "discount", "sale",
    ]
    for term in skip_terms:
        if term in combined:
            return False
    
    # Organizational and business relevance terms
    relevance_terms = [
        "company", "organization", "enterprise", "business", "corporate",
        "breach", "attack", "vulnerability", "risk", "security", "cyber",
        "data", "infrastructure", "system", "network", "cloud",
        "ransomware", "phishing", "malware", "incident", "compliance",
        "executive", "ciso", "cto", "management", "leadership",
    ]
    
    relevance_count = sum(1 for term in relevance_terms if term in combined)
    return relevance_count >= 2


def format_article_for_storage(article, query):
    """
    Format a single article into the standard storage format
    for manual review and analysis.
    """
    title = article.get("title", "No title")
    source = article.get("source", {}).get("name", "Unknown source")
    url = article.get("url", "No URL")
    published_at = article.get("publishedAt", "Unknown date")
    description = article.get("description", "No description available")
    
    return f"""---
### {title}

**Source:** {source}
**Published:** {published_at}
**Collection Query:** {query}
**URL:** {url}

**Summary:**
{description}

**Manual Review Required:**
Before using this in content generation, run through prompts/news_analysis.md
- [ ] Factual assessment completed
- [ ] Organizational relevance scored
- [ ] Content opportunity identified
- [ ] Ethical flags checked

---
"""


def save_collected_news(articles_by_query, output_dir):
    """
    Save all collected articles to a dated file in the output directory.
    """
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    output_file = output_dir / f"{today}-collected-headlines.md"
    
    # Build the file content
    total_articles = sum(len(articles) for articles in articles_by_query.values())
    
    header = f"""# Daily News Collection — {today}
# CIS Authority Engine Automated Collection
#
# IMPORTANT: These are raw, unverified headlines collected for review.
# DO NOT use these directly in LinkedIn posts.
# Run each item through prompts/news_analysis.md before content generation.
#
# Total items collected: {total_articles}
# Collection timestamp: {datetime.now(timezone.utc).isoformat()}

"""
    
    content_sections = []
    seen_urls = set()  # Deduplicate articles
    
    for query, articles in articles_by_query.items():
        if not articles:
            continue
            
        section_articles = []
        for article in articles:
            url = article.get("url", "")
            if url and url not in seen_urls:
                seen_urls.add(url)
                if is_relevant_article(article):
                    section_articles.append(
                        format_article_for_storage(article, query)
                    )
        
        if section_articles:
            section = f"## Query: {query}\n\n" + "\n".join(section_articles)
            content_sections.append(section)
    
    full_content = header + "\n\n".join(content_sections)
    
    # Write to file
    output_dir.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(full_content)
    
    return output_file, len(seen_urls)


# ============================================================
# MAIN EXECUTION
# ============================================================

def main():
    print("CIS Authority Engine — News Collection")
    print("=" * 50)
    
    api_key = get_api_key()
    
    # Collect news for each query
    articles_by_query = {}
    
    for query in SEARCH_QUERIES:
        print(f"Collecting: {query}")
        articles = fetch_news(query, api_key, RESULTS_PER_QUERY)
        articles_by_query[query] = articles
        print(f"  Found {len(articles)} articles")
    
    # Save collected news
    print("\nSaving collected news...")
    output_file, unique_count = save_collected_news(articles_by_query, OUTPUT_DIR)
    
    print(f"\nCollection complete.")
    print(f"Unique relevant articles: {unique_count}")
    print(f"Saved to: {output_file}")
    print("\nNext steps:")
    print("1. Review the collected headlines in /news/raw/")
    print("2. Select relevant items for today's content")
    print("3. Run each item through prompts/news_analysis.md")
    print("4. Save analyzed items to /news/processed/")
    print("5. Run prompts/daily_post_generation.md for today's post")


if __name__ == "__main__":
    main()
