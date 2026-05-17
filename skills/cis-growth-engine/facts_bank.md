# Facts Bank — CIS Authority Engine

## Usage Rules
This facts bank stores verified, publicly sourced information for use in content generation. All entries must include a source type and confidence level. Facts are categorized by topic domain. This database is updated monthly.

### Confidence Levels
VERIFIED — Confirmed by multiple credible public sources (government reports, major research firms, publicly disclosed incident reports)
REPORTED — Confirmed by one credible public source (major news outlet, industry publication, organization's own disclosure)
INDUSTRY CONSENSUS — Widely acknowledged by practitioners and researchers without a single definitive source
FRAMEWORK-BASED — Derived from established frameworks (NIST, ISO, MITRE ATT&CK) — accurate as framework guidance, not necessarily universal statistics

### Usage Protocol
Never present INDUSTRY CONSENSUS facts as hard statistics without qualification.
Always attribute REPORTED facts to their source type (e.g., "according to publicly reported data").
VERIFIED facts can be stated more directly but still benefit from source attribution.
Never fabricate, estimate, or extrapolate beyond what is publicly documented.

---

## Domain 1: Cybersecurity

### Incident Response
- Organizations with tested incident response plans consistently report lower breach costs than those without tested plans. (VERIFIED — multiple annual breach cost studies confirm this pattern)
- Dwell time — the period between initial compromise and detection — remains a critical factor in breach severity. Longer dwell time correlates directly with greater data exposure and higher recovery costs. (VERIFIED — industry research consistently documents this relationship)
- Many organizations discover security incidents through external notification (customers, partners, law enforcement) rather than through internal monitoring. (REPORTED — disclosed in various incident post-mortems and security reports)

### Ransomware
- Ransomware attacks frequently target organizations during weekends, holidays, and overnight hours when monitoring coverage is reduced. (INDUSTRY CONSENSUS — documented in multiple incident analyses)
- Ransomware recovery is not simply paying or not paying a ransom — it involves system restoration, forensic investigation, regulatory notification, and often prolonged operational disruption. (VERIFIED — documented across multiple publicly disclosed incident reports)
- Organizations that maintain tested, offline backups are better positioned to recover from ransomware without paying ransoms. (FRAMEWORK-BASED — established in NIST and CISA guidance)

### Identity and Access Management
- Compromised credentials are among the most common initial access vectors for cyberattacks. (VERIFIED — consistently documented in annual security research reports)
- Privileged access accounts — those with elevated system permissions — represent disproportionate risk because their compromise gives attackers greater organizational reach. (FRAMEWORK-BASED — central principle of least-privilege access in NIST SP 800-53 and related frameworks)
- Multi-factor authentication significantly reduces the risk of credential-based account compromise. (VERIFIED — documented in multiple government and industry security reports)

### Vulnerability Management
- The gap between when a vulnerability is publicly disclosed and when organizations apply patches creates an exploitation window that attackers actively target. (INDUSTRY CONSENSUS — consistently documented in threat intelligence reporting)
- Not all vulnerabilities carry equal risk — prioritization based on exploitability and organizational exposure is more effective than attempting to patch everything immediately. (FRAMEWORK-BASED — CVSS scoring and risk-based vulnerability management frameworks)
- Legacy systems that cannot receive security patches represent a persistent and often difficult-to-address vulnerability in enterprise environments. (INDUSTRY CONSENSUS — widely documented across sectors)

---

## Domain 2: IT Infrastructure

### System Availability
- Unplanned downtime has measurable financial consequences for organizations across all sectors, with the severity varying significantly by industry, system criticality, and duration. (INDUSTRY CONSENSUS — documented in multiple availability and continuity research reports)
- Single points of failure — infrastructure components without redundancy — create disproportionate organizational risk because their failure causes cascading disruption. (FRAMEWORK-BASED — core principle in IT continuity planning and disaster recovery frameworks)
- Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO) are the measurable standards organizations use to define acceptable downtime and data loss limits. (FRAMEWORK-BASED — established in ISO 22301 and NIST SP 800-34 continuity frameworks)

### Change Management
- Poorly managed change processes are a significant source of unplanned outages in enterprise IT environments. (INDUSTRY CONSENSUS — documented in IT service management research and ITIL framework development)
- Changes made to production systems without proper testing, approval, and rollback procedures create unnecessary operational risk. (FRAMEWORK-BASED — ITIL and COBIT change management principles)

---

## Domain 3: Enterprise Systems

### ERP and Business Systems
- Enterprise Resource Planning systems are deeply integrated with core business operations — finance, supply chain, HR, manufacturing — making their availability critical to organizational function. (VERIFIED — documented in enterprise technology research and disclosed incident impacts)
- ERP implementation projects are among the most complex and high-risk technology initiatives organizations undertake, with well-documented histories of cost overruns and timeline extensions. (REPORTED — extensively covered in business and technology press)
- Organizations that do not adequately train users on enterprise systems see reduced ROI from their technology investments and increased error rates. (INDUSTRY CONSENSUS — documented in change management and ERP implementation research)

---

## Domain 4: Vendor Risk and Supply Chain

### Third-Party Risk
- Organizations increasingly depend on third-party vendors for critical business functions, creating supply chain dependencies that extend their risk surface beyond their own infrastructure. (VERIFIED — documented in supply chain security research and regulatory guidance)
- Third-party vendor access to organizational systems must be carefully managed, as vendor credentials and access pathways have been exploited in significant cyberattacks. (REPORTED — documented in publicly disclosed incident analyses)
- Organizations frequently have incomplete visibility into the full set of third-party vendors with access to their systems. (INDUSTRY CONSENSUS — noted in vendor risk management research and audit findings)

### Software Supply Chain
- Software supply chain attacks — where attackers compromise software used by organizations rather than attacking organizations directly — represent a sophisticated and difficult-to-defend attack vector. (VERIFIED — confirmed by government security agencies and documented in publicly disclosed incidents)
- Organizations that rely on commercial software without validating the integrity of updates and patches face supply chain risk they may not fully understand. (FRAMEWORK-BASED — NIST Secure Software Development Framework and related guidance)

---

## Domain 5: Data Protection

### Data Governance
- Data that is not classified, documented, and governed cannot be effectively protected. (FRAMEWORK-BASED — core principle across data protection frameworks including NIST and ISO 27001)
- Many organizations hold more sensitive data than they realize, because data accumulates across systems without systematic governance. (INDUSTRY CONSENSUS — noted in privacy research and audit findings)

### Regulatory Compliance
- Data protection regulations (including GDPR, CCPA, HIPAA, and sector-specific requirements) create legal obligations that connect IT decisions directly to legal and financial liability. (VERIFIED — established in law and regulatory guidance)
- Regulatory compliance does not equal security — compliance frameworks define minimum standards, not optimal security posture. (FRAMEWORK-BASED — acknowledged explicitly in multiple regulatory frameworks)
- Data breach notification requirements vary by jurisdiction and sector, creating compliance complexity for organizations operating across multiple regulatory environments. (VERIFIED — documented in regulatory frameworks)

---

## Domain 6: Cloud Security

### Cloud Adoption Risk
- Shared responsibility models in cloud environments mean that security responsibilities are divided between cloud providers and customer organizations — and many organizations misunderstand where their responsibilities begin. (VERIFIED — documented by major cloud providers and in cloud security research)
- Misconfigured cloud storage and services represent one of the most common causes of unintended data exposure in cloud environments. (REPORTED — documented in multiple publicly disclosed cloud security incidents)
- Cloud environments expand the attack surface organizations must manage, particularly as organizations adopt multiple cloud platforms simultaneously. (INDUSTRY CONSENSUS — documented in cloud security research)

---

## Maintenance Log
Last updated: Initial creation
Next scheduled update: Monthly
Update protocol: Add new verified facts as publicly sourced incidents and research are published. Mark outdated information rather than deleting it. Maintain a change history at the bottom of this file.
