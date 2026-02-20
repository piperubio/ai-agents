# Discovery Frameworks for B2B Technology Consulting

## Table of Contents
- [SPIN Question Bank by Service Line](#spin-question-bank-by-service-line)
- [Buying Committee Roles](#buying-committee-roles)
- [Pain Stack Framework](#pain-stack-framework)
- [Meeting Structure Templates](#meeting-structure-templates)
- [Active Listening Techniques](#active-listening-techniques)
- [Red Flags During Discovery](#red-flags-during-discovery)
- [Green Flags During Discovery](#green-flags-during-discovery)
- [Tech Maturity Quick-Assessment Questionnaire](#tech-maturity-quick-assessment-questionnaire)

---

## SPIN Question Bank by Service Line

### Software Engineering

**Situation** (10 questions):
1. "Describe your current application architecture at a high level — monolith, microservices, hybrid?"
2. "What is your primary tech stack and when were the core systems built?"
3. "How many releases do you ship per month, and what does the release process look like?"
4. "How large is the engineering team, and how is it organized (squads, chapters, feature teams)?"
5. "What does your CI/CD pipeline look like today?"
6. "How do you handle environment management (dev, staging, production)?"
7. "What technology investments have you made in the last 12-18 months?"
8. "How do you manage technical documentation and knowledge sharing?"
9. "What is your current approach to automated testing (unit, integration, e2e)?"
10. "How do you handle incident response and on-call rotation?"

**Problem** (10 questions):
1. "Where do you experience the most friction in your development cycle?"
2. "What technical debt concerns you the most right now?"
3. "How difficult is it to onboard new developers, and how long until they are productive?"
4. "Where do you have single points of failure in the codebase or team?"
5. "What features have you had to defer or descope due to architectural limitations?"
6. "How often do production incidents occur, and what is the mean time to resolution?"
7. "What manual processes consume the most engineering time?"
8. "Where do deployments break most frequently?"
9. "What quality issues reach production most often?"
10. "How challenging is it to scale the application for peak load periods?"

**Implication** (10 questions):
1. "When a critical bug appears, how long does it take to identify the root cause and deploy a fix?"
2. "How does the current architecture affect your ability to attract and retain senior engineers?"
3. "What revenue is at risk if the platform cannot scale for [growth initiative]?"
4. "If a key developer leaves, how long would it take to recover their domain knowledge?"
5. "How many hours per week does the team spend firefighting vs. building new features?"
6. "What is the business cost of each delayed release?"
7. "How does the current deployment friction affect your competitive speed-to-market?"
8. "What compliance or security risks exist in the current architecture?"
9. "If the codebase continues to grow without refactoring, what happens in 18 months?"
10. "How does developer frustration with the current stack affect team morale and attrition?"

**Need-Payoff** (10 questions):
1. "If your team could deploy independently per service, how would that change your roadmap?"
2. "What would it mean for the business if time-to-market for new features was cut in half?"
3. "How would better observability change your incident response?"
4. "If new developers were productive in two weeks instead of two months, what would that enable?"
5. "What would it mean to eliminate the current deployment bottleneck?"
6. "If automated testing caught 90% of regressions before production, how would that change your release confidence?"
7. "How would a modern developer experience affect your hiring pipeline?"
8. "If the platform could auto-scale for peak demand, what new business opportunities would open?"
9. "What would you do with the engineering hours currently spent on manual processes?"
10. "If you could safely experiment and rollback features, how would that change your product strategy?"

---

### Data & Analytics

**Situation** (10 questions):
1. "How do you currently collect, store, and process data across the organization?"
2. "What is your primary data warehouse or lake technology?"
3. "Who are the primary consumers of data — which teams, which roles?"
4. "What BI/analytics tools are in use today, and how widely adopted are they?"
5. "Do you have a dedicated data engineering team, or is data managed within other functions?"
6. "How do you handle data quality and governance today?"
7. "What is your current approach to data integration across source systems?"
8. "How do you manage access control and data security?"
9. "What is the volume and velocity of data you process daily?"
10. "How do you handle data retention and archival policies?"

**Problem** (10 questions):
1. "What data do stakeholders request that you cannot easily provide?"
2. "How long does it take to answer a new business question with data?"
3. "Where do you have data silos that prevent a unified view?"
4. "What manual data processes consume the most time?"
5. "How confident are business leaders in the accuracy of current reports?"
6. "What data pipeline failures occur most frequently, and how are they detected?"
7. "Where do data freshness issues cause the most business friction?"
8. "What data governance gaps keep you up at night?"
9. "How many 'shadow' spreadsheets or databases exist outside the official data platform?"
10. "What reporting requests does the data team consistently struggle to fulfill?"

**Implication** (10 questions):
1. "When leadership cannot get timely data, how does that affect strategic decisions?"
2. "What is the cost of manual reporting processes in headcount and hours?"
3. "How does the lack of a unified data view affect customer experience?"
4. "What regulatory risk exists with current data governance practices?"
5. "How much revenue is left on the table because insights arrive too late?"
6. "What happens when a data pipeline fails on a Monday morning before the executive dashboard refreshes?"
7. "How does data quality uncertainty affect trust in analytics across the organization?"
8. "What competitive disadvantage do you face from slower data-driven decision-making?"
9. "How many data engineer hours per week are spent fixing pipelines vs. building new ones?"
10. "What is the cost of maintaining legacy data infrastructure vs. investing in modernization?"

**Need-Payoff** (10 questions):
1. "If you had real-time access to [key metric], how would that change daily operations?"
2. "What decisions could you automate if the right data infrastructure existed?"
3. "How would self-service analytics change the dynamic between the data team and the business?"
4. "If a new data source could be integrated in days instead of months, what would you prioritize first?"
5. "What would it mean for the finance team to close the books in hours instead of weeks?"
6. "If data quality issues were caught automatically before reaching dashboards, how would that change trust in analytics?"
7. "How would a single source of truth across [systems] change cross-functional collaboration?"
8. "What would you build first if data engineering capacity doubled?"
9. "If you could run ad-hoc queries on all historical data in seconds, what new analyses would you attempt?"
10. "How would reliable data governance simplify your compliance burden?"

---

### AI / Machine Learning

**Situation** (10 questions):
1. "Are you currently using any ML/AI in production? If so, what use cases?"
2. "Do you have a data science team? How is it structured and where does it report?"
3. "What ML tools, platforms, or frameworks are you using or evaluating?"
4. "How much labeled data do you have for your priority use cases?"
5. "What is your current experimentation process for new ML models?"
6. "How do you currently move models from notebook to production?"
7. "What is your experience with LLMs/generative AI so far?"
8. "How do you handle model versioning and reproducibility?"
9. "What compute infrastructure do you use for training and inference?"
10. "How does the data science team collaborate with engineering and product?"

**Problem** (10 questions):
1. "What manual processes could benefit most from automation or prediction?"
2. "Where do your data scientists spend the most time on non-modeling work (data wrangling, infrastructure)?"
3. "What ML projects have you attempted that did not reach production, and why?"
4. "How do you currently handle model monitoring and retraining?"
5. "Where is the biggest gap between AI ambition and current capability?"
6. "What challenges have you faced with data quality or availability for ML use cases?"
7. "How long does it take to go from a model prototype to production deployment?"
8. "What AI/ML vendor tools have you tried and abandoned?"
9. "How do you handle bias detection and fairness in current models?"
10. "What governance challenges exist around AI usage in your organization?"

**Implication** (10 questions):
1. "What is the business value of the decisions currently made without ML support?"
2. "How does the gap in AI capability affect your competitive position?"
3. "What is the cost of the manual processes that could be automated with ML?"
4. "If models degrade in production without monitoring, what is the downstream business impact?"
5. "How does the prototype-to-production gap affect data scientist retention?"
6. "What revenue or cost-savings opportunities are you missing without predictive capabilities?"
7. "How does the lack of AI governance expose you to regulatory or reputational risk?"
8. "What happens when a competitor deploys the AI capability you have been planning?"
9. "How does the absence of MLOps affect experiment velocity and model reliability?"
10. "What is the opportunity cost of data scientists spending 70% of their time on infrastructure?"

**Need-Payoff** (10 questions):
1. "If you could predict [outcome] with 80%+ accuracy, what would you do differently?"
2. "What would it mean for your team to have a reliable ML pipeline from experimentation to production?"
3. "How would automated [process] free up your team's capacity?"
4. "If you had an MLOps platform, how would that change your experimentation velocity?"
5. "What new products or features could you offer with reliable AI capabilities?"
6. "How would real-time inference change your customer-facing operations?"
7. "If data scientists could focus 80% on modeling instead of wrangling, what use cases would they tackle first?"
8. "What would responsible AI governance enable you to do that you currently avoid?"
9. "How would generative AI capabilities change your content, support, or internal workflows?"
10. "If you could deploy a model in days instead of months, how would that change your product roadmap?"

---

## Buying Committee Roles

### Champion
- **Definition**: Internal advocate who wants the project to happen. Signs off internally, rallies support, and sells the initiative inside the organization.
- **Identification tactics**:
  - Ask "Who initiated this conversation?" — the answer often reveals the Champion.
  - Look for the person who follows up proactively, shares internal documents, and makes introductions.
  - Ask "Who benefits most personally if this project succeeds?"
  - Notice who provides the most context and asks the most forward-looking questions.
  - Test commitment: "Would you be comfortable presenting this initiative to your leadership team?"

### Economic Buyer
- **Definition**: Controls the budget and makes the financial decision. May not be in the room during initial discovery.
- **Identification tactics**:
  - Ask "Who approves budget for this type of investment?"
  - Ask "What is the approval process for an engagement of this size?"
  - Ask "Is there an existing budget line for this, or would it require new budget approval?"
  - Listen for phrases like "I'd need to get approval from..." or "My boss would need to sign off."
  - Ask "Who else would need to be comfortable with the investment before moving forward?"

### Technical Buyer
- **Definition**: Evaluates the technical approach, validates feasibility, and assesses whether the proposed solution fits the existing architecture and team.
- **Identification tactics**:
  - Ask "Who will evaluate the technical proposal?"
  - Ask "Who on your team has the deepest expertise in [relevant technology area]?"
  - Look for the person asking detailed technical questions about methodology, tools, and architecture.
  - Ask "Who would your team look to for a technical recommendation on this?"
  - Notice who raises concerns about integration, compatibility, or technical risk.

### Coach
- **Definition**: Internal advocate who provides inside information, warns about landmines, and helps navigate the organization's politics. May or may not be a formal stakeholder.
- **Identification tactics**:
  - Look for the person who shares "off the record" context about internal dynamics.
  - Ask "Is there anything we should know about how decisions like this typically get made here?"
  - Notice who volunteers information about other stakeholders' preferences or concerns.
  - Build trust with mid-level managers who have organizational context but less political risk.
  - Ask "Who else should we be talking to that we have not yet met?"

### Blocker
- **Definition**: Resists the project — may have competing priorities, feel threatened, or prefer an alternative approach. Not always adversarial; sometimes simply risk-averse.
- **Identification tactics**:
  - Ask "Who might have concerns about bringing in external help for this?"
  - Ask "Has anyone expressed reservations about this initiative?"
  - Listen for mentions of competing internal projects or "we tried that before" skepticism.
  - Notice who is absent from meetings but has influence — voluntary absence may signal resistance.
  - Ask "What would need to be true for [skeptical person] to support this initiative?"
  - Look for the person who asks "why can't we do this ourselves?" — address with respect, not dismissal.

---

## Pain Stack Framework

Document pain at three layers to build compelling business cases. Each layer amplifies urgency.

### Layer 1: Technical Pain
The specific technical problem observable in systems, code, or infrastructure.
- Example: "ETL pipelines fail 3x per week due to schema drift."
- Example: "Monolithic application takes 45 minutes to deploy."
- Example: "No automated testing — every release requires 2 days of manual QA."

### Layer 2: Business Pain
The business impact of the technical problem — measurable in revenue, cost, time, or risk.
- Example: "Dashboard downtime costs $15K/day in delayed logistics decisions."
- Example: "Slow releases mean competitors ship features 3x faster."
- Example: "Manual QA bottleneck limits releases to 2 per month, blocking the product roadmap."

### Layer 3: Personal Pain
How the problem affects specific individuals' careers, KPIs, performance reviews, or reputation.
- Example: "VP of Data's credibility is eroding because executives do not trust the dashboards."
- Example: "CTO promised the board a platform modernization by Q3 — currently behind schedule."
- Example: "Head of Engineering is losing senior developers who are frustrated with the legacy stack."

### How to Use the Pain Stack
1. Start with technical pain (safe, factual, easy to discuss).
2. Escalate to business pain (connects to priorities the economic buyer cares about).
3. Surface personal pain (builds emotional urgency — handle with care and empathy).
4. In proposals, present all three layers to create a complete narrative of impact.

---

## Meeting Structure Templates

### First Discovery Meeting (60 min)

| Time | Activity | Notes |
|------|----------|-------|
| 0-5 min | Introductions and agenda | Set expectations: "Our goal is to understand your situation deeply so we can determine if and how we can help." |
| 5-10 min | Their context | Ask them to describe the initiative in their own words. Listen for framing and priorities. |
| 10-25 min | Situation & Problem questions | Use 4-5 Situation questions, then transition to 4-5 Problem questions. Follow the thread — do not stick rigidly to the script. |
| 25-40 min | Implication & Need-payoff questions | Quantify impact: "How often?", "What does that cost?", "What is the risk?" Transition to Need-payoff to envision the future state. |
| 40-50 min | Buying process & timeline | Ask about decision process, budget cycle, timeline drivers, other vendors. |
| 50-55 min | Stakeholder mapping | "Who else should we include in the next conversation?" "Who makes the final decision?" |
| 55-60 min | Next steps | Agree on concrete next action, owner, and date. Summarize key takeaways. |

### Follow-Up Discovery Meeting (45 min)

| Time | Activity | Notes |
|------|----------|-------|
| 0-5 min | Recap and validate | Summarize findings from the first meeting. Ask "Did I capture this correctly?" |
| 5-15 min | Deep-dive on priority pain | Explore the #1 pain point in depth. Get specific metrics, examples, and history. |
| 15-25 min | Gap analysis | Walk through current state → desired state for each area (Software / Data / AI). |
| 25-35 min | Organizational readiness | Team capabilities, change management concerns, internal alignment. |
| 35-40 min | Budget and timeline refinement | Indirect budget probing: "For context, engagements like this typically range from X to Y — does that align with what you had in mind?" |
| 40-45 min | Next steps | Confirm who else to involve, agree on technical deep-dive if needed. |

### Technical Deep-Dive (90 min)

| Time | Activity | Notes |
|------|----------|-------|
| 0-10 min | Context setting | Brief recap for technical audience. Explain what you are evaluating and why. |
| 10-30 min | Architecture walkthrough | Ask them to walk through their current architecture (ideally with diagrams). Document components, integrations, and data flows. |
| 30-50 min | Technical pain deep-dive | Drill into specific systems causing problems. Ask for logs, metrics, or dashboards if available. |
| 50-70 min | Solution landscape discussion | Explore what they have considered, what constraints exist (compliance, vendor lock-in, team skills). Do NOT propose a solution — explore their thinking. |
| 70-80 min | Tech maturity assessment | Run the 5-question assessment per axis. Compare with pre-meeting estimates. |
| 80-90 min | Summary and next steps | Summarize technical findings. Agree on what additional access or information is needed. |

---

## Active Listening Techniques

1. **Mirroring**: Repeat the last 2-3 words of what the prospect said as a question. Forces them to elaborate. ("...and that has been really frustrating." → "Really frustrating?")
2. **Labeling**: Name the emotion or concern you observe. ("It sounds like there is real urgency around the Q4 deadline.")
3. **Summarizing back**: Paraphrase their statement and ask for confirmation. ("So if I understand correctly, the core issue is X. Is that right?")
4. **Comfortable silence**: After asking a question, wait. Do not fill the silence. The prospect will often share more if given space.
5. **Follow the thread**: When the prospect mentions something unexpected, pursue it. The unscripted moments often reveal the deepest pain.
6. **Quantify everything**: When they describe a problem, ask for numbers. "How often?", "How many hours?", "What does that cost?", "How many people are affected?"
7. **Capture exact words**: Write down their exact phrases. Use these words in proposals — it signals you listened and understood.
8. **Check for agreement**: Periodically ask "Is this the right area to focus on, or is there something more pressing?"

---

## Red Flags During Discovery

Watch for these signals that an opportunity may not be real or viable:

1. **Prospect will not commit time**: Cancels or reschedules repeatedly, limits meetings to 15-20 minutes, or sends junior proxies to discovery calls.
2. **No clear champion**: Nobody internally is advocating for the project. The initiative was assigned, not desired.
3. **Shopping for lowest price**: First question is "What is your rate?" or "How much would this cost?" without interest in understanding scope or approach.
4. **Scope too vague even after probing**: After a full discovery session, the prospect still cannot articulate what they want to achieve. Vagueness after probing (not before) is the red flag.
5. **No urgency driver**: No deadline, no executive mandate, no competitive pressure. "We are just exploring" with no catalyst.
6. **Decision-maker inaccessible**: The champion cannot or will not provide access to the economic buyer or decision-maker.
7. **History of stalled initiatives**: "We have been talking about this for two years" with no progress — indicates systemic blockers.
8. **Unrealistic expectations**: Wants enterprise-grade transformation on a startup budget, or expects delivery in an impossible timeline.
9. **Internal politics dominate**: Multiple factions with competing agendas; the project is a political football rather than a business need.
10. **Resistance to sharing information**: Will not share architecture diagrams, team structure, or budget range — signals lack of trust or seriousness.

---

## Green Flags During Discovery

Signals that an opportunity is real, funded, and likely to close:

1. **Executive sponsor engaged**: A senior leader (VP+) is personally invested, attends meetings, and allocates internal resources.
2. **Clear budget allocated**: Budget exists and is approved (or approval is a formality). Prospect discusses budget range openly.
3. **Defined timeline**: Specific deadline driven by business event (product launch, compliance deadline, fiscal year, board commitment).
4. **Acknowledged failed past attempts**: "We tried this internally and it did not work" — indicates they understand the problem's difficulty and value external help.
5. **Multiple stakeholders involved**: They bring technical leads, business owners, and decision-makers to discovery — signals organizational buy-in.
6. **Proactive information sharing**: Sends architecture docs, org charts, or data samples before being asked.
7. **Asking about methodology**: Interested in how you work (process, team structure, delivery cadence) — signals they are evaluating fit, not just price.
8. **Introducing you to others**: "You should talk to [name] about this" — the champion is building internal consensus.
9. **Discussing implementation details**: Questions about team integration, security requirements, or onboarding process — thinking past the sale.
10. **Urgency in follow-up**: Responds quickly, proposes next meetings proactively, asks for proposals or next steps.

---

## Tech Maturity Quick-Assessment Questionnaire

Use these 5 questions per axis during discovery to estimate maturity level (1-5 scale). Compare self-reported answers with observed indicators.

### Software Engineering Maturity

1. **Deployment frequency**: How often do you deploy to production?
   - 1: Monthly or less | 2: Bi-weekly | 3: Weekly | 4: Daily | 5: On-demand (multiple per day)

2. **Automated testing coverage**: What percentage of code changes are validated by automated tests?
   - 1: None | 2: <20% | 3: 20-60% | 4: 60-85% | 5: >85% with CI gates

3. **Mean time to recovery**: When production breaks, how long to restore service?
   - 1: Days | 2: Hours | 3: 1-4 hours | 4: <1 hour | 5: <15 minutes (automated rollback)

4. **Architecture modularity**: How independently can teams build and deploy features?
   - 1: Fully coupled monolith | 2: Monolith with some extraction | 3: Modular monolith or partial services | 4: Service-oriented with some coupling | 5: Independent services with clear contracts

5. **Developer experience**: How long until a new developer ships their first change to production?
   - 1: >1 month | 2: 2-4 weeks | 3: 1-2 weeks | 4: 2-5 days | 5: First day

### Data Maturity

1. **Data integration**: How are data sources connected and consolidated?
   - 1: Manual exports/imports | 2: Scheduled batch scripts | 3: Managed ETL pipelines | 4: Orchestrated pipelines with monitoring | 5: Real-time streaming with data contracts

2. **Data quality**: How do you ensure data accuracy and completeness?
   - 1: No formal process | 2: Ad-hoc spot checks | 3: Basic validation rules | 4: Automated quality checks with alerting | 5: Data observability platform with SLAs

3. **Self-service analytics**: Can business users answer their own data questions?
   - 1: All requests go to IT/data team | 2: Some dashboards, most requests manual | 3: BI tools widely available, some adoption | 4: Most teams self-serve with governed datasets | 5: Data mesh / domain-owned, self-serve with catalog

4. **Data governance**: How do you manage access, lineage, and compliance?
   - 1: No formal governance | 2: Basic access controls | 3: Documented policies, partial enforcement | 4: Automated governance with lineage tracking | 5: Full governance framework with automated compliance

5. **Time to insight**: How long to go from a new business question to a data-backed answer?
   - 1: Weeks to months | 2: 1-2 weeks | 3: 2-5 days | 4: Same day | 5: Minutes (self-serve or real-time)

### AI/ML Maturity

1. **ML in production**: How many ML models are serving production traffic?
   - 1: None | 2: 1-2 experimental | 3: 3-5 in production | 4: 5-15 with some automation | 5: 15+ with full MLOps

2. **Experimentation process**: How do you test and validate new models?
   - 1: No formal process | 2: Ad-hoc notebooks | 3: Structured experiments with tracking | 4: Automated experiment pipelines | 5: Full A/B testing with automated model selection

3. **Model operations**: How do you monitor and maintain production models?
   - 1: No monitoring | 2: Manual checks | 3: Basic performance dashboards | 4: Automated drift detection and alerts | 5: Automated retraining with CI/CD for models

4. **Data readiness for ML**: How prepared is your data for ML use cases?
   - 1: Data not accessible for ML | 2: Raw data available, heavy prep needed | 3: Some curated datasets | 4: Feature store with versioned datasets | 5: Automated feature engineering with data contracts

5. **AI strategy and governance**: How formalized is your AI approach?
   - 1: No AI strategy | 2: Exploring opportunistically | 3: Defined use cases with executive support | 4: AI roadmap with dedicated budget and team | 5: AI-first strategy with governance, ethics review, and ROI tracking
