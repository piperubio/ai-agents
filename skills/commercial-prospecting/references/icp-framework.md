# ICP Assessment Framework & Tech Maturity Scoring Model

## 1. ICP Scoring Rubric

Total: 0-100 points across six dimensions.

### 1.1 Company Size & Budget Capacity (0-20)

| Score | Criteria |
|-------|----------|
| 0-4 | <20 employees or no identifiable tech budget. Likely cannot afford consulting engagement. |
| 5-8 | 20-49 employees. May have budget for small engagements but limited scope. |
| 9-12 | 50-149 employees. Growing companies with emerging tech needs. Budget for targeted engagements. |
| 13-16 | 150-500 employees. Mid-market sweet spot. Established revenue, dedicated tech budget likely. |
| 17-20 | 500-2000 employees. Strong budget capacity, multiple engagement opportunities. Above 2000: risk of internal teams or Big4 relationships — score 10-14 unless clear signals otherwise. |

Key indicators:
- Revenue range (USD $10M-$500M is ideal)
- Tech hiring volume and salary ranges
- Publicly disclosed tech investments
- Office/infrastructure signals

### 1.2 Technology Maturity Gap (0-25)

The highest-weighted dimension. The sweet spot is companies scoring 2-3 on the tech maturity scale — enough baseline to absorb consulting value, but clear room for improvement.

| Score | Criteria |
|-------|----------|
| 0-5 | Tech maturity 5 (Optimized) across axes — minimal consulting need. Or maturity 1 with no readiness to change. |
| 6-10 | Tech maturity 4 (Managed) — limited gaps. Or maturity 1 with some readiness signals. |
| 11-15 | Mixed maturity (e.g., Software 3, Data 2, AI 1) — clear gaps in specific axes. |
| 16-20 | Tech maturity 2-3 across axes — strong consulting need with sufficient baseline capability. |
| 21-25 | Tech maturity 2-3 across axes AND active signals of desire to improve (job postings, transformation announcements, new tech leadership). |

Key indicators:
- Job postings mentioning legacy systems, migrations, or modernization
- Tech stack age and diversity
- Presence/absence of DevOps, data engineering, ML engineering roles
- Public repositories and engineering blog activity

### 1.3 Industry Alignment (0-15)

| Score | Criteria |
|-------|----------|
| 0-3 | Industry with minimal consulting demand (e.g., purely local services, micro-niche). |
| 4-6 | Industry with moderate consulting demand but low tech intensity (e.g., traditional retail, agriculture). |
| 7-9 | Industry with good consulting demand (e.g., manufacturing, energy, education). |
| 10-12 | Industry with strong consulting demand (e.g., healthcare, logistics, insurance). |
| 13-15 | Industry with highest consulting demand (e.g., financial services, fintech, e-commerce, SaaS). |

High-value industries (examples):
- Financial services / fintech — regulatory pressure, data-intensive
- Healthcare / healthtech — compliance requirements, interoperability needs
- Logistics / supply chain — operational optimization, real-time data
- Insurance — legacy modernization, claims automation
- E-commerce / retail — scalability, personalization, data analytics

### 1.4 Decision-Making Accessibility (0-15)

| Score | Criteria |
|-------|----------|
| 0-3 | No identifiable tech leadership. Complex bureaucracy or procurement process (government, large enterprise). |
| 4-6 | Tech leadership exists but multiple approval layers. Long sales cycles expected (6+ months). |
| 7-9 | CTO/VP Engineering identifiable. Standard procurement, 3-6 month sales cycle. |
| 10-12 | CTO/VP Engineering reachable through network or warm intro. 1-3 month sales cycle. |
| 13-15 | Direct access to decision maker (founder/CTO). Fast decision process. Previous relationship or warm referral available. |

Key indicators:
- Organization size and structure
- Existing network connections (1st or 2nd degree)
- Presence at industry events or conferences
- Responsiveness on LinkedIn/social

### 1.5 Growth Trajectory (0-15)

| Score | Criteria |
|-------|----------|
| 0-3 | Declining revenue, layoffs, market contraction. Cost-cutting mode. |
| 4-6 | Flat growth, stable but no expansion signals. |
| 7-9 | Moderate growth (10-20% YoY). Hiring selectively. |
| 10-12 | Strong growth (20-50% YoY). Active hiring across functions. Recent funding or expansion. |
| 13-15 | Hyper-growth (50%+ YoY). Recent significant funding round. Expanding to new markets/products. Urgent need for tech scaling. |

Key indicators:
- Funding history and recent rounds
- Employee growth rate (LinkedIn trends)
- New office openings or market expansions
- Product launches or new business lines
- Public revenue data or estimates

### 1.6 Cultural Fit for Consulting (0-10)

| Score | Criteria |
|-------|----------|
| 0-2 | Strong not-invented-here culture. History of failed consulting engagements. Purely insourcing strategy. |
| 3-4 | No evidence of external consulting usage. Uncertain openness. |
| 5-6 | Some use of external vendors/contractors. Open to outside expertise. |
| 7-8 | Active use of consulting or staff augmentation. Leadership values external perspectives. |
| 9-10 | Strong consulting culture. Previous successful engagements. Champions for external expertise in leadership. |

Key indicators:
- Past consulting engagements (visible in case studies, press releases)
- Job postings mentioning "consulting" or "vendor management"
- Leadership background (ex-consultants in C-suite)
- Vendor ecosystem signals (technology partners page)

---

## 2. Tech Maturity Assessment Guide

Score each axis (Software, Data, AI) from 1 to 5.

### 2.1 Software Maturity

| Level | Name | Indicators |
|-------|------|------------|
| 1 | Ad-hoc/None | No in-house development. Fully outsourced or off-the-shelf only. No version control. No CI/CD. |
| 2 | Emerging | Some in-house development. Basic version control (Git). Manual deployments. Monolithic architecture. Limited testing. |
| 3 | Defined | Structured development process. CI pipeline exists. Some automated testing. Beginning microservices or modular architecture. Code reviews practiced. |
| 4 | Managed | CI/CD fully automated. Comprehensive test suites. Microservices or well-modularized architecture. Monitoring and observability in place. SLAs defined. |
| 5 | Optimized | Continuous deployment. Feature flags, canary releases. Platform engineering team. Developer experience metrics tracked. Contribution to open source. |

### 2.2 Data Maturity

| Level | Name | Indicators |
|-------|------|------------|
| 1 | Ad-hoc/None | Data in spreadsheets or ad-hoc databases. No centralized data storage. Manual reporting. No data governance. |
| 2 | Emerging | Central database exists. Basic SQL reporting. Some ETL processes (manual or scripted). Awareness of data quality issues. |
| 3 | Defined | Data warehouse or data lake in place. Scheduled ETL/ELT pipelines. BI tools deployed (Tableau, Power BI, Looker). Data ownership assigned. |
| 4 | Managed | Modern data stack. Data quality monitoring. Self-service analytics. Data catalog. Data governance policies enforced. Dedicated data engineering team. |
| 5 | Optimized | Real-time data pipelines. Data mesh or federated architecture. Data products mindset. Advanced data governance with lineage tracking. Data-driven decision culture at all levels. |

### 2.3 AI/ML Maturity

| Level | Name | Indicators |
|-------|------|------------|
| 1 | Ad-hoc/None | No AI/ML usage. No awareness or strategy. No data science roles. |
| 2 | Emerging | Exploring AI use cases. Proof-of-concept or pilot projects. 1-2 data scientists or analysts experimenting. Using pre-built AI APIs (e.g., cloud vision, NLP). |
| 3 | Defined | ML models in production for specific use cases. Small data science team. MLOps basics (model versioning, basic monitoring). AI roadmap exists. |
| 4 | Managed | Multiple ML models in production. Dedicated MLOps infrastructure. A/B testing for models. Feature stores. Model performance monitoring. AI governance policies. |
| 5 | Optimized | AI embedded across business processes. Advanced MLOps (automated retraining, drift detection). Research capability. AI center of excellence. Contributing to AI community. |

---

## 3. Prospect Tiering Guide

| Tier | ICP Score | Action | Engagement Model |
|------|-----------|--------|------------------|
| Tier 1 | 80-100 | High-touch: immediate personalized outreach | Dedicated account lead. Custom proposal within 1 week. Executive-level engagement. |
| Tier 2 | 60-79 | Standard: planned outreach within 2 weeks | Structured outreach sequence. Tailored value proposition. Discovery call within 3 weeks. |
| Tier 3 | 40-59 | Nurture: add to content marketing and event invitations | Monthly content touches. Quarterly check-ins. Monitor for tier-upgrade signals. |
| Tier 4 | <40 | Disqualify: do not pursue actively | Archive profile. Revisit quarterly for changed circumstances. |

---

## 4. Pipeline Math

Target prospect volume per tier to maintain a healthy pipeline:

| Metric | Target | Rationale |
|--------|--------|-----------|
| Tier 1 prospects (active) | 5-10 | High conversion rate (~30-40%). Core pipeline. |
| Tier 2 prospects (active) | 15-25 | Moderate conversion rate (~15-20%). Volume layer. |
| Tier 3 prospects (nurture) | 30-50 | Low conversion rate (~5-10%). Long-term pipeline. |
| New prospects researched/month | 10-15 | Replace converted, disqualified, or stale prospects. |
| Stale prospect review cycle | 90 days | Re-score and re-tier or archive. |

Conversion funnel benchmarks:
- Prospect → Discovery call: 25-35%
- Discovery call → Proposal: 40-50%
- Proposal → Signed engagement: 30-40%
- End-to-end (prospect → engagement): 3-7%

To maintain 2-3 active engagements at any time, keep at minimum 50-80 prospects across all tiers.

---

## 5. Red Flags (Poor Fit Indicators)

Flag any of the following — each one should reduce the ICP score and may warrant Tier 4 classification:

- **Cost-cutting mode**: Recent layoffs, public statements about reducing spend, hiring freeze.
- **No tech budget**: No tech leadership role, no tech job postings, no visible tech investment.
- **Previous bad consulting experience**: Public complaints, litigation, or negative references about past consulting engagements.
- **Active Big4 engagement**: Incumbent relationship with Deloitte, McKinsey, Accenture, or similar in the same domain.
- **Recently completed similar project**: Finished a comparable engagement within the last 12 months.
- **No digital ambition**: Purely offline business with no stated interest in technology adoption.
- **Unstable leadership**: Frequent C-suite turnover (3+ changes in 2 years) — indicates inability to commit to long-term initiatives.
- **Procurement complexity**: Government or heavily regulated procurement that requires RFP/tender process exceeding 6 months.

---

## 6. Green Flags (Strong Fit Indicators)

Each green flag should increase confidence in the ICP score and may justify tier upgrade:

- **New CTO/CIO**: New tech leadership (appointed within last 6 months) typically brings fresh strategy and consulting openness.
- **Digital transformation initiative**: Publicly announced modernization, cloud migration, or data strategy program.
- **Recent funding round**: Series A+ funding in last 12 months — capital available for tech investment.
- **Regulatory pressure**: New compliance requirements (GDPR, SOX, PCI, industry-specific) driving technology upgrades.
- **M&A integration**: Post-acquisition technology integration creates urgent consulting needs.
- **Rapid growth**: 30%+ employee growth in 12 months — infrastructure and processes likely lagging behind.
- **Legacy platform end-of-life**: Vendor sunsetting a core platform forces modernization.
- **Competitor disruption**: Competitors adopting new technology, creating pressure to follow.
- **Warm referral**: Existing client or network contact provides introduction.
- **Public tech pain signals**: Blog posts, conference talks, or job postings explicitly mentioning challenges (e.g., "scaling our monolith", "building our first data team").
