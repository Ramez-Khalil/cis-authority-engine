# CIS Authority Engine

> An AI-powered content system that positions Computer Information Systems (CIS) as the strategic backbone of modern enterprise operations — through daily LinkedIn posts, Canva infographics, and a professional fact-verified knowledge base.

---

## Mission

The CIS Authority Engine transforms cybersecurity and business technology news into high-engagement LinkedIn content that positions CIS professionals as essential organizational risk managers — not just technologists.

**CIS is positioned as:** Organizational risk management, cybersecurity awareness and operations, enterprise systems management, business technology leadership, IT infrastructure operations, and data-driven decision support.

**Content targets:** CIS students and recent graduates, recruiters and hiring managers, business executives and IT leaders, and working IT professionals.

**Tone:** Professional. Sharp. Executive-level. Slightly provocative. Always credible.

---

## Repository Structure

```
cis-authority-engine/
|
+-- skills/cis-growth-engine/        # Core identity and strategy system
|   +-- SKILL.md                     # System definition and mission
|   +-- brand_voice.md               # Voice, tone, and language rules
|   +-- post_frameworks.md           # 6 LinkedIn post frameworks
|   +-- controversy_rules.md         # Controversy guidelines (3 levels)
|   +-- cis_roles.md                 # CIS career roles and organizational value
|   +-- linkedin_strategy.md         # Deep LinkedIn engagement strategy
|   +-- canva_design_rules.md        # Visual design system (dark navy/cyan)
|   +-- facts_bank.md                # Verified fact database by domain
|   +-- top_hooks.md                 # Hook pattern library (7 categories)
|
+-- prompts/                         # Reusable AI prompt system
|   +-- daily_post_generation.md     # Master prompt for daily post creation
|   +-- news_analysis.md             # News verification and analysis prompt
|   +-- canva_generation.md          # Canva infographic instruction prompt
|
+-- news/
|   +-- raw/                         # Unprocessed news headlines (auto-collected)
|   +-- processed/                   # Analyzed and verified news (ready for use)
|
+-- posts/
|   +-- drafts/                      # Generated posts pending review
|   +-- posted/                      # Published posts with engagement data
|   +-- top_performing/              # Top 20% posts for pattern analysis
|
+-- analytics/
|   +-- engagement_tracking.md       # Weekly/monthly engagement data
|   +-- top_performing_patterns.md   # Pattern analysis and strategy evolution
|
+-- workflows/
|   +-- daily_content_pipeline.md    # Complete 8-phase daily workflow
|
+-- .github/workflows/
|   +-- daily-news.yml               # GitHub Actions news collection automation
|
+-- scripts/
|   +-- collect_news.py              # News collection script (requires API key)
|   +-- generate_daily_post.py       # Draft file structure creator
|
+-- README.md                        # This file
```

---

## Daily Workflow Overview

```
Morning News (CISA, Dark Reading, Reuters, CIO)
        |
  collect_news.py (automated) --> /news/raw/
        |
  news_analysis.md prompt (manual AI analysis) --> /news/processed/
        |
  daily_post_generation.md prompt (manual AI generation)
        |
  Output: LinkedIn post + Canva instructions
        |
  Human review (checklist in draft file)
        |
  Canva production (manual, 30 min)
        |
  LinkedIn publish (manual, 7-9 AM optimal)
        |
  Engagement tracking (analytics/engagement_tracking.md)
```

See `workflows/daily_content_pipeline.md` for the full 8-phase process.

---

## Quick Start

**Step 1: Generate a Draft File**

```bash
python scripts/generate_daily_post.py your-topic-slug
```

**Step 2: Collect News (Requires API Key)**

```bash
export NEWS_API_KEY=your_key_here
python scripts/collect_news.py
```

**Step 3: Analyze News (Manual)**
Open `prompts/news_analysis.md` and run through your AI assistant. Save to `/news/processed/`.

**Step 4: Generate Post (Manual)**
Open `prompts/daily_post_generation.md` and run with the processed news item. Paste output into your draft file.

**Step 5: Review and Publish**
Complete the review checklist. Build Canva infographic. Publish manually to LinkedIn.

---

## CIS Career Roles Covered

| Role | Primary Organizational Function |
|------|----------------------------------|
| Systems Analyst | Bridge between business needs and technology solutions |
| IT Project Manager | Technology investment delivery and risk management |
| Database Administrator | Data infrastructure and integrity stewardship |
| Cybersecurity Analyst | Threat detection, incident response, risk reduction |
| Network Administrator | Infrastructure reliability and network security |
| Business Intelligence Analyst | Data-to-decision transformation |

---

## Canva Design System

| Element | Value |
|---------|-------|
| Background | Dark Navy #0A1628 |
| Primary Accent | Cyan #00D4FF |
| Container | Steel Blue #1E3A5F |
| Body Text | Light Gray #A8B8CC |
| Font | Inter or Montserrat |
| Canvas Size | 1080 x 1080 px |

---

## Ethical Commitments

This system will **never:** attribute specific attacks to named organizations without verified public reporting, claim CIS professionals can prevent all cyberattacks, use fabricated or extrapolated statistics, or create fear without organizational context.

This system will **always:** distinguish between verified facts and reported facts, connect technology to measurable business consequences, and maintain consistent professional credibility over viral reach.

---

## Automation Status

| Component | Status |
|-----------|--------|
| News collection | Automated (requires NEWS_API_KEY secret) |
| News analysis | Manual (AI-assisted via prompt) |
| Post generation | Manual (AI-assisted via prompt) |
| Canva production | Manual (instruction-guided) |
| LinkedIn publishing | Manual (human decision required) |
| Engagement tracking | Manual (LinkedIn Analytics data entry) |

Automated LinkedIn publishing is **intentionally excluded**. Content quality and professional credibility require human editorial judgment at every generation and publishing step.

---

## Maintenance Schedule

| Frequency | Task |
|-----------|------|
| Daily | News collection and post generation |
| Weekly | Engagement tracking update, pattern review |
| Monthly | Facts bank update, top performing patterns analysis |
| Quarterly | Skill definition review, strategy refinement |
