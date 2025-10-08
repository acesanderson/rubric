from conduit.sync import Model, Verbosity, ConduitCache
from rubric.score import score_cert, PartnershipEvaluation

cache = ConduitCache()
Model.conduit_cache = cache

verbose = Verbosity.COMPLETE


titles = """
Change Management Professional Certificate by ACMP (Association of Change Management Professionals)
Change Management Professional Certificate by ACMP (Association of Change Management Professionals)
AI Engineering Professional Certificate by AI Engineer
Responsible AI Professional Certificate by All Tech is Human
Critical Thinking and Decision-Making Professional Certificate by American Management Association (AMA)
Time Management Professional Certificate by American Management Association (AMA)
Quality Management and Lean Six Sigma Professional Certificate by American Society for Quality (ASQ)
Deep Learning with Python Professional Certificate by Anaconda
Generative AI for Developers Professional Certificate by Anthropic
Instructional Design Professional Certificate by Articulate
Time Management Professional Certificate by Asana
Emotional Intelligence Professional Certificate by Association for Talent Development (ATD)
Business Communication Skills Professional Certificate by Association for Talent Development (ATD)
Change Management Professional Certificate by Association for Talent Development (ATD)
Talent Development Essentials Professional Certificate by Association for Talent Development (ATD)
Time Management Professional Certificate by Association for Talent Development (ATD)
Identity and Access Management (IAM) Professional Certificate by Auth0
AutoCAD Professional Certificate by Autodesk
Critical Thinking and Decision-Making Professional Certificate by Behavioral Science & Policy Association (BSPA)
Critical Thinking and Decision-Making Professional Certificate by Center for Creative Leadership (CCL)
Emotional Intelligence Professional Certificate by Center for Creative Leadership (CCL)
Change Management Professional Certificate by Center for Creative Leadership (CCL)
IT Security Fundamentals Professional Certificate by Cisco
Building AI Products: Security Essentials Professional Certificate by Cloud Security Alliance
Cybersecurity Management Professional Certificate by Cloud Security Alliance
Change Management Professional Certificate by CMI (Change Management Institute)
Change Management Professional Certificate by CMI (Change Management Institute)
IT Security Fundamentals Professional Certificate by Crowdstrike
Identity and Access Management (IAM) Professional Certificate by Cyberark
Business Communication Skills Professional Certificate by Dale Carnegie Training
Database Administration Professional Certificate by DAMA International
Database Administration Professional Certificate by DAMA International
Emotional Intelligence Professional Certificate by Daniel Goleman (Goleman, Inc.)
Machine Learning Operations (MLOps) Professional Certificate by Databricks
Cloud-Native Security Professional Certificate by Datadog
Building AI Products: Understanding the AI Workflow Professional Certificate by DataRobot
Emotional Intelligence Professional Certificate by Deloitte Human Capital
Critical Thinking and Decision-Making Professional Certificate by Deloitte, PricewaterhouseCoopers (PwC), Ernst & Young (EY), KPMG, McKinsey & Company, Bain & Company
Change Management Professional Certificate by Deloitte, PricewaterhouseCoopers (PwC), Ernst & Young (EY), KPMG, McKinsey & Company, Bain & Company
Governance, Risk, and Compliance (GRC) Professional Certificate by Deloitte, PricewaterhouseCoopers (PwC), Ernst & Young (EY), KPMG, McKinsey & Company, Bain & Company
Governance, Risk, and Compliance (GRC) Professional Certificate by Deloitte, PricewaterhouseCoopers (PwC), Ernst & Young (EY), KPMG, McKinsey & Company, Bain & Company
Governance, Risk, and Compliance (GRC) Professional Certificate by Deloitte, PricewaterhouseCoopers (PwC), Ernst & Young (EY), KPMG, McKinsey & Company, Bain & Company
UX Design Professional Certificate by Design Management Institute (DMI)
UX Design Professional Certificate by Design Research Society
Building AI Products: Prototyping Essentials Professional Certificate by Design Thinking Institute
Governance, Risk, and Compliance (GRC) Professional Certificate by Diligent
Edge AI Professional Certificate by Edge AI Foundation
Building AI Products: Security Essentials Professional Certificate by Elastic
Building AI Products: Prototyping Essentials Professional Certificate by Figma
UX Design Professional Certificate by Figma
IT Security Fundamentals Professional Certificate by Fortinet
Time Management Professional Certificate by FranklinCovey
UX Design Professional Certificate by Frog Design
Building AI Products: Understanding the AI Workflow Professional Certificate by Gartner
Governance, Risk, and Compliance (GRC) Professional Certificate by Gartner
TBD Professional Certificate by Google Cloud
Teamwork and Collaboration Professional Certificate by Great Place to Work
Emotional Intelligence Professional Certificate by Greater Good Science Center (UC Berkeley)
Generative AI and Prompting Essentials Professional Certificate by Grow with Google
TBD Professional Certificate by Guild
Generative AI for Business Partners Professional Certificate by Harvard Business School
Cloud-Native Security Professional Certificate by Hashicorp
Business Communication Skills Professional Certificate by IABC
Governance, Risk, and Compliance (GRC) Professional Certificate by IBM Security
Building AI Products: Understanding the AI Workflow Professional Certificate by IDC
Building AI Products: Prototyping Essentials Professional Certificate by IDEO
UX Design Professional Certificate by IDEO
Cybersecurity Management Professional Certificate by Information Systems Security Association (ISSA)
Cybersecurity Topics Professional Certificate by Information Systems Security Association (ISSA)
Critical Thinking and Decision-Making Professional Certificate by INFORMS
Emotional Intelligence Professional Certificate by Institute for Health and Human Potential (IHHP)
Generative AI for Customer Service Professional Certificate by Intercom
Emotional Intelligence Professional Certificate by International Coaching Federation (ICF)
Building AI Products: Security Essentials Professional Certificate by ISACA
Governance, Risk, and Compliance (GRC) Professional Certificate by ISACA
Interaction Design Professional Certificate by IxDA (Interaction Design Association)
Kotlin Development Professional Certificate by JetBrains
Change Management Professional Certificate by Korn Ferry
Governance, Risk, and Compliance (GRC) Professional Certificate by KPMG
Organizational Emotional Intelligence Professional Certificate by McKinsey Organizational Practice
UX Design Professional Certificate by Miro
Building AI Products: Prototyping Essentials Professional Certificate by Miro
Building AI Products: Security Essentials Professional Certificate by Mistral
UX Design Professional Certificate by Nielsen Norman Group
Identity and Access Management (IAM) Professional Certificate by Okta
Cloud-Native Security Professional Certificate by OWASP
IT Security Fundamentals Professional Certificate by Palo Alto Networks
Building AI Products: Prototyping Essentials Professional Certificate by Product Development Management Association (PDMA)
Generative AI for Project Management Professional Certificate by Project Management Institute
Rapid Prototyping Professional Certificate by Rapid Prototyping Association
IT Security Fundamentals Professional Certificate by Rapid7
Building AI Products: Security Essentials Professional Certificate by SANS Institute
Governance, Risk, and Compliance (GRC) Professional Certificate by SANS Institute
Governance, Risk, and Compliance (GRC) Professional Certificate by SANS Institute
SAP Consulting Professional Certificate by SAP
Mindfulness and Emotional Intelligence Professional Certificate by Search Inside Yourself Leadership Institute (SIYLI)
IT Security Fundamentals Professional Certificate by SentinelOne
Emotional Intelligence Professional Certificate by Six Seconds
Cloud-Native Security Professional Certificate by Snyk
Emotional Intelligence Professional Certificate by Society for Human Resource Management (SHRM)
Business Communication Skills Professional Certificate by Society for Human Resource Management (SHRM)
Change Management Professional Certificate by Society for Human Resource Management (SHRM)
Generative AI for HR Professional Certificate by Society for Human resource Management (SHRM)
Time Management Professional Certificate by Society for Human Resource Management (SHRM)
Judgment and Decision-Making Professional Certificate by Society for Judgment and Decision Making (SJDM)
Database Administration Professional Certificate by Solarwinds
Building AI Products: Security Essentials Professional Certificate by Splunk
IT Security Fundamentals Professional Certificate by Splunk
Emotional Intelligence Professional Certificate by TalentSmart
UX Design Professional Certificate by UserTesting
UX Design Professional Certificate by UX Collective
UX Design Professional Certificate by UXPA (User Experience Professionals Association)
UX Design Professional Certificate by UXPA (User Experience Professionals Association)
Governance, Risk, and Compliance (GRC) Professional Certificate by Vanta
Building AI Products: Architecture and Orchestration Professional Certificate by Weights and Biases
Cloud-Native Security Professional Certificate by Wiz
Time Management Professional Certificate by WorldatWork
AI Business Automation Professional Certificate by Zapier
Cloud-Native Security Professional Certificate by Zscaler
""".strip().split("\n")

scores = []
for index, title in enumerate(titles):
    print(f"Scoring {index + 1}/{len(titles)}: {title}")
    evaluation = score_cert(title)
    print("-------" * 10)
    print(evaluation.human_readable_summary)
    print("-------" * 10)
    score = evaluation.total_score
    scores.append(score)

for score in scores:
    print(score)
