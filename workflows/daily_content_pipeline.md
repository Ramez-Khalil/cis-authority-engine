# Daily Content Pipeline — CIS Authority Engine

## Pipeline Overview
This document defines the complete daily workflow for the CIS Authority Engine. It covers how cybersecurity and business technology news enters the system, how it is analyzed, how content is generated, and how it moves from draft to published to analyzed.

---

## Daily Workflow: Step-by-Step

### PHASE 1: NEWS COLLECTION (Morning — 7:00-7:30 AM)

#### Sources to Monitor Daily
Check the following sources for relevant cybersecurity and business technology news:

Government and Official Sources:
- CISA (Cybersecurity and Infrastructure Security Agency) — cisa.gov/news-events
- NIST National Cybersecurity Center of Excellence — nccoe.nist.gov
- FBI Cyber Division press releases — ic3.gov

Established Security Research:
- Krebs on Security — krebsonsecurity.com
- Dark Reading — darkreading.com
- SC Media — scmagazine.com

Business Technology News:
- CIO Magazine — cio.com
- InformationWeek — informationweek.com
- TechTarget Security news — searchsecurity.techtarget.com

Academic and Framework Sources:
- SANS Internet Storm Center — isc.sans.edu
- MITRE ATT&CK updates — attack.mitre.org

#### What to Look For
Prioritize news items that:
- Affect organizations across multiple industries (not just one sector)
- Connect clearly to a CIS role or competency
- Have organizational risk as the consequence (not just technical impact)
- Are publicly verified by at least one credible source
- Have not been used in the last 30 days (avoid repetitive topic coverage)

#### What to Skip
Do not collect news items that:
- Involve unverified claims or allegations
- Focus on technical exploitation details without organizational context
- Name specific victim organizations without their own public disclosure
- Are driven by vendor marketing rather than independent reporting
- Are more than 7 days old (unless the topic remains highly relevant)

#### Collection Action
Save raw news items to: /news/raw/YYYY-MM-DD-source-slug.md
Format: Include headline, source, publication date, one-paragraph summary, and source URL.

---

### PHASE 2: NEWS ANALYSIS (Morning — 7:30-8:00 AM)

#### Run News Analysis Prompt
For each collected news item, run the prompts/news_analysis.md prompt through your AI assistant.

Input: Raw news item from /news/raw/
Output: Structured analysis including factual assessment, organizational relevance scores, content opportunity, extracted facts, content recommendation, and ethical flags.

#### Filtering Decision
After analysis, decide:
- HIGH PRIORITY: Post today or within 24 hours (score 7+ overall relevance, time-sensitive)
- MEDIUM PRIORITY: Use within 48 hours (score 5-6 relevance, evergreen topic)
- LOW PRIORITY: File for future use (score below 5 or limited audience relevance)
- NOT SUITABLE: Do not use (fails factual assessment or has ethical flags)

#### Storage Action
Save analyzed news to: /news/processed/YYYY-MM-DD-topic-slug.md
Update /skills/cis-growth-engine/facts_bank.md with any new VERIFIED facts extracted.

---

### PHASE 3: POST GENERATION (Morning — 8:00-8:30 AM)

#### Select Today's Topic
Review /news/processed/ for HIGH PRIORITY items. If no new high-priority news, select a MEDIUM PRIORITY item or generate an evergreen post using facts_bank.md.

Weekly topic rotation (suggested):
- Monday: Risk awareness or organizational readiness topic
- Tuesday: CIS career value or role highlight
- Wednesday: Incident lesson or industry pattern
- Thursday: Uncomfortable question or myth vs. reality
- Friday: Strategic insight or forward-looking organizational perspective

#### Run Daily Post Generation Prompt
Use prompts/daily_post_generation.md with today's selected news item or topic.

Input: Processed news item from /news/processed/
Output: Post analysis, LinkedIn post text, Canva instructions, engagement prediction

#### Storage Action
Save generated draft to: /posts/drafts/YYYY-MM-DD-topic-slug.md
File should include all output sections from the generation prompt.

---

### PHASE 4: REVIEW AND REFINEMENT (Morning — 8:30-9:00 AM)

#### Self-Review Checklist
Before approving a post for publishing, confirm:

CONTENT QUALITY:
[ ] First line creates immediate intellectual tension
[ ] No fabricated statistics — all claims are clearly framed
[ ] No named organizations accused without public verification
[ ] Controversy level is appropriate for the topic
[ ] CIS role or competency is clearly connected
[ ] Brand voice is consistent (professional, sharp, slightly provocative)

FORMATTING:
[ ] Maximum 12 words per line for mobile readability
[ ] Visual line breaks every 2-3 lines
[ ] Closing CTA invites specific engagement (not "like and share")
[ ] 3-5 relevant hashtags at the end
[ ] Length is 150-300 words

ETHICAL:
[ ] All claims are verifiable or clearly framed as reported
[ ] No fearmongering or exaggeration
[ ] No arrogance or overconfidence about CIS capabilities
[ ] Controversy level matches controversy_rules.md guidelines

CANVA INSTRUCTIONS:
[ ] Template type selected
[ ] All four zones specified
[ ] Color palette matches canva_design_rules.md
[ ] Icon specifications included
[ ] Quality checklist included in instructions

---

### PHASE 5: CANVA PRODUCTION (Before Posting — 30 minutes)

Using the Canva instructions from the draft file:
1. Open Canva and start with a blank 1080x1080 canvas
2. Set background to #0A1628 (Dark Navy)
3. Build each zone following the instructions exactly
4. Complete the quality checklist before downloading
5. Download as PNG at highest available resolution

---

### PHASE 6: LINKEDIN PUBLISHING (Manual — 9:00-10:00 AM optimal window)

Optimal posting times by audience target:
- Executive-focused posts: 7:00-9:00 AM Tuesday through Thursday
- Student/career posts: Monday 9:00-11:00 AM or Friday 9:00-11:00 AM
- IT professional posts: Tuesday through Thursday 10:00 AM-12:00 PM

Publishing steps:
1. Open LinkedIn
2. Create new post
3. Paste LinkedIn post text from draft file
4. Attach Canva infographic as image
5. Review formatting in LinkedIn's preview
6. Publish
7. Move draft file to /posts/posted/ and note posting date and time

---

### PHASE 7: ENGAGEMENT MONITORING (Same day, 6:00 PM check / Next day, 24-hour check)

Check LinkedIn Analytics for initial performance data.
Respond to all substantive comments within 24 hours.
Note any high-value commenters (senior titles, large followings) for relationship building.
Update /posts/posted/YYYY-MM-DD-topic-slug.md with initial 24-hour metrics.

---

### PHASE 8: 48-HOUR PERFORMANCE LOGGING

Update /analytics/engagement_tracking.md with 48-hour performance data.
If post enters top 20% of engagement for the week, copy to /posts/top_performing/.
Update top_performing_patterns.md with any newly confirmed patterns.

---

## Weekly Pipeline Review (Friday)

Review the week's content performance.
Update engagement_tracking.md weekly summary.
Identify the week's top and lowest performing posts.
Note any patterns that should inform the following week's content strategy.
Check facts_bank.md for currency — add any new verified facts from the week's news.
Plan next week's topic rotation based on performance data.

---

## Monthly Pipeline Maintenance (First Monday of each month)

Complete monthly summary in engagement_tracking.md.
Update top_performing_patterns.md with monthly analysis.
Review and update SKILL.md if mission or audience priorities have shifted.
Update brand_voice.md if tone refinements are needed based on performance data.
Update top_hooks.md with new patterns discovered from high-performing posts.
Archive previous month's news raw files to reduce repository size.
Review facts_bank.md for outdated information and mark accordingly.

---

## Scaling Plan

### Phase 1 — Manual Operation (Months 1-3)
All steps above executed manually. Goal: establish content quality baseline and initial engagement data.

### Phase 2 — Partial Automation (Months 4-6)
Automate news collection using GitHub Actions workflow (.github/workflows/daily-news.yml).
Scripts in /scripts/ folder handle news fetching and initial filtering.
Human review still required for all content generation and publishing decisions.

### Phase 3 — AI-Assisted Generation (Months 7+)
After 6 months of engagement data, refine prompts based on confirmed top_performing_patterns.
Consider batch generation (generate 5 posts per week in one session, then review and schedule).
Maintain manual review and publishing step to preserve content quality control.
