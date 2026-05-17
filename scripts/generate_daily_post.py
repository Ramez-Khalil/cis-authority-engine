#!/usr/bin/env python3
"""
CIS Authority Engine — Daily Post Generation Helper
====================================================
This script creates the daily post draft file structure in /posts/drafts/
to be filled in manually after running the AI generation prompts.

USAGE:
- Run this script to create today's draft file with the correct structure
- Then open the file and paste in your AI-generated content
- python scripts/generate_daily_post.py [optional-topic-slug]

EXAMPLE:
- python scripts/generate_daily_post.py vendor-risk-management
- Creates: posts/drafts/2026-05-16-vendor-risk-management.md

This script does NOT generate content automatically.
Content generation requires running the prompts in /prompts/ through Claude or another AI.

DESIGN DECISION:
Automated AI content generation for LinkedIn posts is intentionally not included.
Content quality, fact verification, and editorial judgment require human review at every step.
This script only handles file structure management to make the manual workflow more efficient.
"""

import sys
import os
from datetime import datetime, timezone
from pathlib import Path


# ============================================================
# CONFIGURATION
# ============================================================

DRAFTS_DIR = Path("posts/drafts")
TODAY = datetime.now(timezone.utc).strftime("%Y-%m-%d")


# ============================================================
# DRAFT FILE TEMPLATE
# ============================================================

DRAFT_TEMPLATE = """# Daily Post Draft — {date}
# Topic: {topic_slug}
# Status: DRAFT — Pending review before publishing

---

## POST ANALYSIS
<!-- Fill this in from the daily_post_generation.md prompt output -->

- Topic category: 
- Framework selected: 
- Hook category: 
- Primary audience: 
- Controversy level: 
- CIS role connection: 

---

## LINKEDIN POST
<!-- Paste the generated LinkedIn post text here -->
<!-- Remember: 150-300 words, mobile-first formatting, max 12 words per line -->

[PASTE LINKEDIN POST TEXT HERE]

---

## CANVA INSTRUCTIONS
<!-- Paste the Canva infographic instructions here from the generation prompt -->

### Infographic Brief
- Template type: 
- Core message (8 words max): 
- Primary audience visual cue: 
- Tone: 

### Canvas Setup
- Canvas size: 1080 x 1080 pixels
- Background color: #0A1628 (Dark Navy)
- Margin: 60px all sides

### Zone 1 — Hook Zone (Top 20%)
[PASTE ZONE 1 INSTRUCTIONS HERE]

### Zone 2 — Context Zone (Middle 50%)
[PASTE ZONE 2 INSTRUCTIONS HERE]

### Zone 3 — Impact Zone (Lower 25%)
[PASTE ZONE 3 INSTRUCTIONS HERE]

### Zone 4 — Brand Zone (Bottom 5%)
[PASTE ZONE 4 INSTRUCTIONS HERE]

### Visual Accents
[PASTE VISUAL ACCENT INSTRUCTIONS HERE]

### Icon Specifications
[PASTE ICON SPECIFICATIONS HERE]

---

## ENGAGEMENT PREDICTION
<!-- From the generation prompt output -->

- Expected comment drivers: 
- Expected share drivers: 
- Suggested optimal posting time: 

---

## REVIEW CHECKLIST
<!-- Complete before publishing -->

### Content Quality
- [ ] First line creates immediate intellectual tension
- [ ] No fabricated statistics — all claims are clearly framed
- [ ] No named organizations accused without public verification
- [ ] Controversy level is appropriate for the topic
- [ ] CIS role or competency is clearly connected
- [ ] Brand voice is consistent (professional, sharp, slightly provocative)

### Formatting
- [ ] Maximum 12 words per line for mobile readability
- [ ] Visual line breaks every 2-3 lines
- [ ] Closing CTA invites specific engagement (not "like and share")
- [ ] 3-5 relevant hashtags at the end
- [ ] Length is 150-300 words

### Ethical
- [ ] All claims are verifiable or clearly framed as reported
- [ ] No fearmongering or exaggeration
- [ ] No arrogance or overconfidence about CIS capabilities
- [ ] Controversy level matches controversy_rules.md guidelines

### Canva
- [ ] All four zones specified with exact text and styling
- [ ] Color palette matches #0A1628, #00D4FF, #1E3A5F, #FFFFFF, #A8B8CC
- [ ] Icon specifications included with search terms
- [ ] Quality checklist included in instructions

---

## POST METADATA
<!-- Fill in after publishing -->

- News source used: 
- Processed news file: /news/processed/[filename]
- Draft created: {date} {time} UTC
- Reviewed and approved: [date]
- Posted to LinkedIn: [date and time]
- LinkedIn post URL: [URL after posting]

---

## ENGAGEMENT DATA
<!-- Fill in 48 hours after posting from LinkedIn Analytics -->

### 48-Hour Metrics
- Impressions: 
- Likes: 
- Comments: 
- Reposts: 
- Profile clicks: 
- Follower additions: 
- Engagement rate: 

### Notable Comments
[Describe any high-value comments from senior professionals]

### Performance Notes
What worked well:

What could be stronger:

### Status
- [ ] Draft complete
- [ ] Review complete  
- [ ] Published to LinkedIn
- [ ] Moved to /posts/posted/
- [ ] Engagement data logged in /analytics/engagement_tracking.md
- [ ] Copied to /posts/top_performing/ (if top 20% engagement)
"""


# ============================================================
# MAIN EXECUTION
# ============================================================

def create_draft_file(topic_slug=None):
    """Create a new draft file for today's post."""
    
    # Generate filename
    if topic_slug:
        # Clean the slug
        clean_slug = topic_slug.lower().replace(" ", "-").replace("_", "-")
        filename = f"{TODAY}-{clean_slug}.md"
    else:
        filename = f"{TODAY}-post.md"
    
    filepath = DRAFTS_DIR / filename
    
    # Check if file already exists
    if filepath.exists():
        print(f"Draft file already exists: {filepath}")
        print("Add a topic slug to create a second draft for today:")
        print(f"  python scripts/generate_daily_post.py your-topic-slug")
        return filepath
    
    # Create the drafts directory if it doesn't exist
    DRAFTS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Format the template
    time_now = datetime.now(timezone.utc).strftime("%H:%M")
    content = DRAFT_TEMPLATE.format(
        date=TODAY,
        time=time_now,
        topic_slug=topic_slug or "to-be-determined",
    )
    
    # Write the file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Draft file created: {filepath}")
    print()
    print("Next steps:")
    print(f"1. Open /news/processed/ and select today's news item")
    print(f"2. Run prompts/daily_post_generation.md through your AI assistant")
    print(f"3. Paste the generated content into: {filepath}")
    print(f"4. Complete the review checklist before publishing")
    print(f"5. Build the Canva infographic following the instructions in the draft")
    print(f"6. Publish manually to LinkedIn")
    print(f"7. Update the metadata and engagement sections after posting")
    
    return filepath


def main():
    topic_slug = sys.argv[1] if len(sys.argv) > 1 else None
    
    print("CIS Authority Engine — Post Draft Creator")
    print("=" * 50)
    print(f"Creating draft for: {TODAY}")
    if topic_slug:
        print(f"Topic: {topic_slug}")
    print()
    
    filepath = create_draft_file(topic_slug)
    
    print()
    print("Reminder: Content generation is manual.")
    print("Use prompts/daily_post_generation.md with your AI assistant.")
    print("Do not publish any post without completing the review checklist.")


if __name__ == "__main__":
    main()
