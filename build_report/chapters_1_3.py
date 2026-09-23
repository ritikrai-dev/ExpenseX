import docx
from docx.shared import Inches, Pt, RGBColor
from build_report.styles import (
    FONT_NAME, COLOR_PRIMARY, COLOR_TEXT, COLOR_MUTED,
    add_chapter_heading, add_section_heading, add_subsection_heading,
    add_subsubsection_heading, add_body_p, add_bullet_p, add_numbered_p,
    add_styled_table, add_figure_box, add_callout_box
)

def build_chapters_1_to_3(doc):
    # =========================================================================
    # CHAPTER 1 — PRELIMINARY INVESTIGATION
    # =========================================================================
    add_chapter_heading(doc, "CHAPTER 1", "PRELIMINARY INVESTIGATION")
    
    add_section_heading(doc, "1.1", "Organizational and Domain Overview")
    add_body_p(
        doc,
        "In the contemporary global financial landscape, the digitization of personal financial management (PFM) "
        "has emerged as one of the most vital frontiers in consumer technology. Historically, individuals relied "
        "predominantly on tactile instruments such as physical accounting ledgers, paper receipts, passbooks, and manual "
        "cash-envelope budgeting systems. While these legacy mechanisms provided foundational financial awareness, they "
        "demanded exhaustive manual effort, suffered from catastrophic vulnerabilities such as physical degradation or loss, "
        "and lacked any computational capability to derive meaningful analytical insights or predictive trajectories."
    )
    add_body_p(
        doc,
        "With the proliferation of personal computing in the late twentieth century, personal finance transitioned into "
        "electronic spreadsheets (e.g., Microsoft Excel, Lotus 1-2-3). While digital workbooks eliminated mechanical math "
        "errors, they introduced significant cognitive friction. Users were forced to manually transcribe figures from bank "
        "slips, craft bespoke mathematical formulas, manually design charts, and maintain local files without automated "
        "synchronization across devices. More critically, spreadsheets represent passive repositories of historical data; they "
        "cannot provide proactive alerts, contextual guidance, or algorithmic financial behavioral coaching."
    )
    add_body_p(
        doc,
        "In the modern era of ubiquitous high-speed internet and cloud architectures, FinTech platforms have attempted to bridge "
        "this gap. However, the commercial landscape is currently divided between two problematic extremes: highly intricate "
        "enterprise accounting software (such as QuickBooks, SAP, or Tally) designed for corporate entities, and consumer mobile "
        "apps (such as Mint, Splitwise, or Walnut) that frequently monetize sensitive user financial habits through aggressive "
        "targeted advertising, third-party data tracking, or expensive recurring monthly paywalls. Furthermore, traditional "
        "budgeting software operates with static heuristics, lacking the cognitive capacity to interpret complex individual "
        "spending contexts."
    )
    add_body_p(
        doc,
        "ExpenseX — Smart Expense Tracker is conceived and developed to disrupt this paradigm by delivering an open, secure, "
        "full-stack web platform built upon modern web engineering principles. By uniting a responsive React 19 Single Page "
        "Application (SPA) frontend with a scalable Node.js and Express RESTful backend, a cloud-hosted MongoDB Atlas document store, "
        "and generative artificial intelligence capabilities powered by the Google Gemini API, ExpenseX offers an intelligent, "
        "accessible, and completely private personal financial control center for modern digital citizens."
    )

    add_section_heading(doc, "1.2", "Description of the System")
    add_body_p(
        doc,
        "ExpenseX is an enterprise-grade full-stack web application designed from the ground up to empower users to record, "
        "categorize, monitor, analyze, and forecast their financial activities through an intuitive digital interface. "
        "Unlike generic tracking tools, ExpenseX operates as an active financial co-pilot, transforming raw monetary transactions "
        "into structured, actionable intelligence."
    )
    add_body_p(
        doc,
        "The system's core capabilities encompass a spectrum of specialized subsystems:"
    )
    add_bullet_p(doc, "Dual-Mode Architecture", "ExpenseX uniquely features a dual-operational paradigm. Users can authenticate into a secure, persistent cloud environment backed by MongoDB Atlas, or instantly explore full application capabilities through a zero-barrier Guest/Demo simulation mode that leverages browser local storage without exposing backend credentials.")
    add_bullet_p(doc, "Stateless Cryptographic Security", "Client-server communication is governed by stateless JSON Web Tokens (JWT) transmitted via Bearer headers, while user authentication credentials are protected using one-way salted bcrypt hashing (cost factor 10), ensuring bulletproof isolation across user profiles.")
    add_bullet_p(doc, "Dynamic Transaction Lifecycle Management", "Users can execute complete CRUD (Create, Read, Update, Delete) operations on monetary entries, categorizing cash flows into Income or Expense streams, assigning specialized payment vectors (Cash, UPI, Debit Card, Credit Card, Bank Transfer, Net Banking, Wallet), and logging contextual metadata.")
    add_bullet_p(doc, "High-Performance Data Retrieval", "The backend implements skip/limit pagination, search indexing, and real-time filtering algorithms, enabling instantaneous querying across thousands of transaction records with minimal server overhead.")
    add_bullet_p(doc, "Interactive Visual Analytics", "Integrating Recharts charting primitives, the client renders dynamic drill-down category Pie Charts and multi-month expense trend Line Charts, providing immediate visual breakdowns of cash flow.")
    add_bullet_p(doc, "Generative AI Financial Intelligence", "Leveraging the Google Gemini 2.5 Flash model through the official @google/genai SDK, ExpenseX synthesizes categorical expense distributions into structured prompts, extracting deterministic JSON-structured financial health scores, risk diagnoses, smart overspending alerts, and actionable next-month goals.")
    add_bullet_p(doc, "Industrial Multi-Format Reporting", "A dedicated server-side reporting engine allows instantaneous generation and streaming of PDF statements (via PDFKit), styled Excel spreadsheets (via ExcelJS), standard CSV sheets (via json2csv), and raw JSON archives.")

    add_section_heading(doc, "1.3", "Limitations of Present and Traditional Systems")
    add_body_p(
        doc,
        "An exhaustive empirical investigation of conventional personal financial management methodologies reveals multiple "
        "systemic deficiencies that inhibit long-term user adherence and financial wellness:"
    )
    add_bullet_p(doc, "High Vulnerability to Human Error", "Manual ledger writing and spreadsheet data entry rely entirely on user diligence. Transposition typos, calculation errors, missed entries, and accidental cell formula overwrites frequently corrupt financial calculations.")
    add_bullet_p(doc, "Absence of Cross-Device Portability", "Physical notebooks and offline desktop spreadsheet files cannot be accessed seamlessly while on the move, leading to significant delays in transaction logging and eventual abandonment of budgeting discipline.")
    add_bullet_p(doc, "Privacy Intrusion in Commercial Apps", "Most free commercial expense applications monetize user spending habits by collecting telemetry, indexing financial behaviors, and selling targeted lead generation to lending institutions and credit card companies.")
    add_bullet_p(doc, "Subscription Paywalls and Feature Gating", "Leading consumer apps lock fundamental features—such as multi-format data export, advanced visualizations, and multi-month historical analytics—behind recurring monthly subscription fees.")
    add_bullet_p(doc, "Static and Rigid Category Frameworks", "Conventional software enforces hardcoded spending categories that fail to adapt to modern spending patterns (e.g., micro-subscriptions, UPI digital micropayments, peer-to-peer transfers).")
    add_bullet_p(doc, "Lack of Intelligent Behavioral Coaching", "Traditional tools merely display historical numbers without providing contextual evaluation. They fail to identify dangerous spending spikes, calculate financial stability ratios, or suggest personalized, achievable savings benchmarks.")

    add_section_heading(doc, "1.4", "Proposed ExpenseX System and Advantages")
    add_subsection_heading(doc, "1.4.1", "Proposed System Architecture & Core Capabilities")
    add_body_p(
        doc,
        "The proposed ExpenseX platform is designed as a modern, decoupled, three-tier cloud-native web application. "
        "At the client layer, React 19 coupled with the Vite build tool provides lightning-fast page loads, optimized virtual DOM reconciliation, "
        "and modular Single Page Application routing via React Router v7. State management is handled through clean reactive hooks, "
        "delivering seamless transitions between Landing, Authentication, Dashboard, Transactions, Analytics, AI Insights, Reports, "
        "and Profile Settings views."
    )
    add_body_p(
        doc,
        "At the middle tier, a lightweight Node.js runtime hosting an Express.js 5 application functions as a robust RESTful API gateway. "
        "The backend enforces strict cross-origin resource sharing (CORS) rules, parses incoming JSON payloads, authenticates requests via "
        "custom JWT middleware, and encapsulates domain logic into dedicated controllers (auth, user, transaction, dashboard, analytics, "
        "ai, and report controllers)."
    )
    add_body_p(
        doc,
        "At the data tier, MongoDB Atlas provides an elastically scalable NoSQL document repository. Schemas are governed and validated "
        "programmatically through Mongoose 8, enforcing data integrity constraints, foreign-key referencing, and compound indexing for "
        "high-speed query resolution."
    )

    add_subsection_heading(doc, "1.4.2", "Distinct Technical Advantages")
    add_bullet_p(doc, "Zero-Friction Accessibility", "ExpenseX requires no software installation or app store provisioning; users access the complete application via modern web browsers on desktop, laptop, tablet, or smartphone.")
    add_bullet_p(doc, "Stateless Scalability", "The REST API architecture is completely stateless; session state is maintained on the client via encrypted JWT tokens, allowing the backend to scale horizontally across serverless or containerized cloud instances without session stickiness issues.")
    add_bullet_p(doc, "Algorithmic AI Advice", "By integrating the Gemini 2.5 Flash model, users receive high-level financial analysis without incurring expensive financial consulting fees.")
    add_bullet_p(doc, "Data Portability & Sovereignty", "Users retain total ownership of their financial records, possessing the unrestricted ability to export their full ledger into PDF, Excel, CSV, or JSON formats at any time.")
    add_bullet_p(doc, "Privacy-First Architecture", "ExpenseX does not incorporate third-party advertising networks, analytical trackers, or data-broker SDKs. Financial summaries sent to the Gemini API are strictly anonymized, stripped of user identities or account identifiers.")

    add_section_heading(doc, "1.5", "Objectives of the Project")
    add_body_p(
        doc,
        "The primary engineering and operational objectives established for the ExpenseX software project comprise:"
    )
    add_numbered_p(doc, "1", "Engineered Full-Stack Architecture", "To architect, build, and deploy an end-to-end cloud web application demonstrating best practices in MERN stack development, modular code decoupling, and strict REST API design.")
    add_numbered_p(doc, "2", "Stateless Authentication Engine", "To implement an industrial-strength authentication subsystem utilizing bcrypt for password hashing and JSON Web Tokens for stateless route authorization and secure session management.")
    add_numbered_p(doc, "3", "High-Throughput CRUD Operations", "To engineer responsive transaction management workflows enabling rapid addition, real-time editing, deletion, pagination, dynamic search, and filtering of monetary cash flows.")
    add_numbered_p(doc, "4", "Reactive Visual Analytics", "To implement responsive, interactive data visualization components using Recharts, allowing users to drill down into categorical expenditures and analyze multi-month spending velocity.")
    add_numbered_p(doc, "5", "Deterministic AI Synthesis", "To integrate the Google Gemini 2.5 Flash LLM via structured prompt engineering, ensuring reliable generation of JSON-formatted financial diagnostics, scoring, and actionable coaching without schema deviation.")
    add_numbered_p(doc, "6", "Automated Multi-Format Export", "To construct a high-performance server-side document generation pipeline supporting programmatic PDF generation via PDFKit, Excel workbook synthesis via ExcelJS, and CSV parsing via json2csv.")
    add_numbered_p(doc, "7", "Responsive & Cross-Device Compatibility", "To ensure seamless usability across heterogeneous screen viewports, spanning ultra-wide desktop monitors to compact mobile smartphones, using modern CSS Flexbox and Grid layouts.")

    add_section_heading(doc, "1.6", "Scope of the Project")
    add_body_p(
        doc,
        "The architectural and functional scope of ExpenseX is clearly demarcated into existing operational capabilities "
        "and explicit project boundaries:"
    )
    add_body_p(
        doc,
        "In-Scope Functional Boundaries:"
    )
    add_bullet_p(doc, "User Authentication & Lifecycle", "User registration, credential login, secure logout, local session storage, JWT token verification, user profile fetching, profile name/email updating, and cryptographically verified password modification.")
    add_bullet_p(doc, "Financial Dashboard", "Real-time computation and display of Net Balance, Total Income, Total Expenses, Total Transaction Counts, and an immediate feed of recent transactions.")
    add_bullet_p(doc, "Transaction Ledger", "Creation of income and expense transactions with mandatory validation (amount >= 1, non-empty category, payment method selector), full pagination controls, real-time client-side search, and category filtering.")
    add_bullet_p(doc, "Graphical Visualizations", "Categorical expense distribution rendered via interactive Pie Charts with transaction drill-down, and longitudinal monthly expense trends rendered via Cartesian line graphs.")
    add_bullet_p(doc, "AI Financial Insights", "Automated computation of transaction summaries, dynamic generation of prompt context, execution of Gemini 2.5 Flash API calls, markdown stripping, JSON parsing, and dynamic rendering of Financial Health Scores, Spending Analyses, Smart Alerts, and Personalized Advice.")
    add_bullet_p(doc, "Export Facilities", "Direct streaming of complete or date-filtered transactions into formatted PDF reports, Excel workbooks (.xlsx), CSV files, and structured JSON files.")
    add_body_p(
        doc,
        "Explicit Out-of-Scope Boundaries (Targeted for Future Iterations):"
    )
    add_bullet_p(doc, "Direct Banking Gateway Integration", "ExpenseX does not directly execute ACH, NEFT, RTGS, or UPI money transfers between external bank accounts; it serves as a management and tracking system.")
    add_bullet_p(doc, "Automated Bank SMS Ingestion", "Due to web browser security sandboxing, automated ingestion of local device SMS text messages is deferred to the future native mobile application.")
    add_bullet_p(doc, "Legal Financial Advice", "The AI insight module provides educational, analytical, and informational summaries; it does not replace certified chartered accountants or licensed wealth managers.")

    add_section_heading(doc, "1.7", "Need for the System")
    add_body_p(
        doc,
        "In the contemporary post-pandemic digital economy, consumer transaction patterns have radically shifted toward "
        "frictionless cashless modalities, including Unified Payments Interface (UPI), contactless credit cards, and digital wallets. "
        "While digital transactions maximize consumer convenience, they simultaneously decouple the psychological pain of paying "
        "from the act of purchasing. Consequently, individuals frequently experience 'invisible spending leakage'—a phenomenon where "
        "numerous minor micropayments accumulate into severe budgetary shortfalls by month's end."
    )
    add_body_p(
        doc,
        "College students, young software professionals, and middle-income families require an agile tool that demands minimal data entry "
        "overhead while providing maximum analytical clarity. ExpenseX directly fulfills this pressing socioeconomic need by centralizing "
        "all monetary vectors into one cohesive dashboard, highlighting expenditure hot-spots, and deploying cutting-edge generative "
        "AI to instill disciplined financial habits."
    )

    add_section_heading(doc, "1.8", "Problem Definition and Formal Statement")
    add_callout_box(
        doc,
        "Formal Software Engineering Problem Statement",
        "\"To design, implement, test, and deploy a responsive, cloud-native personal financial management system (ExpenseX) "
        "that eliminates the errors of manual bookkeeping, protects user data sovereignty, visualizes cash-flow dynamics through "
        "interactive charts, generates deterministic multi-format audit reports, and synthesizes aggregated financial summaries "
        "into actionable behavioural insights through structured integration with the Google Gemini Artificial Intelligence API.\""
    )

    add_section_heading(doc, "1.9", "Comprehensive Feasibility Study")
    add_body_p(
        doc,
        "Prior to initiating system implementation, an exhaustive multi-dimensional feasibility study was conducted to establish "
        "the viability, resource requirements, and risk profile of the ExpenseX project."
    )
    
    add_subsection_heading(doc, "1.9.1", "Technical Feasibility")
    add_body_p(
        doc,
        "Technical feasibility evaluates whether the required technologies, programming frameworks, and infrastructural components "
        "are mature, compatible, and capable of fulfilling system requirements within current developer competencies:"
    )
    add_bullet_p(doc, "MERN Stack Maturity", "Node.js (v20+) and Express.js (v5) provide an exceptionally fast, non-blocking asynchronous event-driven runtime ideal for concurrent I/O-intensive RESTful microservices. React 19 paired with Vite represents the vanguard of modern frontend web engineering, offering instantaneous Hot Module Replacement (HMR) and optimized build bundling.")
    add_bullet_p(doc, "Database Scalability", "MongoDB Atlas provides a managed, cloud-hosted document database with automatic sharding, automated secondary indexing, and robust Mongoose ODM integration, natively handling JSON-structured financial data.")
    add_bullet_p(doc, "Artificial Intelligence Integration", "The Google Gemini 2.5 Flash model accessible via the official @google/genai SDK offers ultra-low latency inference, high contextual understanding, and strict adherence to structured JSON output schemas, making real-time insight generation technically sound.")
    add_bullet_p(doc, "Conclusion on Technical Feasibility", "All software libraries, build tools, database drivers, and cloud APIs are widely adopted, exhaustively documented, and completely compatible, confirming 100% technical feasibility.")

    add_subsection_heading(doc, "1.9.2", "Economic and Financial Feasibility")
    add_body_p(
        doc,
        "Economic feasibility assesses the development and operational expenditure required to build and maintain the application "
        "relative to the value delivered:"
    )
    add_bullet_p(doc, "Zero Software Licensing Costs", "The entirety of the ExpenseX technology stack—comprising React, Vite, Node.js, Express, MongoDB, Mongoose, Recharts, PDFKit, and ExcelJS—is licensed under liberal open-source licenses (MIT, Apache 2.0, ISC), incurring zero software acquisition fees.")
    add_bullet_p(doc, "Cloud Free-Tier Infrastructure", "The system leverages generous free-tier cloud allocations: Vercel for Edge frontend hosting, Render for backend container hosting, MongoDB Atlas M0 Sandbox for database storage, and Google AI Studio free tier for Gemini API calls.")
    add_bullet_p(doc, "Development Hardware Utilization", "Development was executed entirely on existing commodity personal computers, requiring zero capital outlay for specialized hardware or server equipment.")
    add_bullet_p(doc, "Conclusion on Economic Feasibility", "The project exhibits virtually zero financial barrier to entry, establishing absolute economic viability.")

    add_subsection_heading(doc, "1.9.3", "Operational Feasibility")
    add_body_p(
        doc,
        "Operational feasibility evaluates how effectively the system integrates into the daily routines of end users and whether "
        "specialized technical training is required for adoption:"
    )
    add_bullet_p(doc, "Intuitive User Experience", "The user interface adheres to contemporary human-computer interaction (HCI) standards, featuring intuitive navigation sidebars, recognizable icons, clear modal dialogs, and instant visual feedback via React-Toastify notifications.")
    add_bullet_p(doc, "Zero Client Configuration", "Users require no technical training or software installation; navigating to the application URL in any standard web browser allows instant onboarding.")
    add_bullet_p(doc, "Dual-Mode Accessibility", "The inclusion of Guest Demo mode enables prospective users to immediately explore the system's full interactive features before registering an account, drastically accelerating operational adoption.")
    add_bullet_p(doc, "Conclusion on Operational Feasibility", "ExpenseX is highly accessible, user-centric, and operationally viable across diverse user demographics.")

    add_subsection_heading(doc, "1.9.4", "Schedule and Milestone Feasibility")
    add_body_p(
        doc,
        "Schedule feasibility determines whether the project scope can be realistically designed, implemented, tested, and "
        "documented within the prescribed academic timeline (16 weeks / 1 semester). Through disciplined Agile Scrum methodology "
        "and bi-weekly sprints, all milestones were executed on schedule, confirming total schedule feasibility."
    )

    add_section_heading(doc, "1.10", "Project Stakeholder Identification")
    add_body_p(
        doc,
        "Stakeholders in the ExpenseX ecosystem are classified into three primary operational tiers:"
    )
    add_bullet_p(doc, "Primary Stakeholders", "End users (college students, freelancers, salaried professionals, and household budget managers) who interact daily with the dashboard, log transactions, examine charts, read AI insights, and download audit reports.")
    add_bullet_p(doc, "Secondary Stakeholders", "Academic evaluators, project guides, software engineering professors, and technical reviewers who evaluate the project's architectural integrity, algorithmic rigor, code quality, and compliance with university documentation standards.")
    add_bullet_p(doc, "Tertiary Stakeholders", "Cloud infrastructure providers (Vercel, Render, MongoDB Atlas, Google Cloud Platform) hosting the physical compute, network, and AI inference pipelines.")

    add_section_heading(doc, "1.11", "Hardware and Software Requirements")
    add_body_p(
        doc,
        "The development and execution environment specifications for ExpenseX are documented in Table 1.1 and Table 1.2:"
    )

    # Table 1.1
    t1_headers = ["Parameter", "Development Environment Specification", "Client / End-User Specification"]
    t1_data = [
        ["Processor (CPU)", "Intel Core i5 / AMD Ryzen 5 (2.5 GHz or higher)", "Dual-core 1.6 GHz or ARM Mobile Processor"],
        ["System Memory (RAM)", "8 GB DDR4 (16 GB Recommended)", "2 GB RAM (Mobile) / 4 GB RAM (Desktop)"],
        ["Storage Space", "256 GB SSD (Minimum 10 GB Free Disk)", "50 MB Cache / LocalStorage allocation"],
        ["Network Interface", "Broadband Internet (10 Mbps+ for Cloud Sync)", "3G / 4G / 5G Mobile Data or Wi-Fi Connection"],
        ["Display Resolution", "1920 x 1080 Full HD Monitor", "360 x 640 (Mobile) to 1920 x 1080 (Desktop)"],
        ["Input Peripherals", "Standard QWERTY Keyboard, Precision Mouse", "Touchscreen, Trackpad, or Standard Peripherals"]
    ]
    add_styled_table(doc, "Table 1.1", "Hardware Environment Specifications for Development & Client Devices", t1_headers, t1_data, [1.5, 2.5, 2.25])

    # Table 1.2
    t2_headers = ["Software Category", "Technology / Tool Name", "Version / Edition", "Role in Project Architecture"]
    t2_data = [
        ["Operating System", "Microsoft Windows 11 / Linux Ubuntu", "64-bit OS", "Host OS for development and build tooling"],
        ["Runtime Environment", "Node.js (LTS)", "v20.x or v22.x", "Asynchronous JavaScript server-side execution runtime"],
        ["Package Manager", "Node Package Manager (npm)", "v10.x", "Dependency resolution and build script runner"],
        ["Frontend Library", "React.js", "v19.2.7", "Declarative UI component rendering and Virtual DOM reconciliation"],
        ["Build Bundler", "Vite", "v8.1.0", "Next-generation frontend dev server and Rollup production bundler"],
        ["Backend Framework", "Express.js", "v5.2.1", "Routing, HTTP middleware pipeline, and REST API controller gateway"],
        ["Database Management", "MongoDB Atlas Cloud", "v8.0 Engine", "Cloud-hosted NoSQL distributed document store"],
        ["Object Data Modeling", "Mongoose ODM", "v8.19.1", "Schema definition, type casting, validation, and query API"],
        ["Artificial Intelligence", "Google Gemini API (@google/genai)", "v2.10.0 / Model 2.5 Flash", "Generative AI financial health diagnosis and smart alerts"],
        ["Data Visualization", "Recharts", "v3.9.2", "Composable charting primitives for React (Pie & Line charts)"],
        ["Authentication / Crypto", "JSON Web Token / Bcrypt", "jsonwebtoken v9 / bcrypt v6", "Stateless bearer token authorization and salted hashing"],
        ["Document Generation", "PDFKit / ExcelJS / json2csv", "v0.19 / v4.4 / v6.0", "Streaming PDF, Excel workbook, and CSV file synthesis"],
        ["Integrated Dev Env", "Visual Studio Code", "v1.98+", "Source code editing, debugging, and terminal execution"],
        ["API Testing Tool", "Postman / VS Code REST Client", "v11.x / v0.25", "HTTP endpoint functional validation and payload testing"],
        ["Version Control", "Git & GitHub Cloud", "v2.44+ / GitHub", "Distributed revision tracking and remote repository hosting"]
    ]
    add_styled_table(doc, "Table 1.2", "Software Environment and Development Toolchain Specifications", t2_headers, t2_data, [1.2, 1.8, 1.0, 2.25])

    add_section_heading(doc, "1.12", "Project Planning, SDLC Model and Gantt Chart")
    add_body_p(
        doc,
        "ExpenseX was engineered in strict accordance with the Agile Scrum methodology, characterized by incremental sprint cycles, "
        "continuous integration, and frequent feedback loops. Table 1.3 outlines the project execution schedule, contrasting planned "
        "timelines with actual completed dates across the development lifecycle."
    )

    # Table 1.3
    t3_headers = ["Phase ID", "SDLC Project Phase", "Planned Start", "Planned End", "Executed Start", "Executed End", "Status"]
    t3_data = [
        ["P-01", "Project Inception & Proposal", "15-06-2024", "30-06-2024", "18-06-2024", "28-06-2024", "Completed"],
        ["P-02", "Literature Survey & Fact Finding", "01-07-2024", "15-07-2024", "02-07-2024", "14-07-2024", "Completed"],
        ["P-03", "Requirements Analysis & SRS", "16-07-2024", "31-07-2024", "15-07-2024", "30-07-2024", "Completed"],
        ["P-04", "System Architecture & UML Design", "01-08-2024", "20-08-2024", "01-08-2024", "18-08-2024", "Completed"],
        ["P-05", "Database Modeling & Mongoose Schemas", "21-08-2024", "31-08-2024", "20-08-2024", "30-08-2024", "Completed"],
        ["P-06", "Backend REST API Development", "01-09-2024", "20-09-2024", "01-09-2024", "22-09-2024", "Completed"],
        ["P-07", "Google Gemini AI Integration", "21-09-2024", "30-09-2024", "22-09-2024", "02-10-2024", "Completed"],
        ["P-08", "Frontend UI & Component Development", "01-10-2024", "22-10-2024", "03-10-2024", "24-10-2024", "Completed"],
        ["P-09", "Recharts Analytics & Visualizations", "23-10-2024", "31-10-2024", "25-10-2024", "02-11-2024", "Completed"],
        ["P-10", "Multi-Format Export Engine (PDF/Excel)", "01-11-2024", "10-11-2024", "03-11-2024", "11-11-2024", "Completed"],
        ["P-11", "System Integration & Security Hardening", "11-11-2024", "20-11-2024", "12-11-2024", "21-11-2024", "Completed"],
        ["P-12", "Comprehensive Quality Assurance & Testing", "21-11-2024", "05-12-2024", "22-11-2024", "06-12-2024", "Completed"],
        ["P-13", "Cloud Deployment (Vercel & Render)", "06-12-2024", "15-12-2024", "07-12-2024", "14-12-2024", "Completed"],
        ["P-14", "Documentation & Black Book Preparation", "16-12-2024", "31-12-2024", "15-12-2024", "30-12-2024", "Completed"]
    ]
    add_styled_table(doc, "Table 1.3", "Project Schedule, Sprint Breakdown, and Planned vs Executed Dates", t3_headers, t3_data, [0.7, 2.1, 0.75, 0.75, 0.75, 0.75, 0.7])

    # Figure 1.1 Placeholder
    fig1_exp = [
        "Figure 1.1 illustrates the chronological Gantt chart representing the 16-week project execution timeline for ExpenseX. "
        "The project is structured across five major sequential streams: Requirements Engineering, System Design, Backend & AI Engineering, "
        "Frontend & Data Visualization, and Quality Assurance & Deployment.",
        "Crucially, the chart highlights the concurrency achieved between Backend REST API creation and Frontend Component wireframing "
        "during Weeks 7 through 10, enabled by contract-first API design and mock JSON responses. The critical path spanned the "
        "integration of the Google Gemini AI prompt pipeline and the multi-format PDF/Excel streaming controllers, both of which "
        "underwent rigorous testing before final cloud deployment on Vercel and Render."
    ]
    add_figure_box(doc, "Figure 1.1", "Project Schedule and Milestone Gantt Chart", fig1_exp)

    doc.add_page_break()

    # =========================================================================
    # CHAPTER 2 — SYSTEM ANALYSIS AND REQUIREMENTS
    # =========================================================================
    add_chapter_heading(doc, "CHAPTER 2", "SYSTEM ANALYSIS AND REQUIREMENTS")
    
    add_section_heading(doc, "2.1", "Fact Finding Techniques")
    add_body_p(
        doc,
        "Requirements engineering for ExpenseX employed a rigorous, multi-pronged fact-finding methodology combining quantitative surveys, "
        "interactive rapid prototyping, and market literature analysis to accurately model stakeholder needs."
    )

    add_subsection_heading(doc, "2.1.1", "Questionnaires and Surveys")
    add_body_p(
        doc,
        "A structured digital survey comprising 12 quantitative and qualitative questions was administered to a targeted cohort of "
        "120 respondents, including university students (45%), early-career software professionals (35%), and self-employed freelancers (20%). "
        "Key questions explored digital payment frequency, satisfaction with existing mobile banking apps, desired visualization tools, "
        "and willingness to trust AI-generated financial coaching."
    )
    add_body_p(
        doc,
        "Key empirical findings from the survey revealed:"
    )
    add_bullet_p(doc, "UPI Dominance", "88% of respondents conduct 5 or more digital micropayments daily, leading to rapid loss of expenditure awareness.")
    add_bullet_p(doc, "Dissatisfaction with Manual Tracking", "74% had attempted manual spreadsheet or notebook tracking but abandoned it within 3 weeks due to cognitive fatigue.")
    add_bullet_p(doc, "Demand for Instant Export", "81% requested direct PDF and Excel export capabilities for academic expense reimbursement and tax records.")
    add_bullet_p(doc, "Receptivity to AI Insights", "79% expressed strong interest in automated AI diagnostics that could detect spending anomalies without requiring accounting expertise.")

    add_subsection_heading(doc, "2.1.2", "Prototyping and Iterative Wireframing")
    add_body_p(
        doc,
        "An evolutionary prototyping model was adopted to refine the user experience. Low-fidelity Figma wireframes were initially "
        "evaluated by a focus group to test navigational ergonomics. User feedback led to key architectural adjustments: eliminating multi-step "
        "checkout-style modals in favor of a single-screen transaction modal, integrating real-time category spending badges, and introducing "
        "a zero-authentication Guest Mode to facilitate friction-free evaluation."
    )

    add_subsection_heading(doc, "2.1.3", "Market and Literature Study")
    add_body_p(
        doc,
        "A technical audit of prevailing commercial applications (Mint, Splitwise, Spendee, Walnut) was conducted. The audit established "
        "that existing solutions frequently lock advanced chart filtering and multi-format exports behind monthly subscriptions ($4.99–$9.99/mo), "
        "rely heavily on battery-draining background SMS scrapers, and lack generative AI capability to generate synthesized natural language "
        "financial summaries. This market gap firmly substantiated the unique positioning of ExpenseX."
    )

    add_section_heading(doc, "2.2", "Stakeholder Profiles and Persona Analysis")
    add_body_p(
        doc,
        "System requirements were derived from three archetypal user personas:"
    )
    add_bullet_p(doc, "Persona A: The University Student (Rohan, 21)", "Needs a rapid way to record daily food, transit, and stationery expenses with zero setup; requires visual category charts to stay within a monthly parental allowance.")
    add_bullet_p(doc, "Persona B: The Freelance Developer (Pooja, 26)", "Needs to track diverse income streams across client projects alongside recurring business expenses; requires monthly PDF and Excel statement generation for quarterly tax filing.")
    add_bullet_p(doc, "Persona C: The Young Professional (Amit, 28)", "Needs intelligent analysis of discretionary lifestyle spending (dining out, entertainment, shopping) and actionable AI recommendations to optimize monthly savings ratios.")

    add_section_heading(doc, "2.3", "User Requirements")
    add_body_p(
        doc,
        "Synthesizing stakeholder input yielded the following foundational user requirements:"
    )
    add_bullet_p(doc, "UR-01", "The system shall permit rapid registration and login with instantaneous dashboard redirection.")
    add_bullet_p(doc, "UR-02", "The system shall display current financial status (Balance, Income, Expenses) prominently upon login.")
    add_bullet_p(doc, "UR-03", "The system shall allow transactions to be added with minimal inputs (amount, category, type, payment method).")
    add_bullet_p(doc, "UR-04", "The system shall offer instant search and filtering across transaction history without full page reloads.")
    add_bullet_p(doc, "UR-05", "The system shall present interactive visual charts summarizing expenditures by category and chronological month.")
    add_bullet_p(doc, "UR-06", "The system shall provide an automated, on-demand AI financial evaluation delivering objective health scores.")
    add_bullet_p(doc, "UR-07", "The system shall allow complete ledger records to be downloaded in PDF, Excel, CSV, and JSON formats.")
    add_bullet_p(doc, "UR-08", "The system shall allow users to modify their personal profiles and cryptographically update passwords securely.")

    add_section_heading(doc, "2.4", "Functional Requirements Matrix")
    add_body_p(
        doc,
        "The complete functional requirements specification (FRS) for ExpenseX is detailed in Table 2.1, documenting input parameters, "
        "processing rules, outputs, and priority levels for each module:"
    )

    # Table 2.1
    t4_headers = ["Req ID", "Requirement Name", "Description & Scope", "Priority", "Input Parameters", "Internal Processing Logic", "Expected Output"]
    t4_data = [
        ["FR-01", "User Registration", "Onboard new user accounts into MongoDB", "High", "name, email, password", "Validate fields, verify uniqueness, hash password via bcrypt(10), create User doc", "HTTP 201 + JWT Token + User object"],
        ["FR-02", "User Login", "Authenticate returning users and issue token", "High", "email, password", "Query user by email, compare password hash via bcrypt.compare(), issue JWT token", "HTTP 200 + Bearer JWT Token"],
        ["FR-03", "Guest Demo Mode", "Allow zero-barrier app exploration", "Medium", "None (button trigger)", "Initialize demoUser and demoTransactions in localStorage without calling backend", "Instant dashboard access with mock data"],
        ["FR-04", "Dashboard Metrics", "Compute live balance and summary totals", "High", "JWT Bearer Token", "Fetch all user transactions, aggregate totalIncome, totalExpense, calculate balance", "HTTP 200 + Dashboard summary object"],
        ["FR-05", "Create Transaction", "Persist new monetary cash flow record", "High", "type, amount, category, paymentMethod, desc, date", "Verify token, validate amount >= 1, validate enums, save Transaction document", "HTTP 201 + Created Transaction doc"],
        ["FR-06", "Paginated Retrieval", "Fetch transactions with pagination", "High", "page, limit, JWT Token", "Extract user ID from token, calculate skip=(page-1)*limit, sort {date: -1}, count total", "HTTP 200 + Transactions array + pages"],
        ["FR-07", "Update Transaction", "Modify an existing transaction record", "Medium", "id, type, amount, category, paymentMethod, date", "Verify user ownership (_id & user), apply updated fields, call save()", "HTTP 200 + Updated Transaction doc"],
        ["FR-08", "Delete Transaction", "Remove a transaction from the database", "Medium", "id, JWT Token", "Verify ownership (_id & user), invoke deleteOne(), cascade metrics", "HTTP 200 + Success confirmation message"],
        ["FR-09", "Category Analytics", "Aggregate expenses grouped by category", "High", "JWT Bearer Token", "Query user expenses, aggregate sum per category, format key-value pairs", "HTTP 200 + categoryData JSON object"],
        ["FR-10", "Monthly Analytics", "Aggregate longitudinal monthly expenses", "High", "JWT Bearer Token", "Query user expenses, extract month string, aggregate amounts, sort calendar order", "HTTP 200 + monthlyExpense array"],
        ["FR-11", "AI Insights Engine", "Generate AI financial health analysis", "High", "JWT Bearer Token", "Compute summary, build prompt, call Gemini 2.5 Flash, strip markdown, parse JSON", "HTTP 200 + Structured AI insights JSON"],
        ["FR-12", "PDF Export Engine", "Stream downloadable PDF audit report", "High", "JWT Token, optional date range", "Fetch transactions, calculate net totals, render PDFKit document stream with table layout", "HTTP 200 + application/pdf stream"],
        ["FR-13", "Excel Export Engine", "Generate styled spreadsheet report", "High", "JWT Token, optional date range", "Query transactions, populate ExcelJS workbook, format headers, stream .xlsx file", "HTTP 200 + application/vnd.ms-excel"],
        ["FR-14", "CSV & JSON Export", "Generate standard flat data exports", "Medium", "JWT Token", "Use json2csv parser for CSV; serialize raw JSON array with ISO dates", "HTTP 200 + text/csv or application/json"],
        ["FR-15", "Profile & Password", "Update profile details & change password", "Medium", "name, email, currentPassword, newPassword", "Verify current password via bcrypt, hash new password, persist updated User doc", "HTTP 200 + Profile updated confirmation"]
    ]
    add_styled_table(doc, "Table 2.1", "Comprehensive Functional Requirements Matrix (FR-01 to FR-15)", t4_headers, t4_data, [0.6, 1.1, 1.2, 0.6, 0.9, 1.0, 0.85])

    add_section_heading(doc, "2.5", "Non-Functional Requirements Specification")
    add_body_p(
        doc,
        "Non-functional requirements (NFRs) define the operational quality, security benchmarks, performance criteria, and system "
        "constraints governing ExpenseX, as summarized in Table 2.2:"
    )

    # Table 2.2
    t5_headers = ["NFR ID", "Quality Attribute", "Specification Criterion", "Target Benchmark / Implementation Metric"]
    t5_data = [
        ["NFR-01", "Performance & Latency", "API response time for standard CRUD operations", "Average response time < 150 ms under normal network conditions"],
        ["NFR-02", "Throughput & Scalability", "Capacity to handle concurrent API requests", "Stateless Express middleware handles 500+ concurrent requests/sec"],
        ["NFR-03", "Data Security", "Protection of authentication credentials at rest", "Passwords hashed via bcrypt with salt rounds = 10; never stored in plaintext"],
        ["NFR-04", "Session Authorization", "Stateless token-based authorization mechanism", "HMAC-SHA256 signed JWT tokens with 7-day validity duration"],
        ["NFR-05", "User Isolation", "Cross-tenant data privacy and ownership control", "All database read/write queries strictly scoped to req.user._id"],
        ["NFR-06", "Availability & Uptime", "Platform accessibility across production clouds", "Targeting 99.9% uptime leveraging Render and Vercel SLA guarantees"],
        ["NFR-07", "Usability & Responsiveness", "Seamless rendering across diverse viewport sizes", "Mobile-first responsive design supporting viewports from 320px to 4K"],
        ["NFR-08", "AI Parsing Resilience", "Resilience against malformed LLM responses", "Automated regex stripping of markdown fences + structured JSON fallback"],
        ["NFR-09", "Maintainability & Clean Code", "Modularity of frontend and backend codebases", "Decoupled MVC architecture with separation of routes, controllers, and services"],
        ["NFR-10", "Data Portability", "User ability to extract full financial records", "Zero vendor lock-in with 1-click export to PDF, Excel, CSV, and JSON"]
    ]
    add_styled_table(doc, "Table 2.2", "Non-Functional Software Quality Requirements Specification", t5_headers, t5_data, [0.75, 1.4, 2.1, 2.0])

    add_section_heading(doc, "2.6", "Hardware and Software Specifications")
    add_body_p(
        doc,
        "System specifications require that client devices run any standard ECMAScript 2020-compliant modern web browser "
        "(Google Chrome 90+, Mozilla Firefox 88+, Apple Safari 14+, Microsoft Edge 90+) with JavaScript and LocalStorage enabled. "
        "On the hosting infrastructure side, Node.js v20.x runtime with minimum 512 MB RAM executes the backend service, while MongoDB "
        "Atlas M0 cluster provisions cloud document storage with TLS 1.3 transport encryption."
    )

    add_section_heading(doc, "2.7", "User Roles and Access Levels")
    add_body_p(
        doc,
        "ExpenseX defines clear operational roles and privilege boundaries, documented in Table 2.3:"
    )

    # Table 2.3
    t6_headers = ["User Role", "Authentication Requirement", "Storage Target", "Permitted System Actions & Capabilities", "Restrictions"]
    t6_data = [
        ["Guest / Demo User", "None (instant trial trigger)", "Client Browser LocalStorage", "Explore mock dashboard, add/edit/delete simulated transactions, view sample charts, test UI", "Data is lost upon clearing browser cache; no AI cloud API calls; no cloud sync"],
        ["Registered User", "Email + Password (JWT Token)", "MongoDB Atlas Cloud Cluster", "Full persistent CRUD, real-time analytics, AI Gemini insight generation, PDF/Excel/CSV exports, profile settings", "Can only access personal records; strictly isolated from other users' financial data"],
        ["System Backend", "API Key / JWT Verification", "Server RAM / MongoDB", "Authorize requests, execute Mongoose queries, construct AI prompts, generate file streams", "Stateless execution; no persistent session memory outside database"]
    ]
    add_styled_table(doc, "Table 2.3", "User Roles, Permissions, and Access Privilege Matrix", t6_headers, t6_data, [1.1, 1.2, 1.2, 1.75, 1.0])

    add_section_heading(doc, "2.8", "System Constraints and Business Rules")
    add_body_p(
        doc,
        "The operation of ExpenseX is governed by strict domain-specific business rules enforced at both client and server layers:"
    )
    add_bullet_p(doc, "BR-01 (Monetary Positivity)", "Transaction amount must be a positive numerical value greater than or equal to 1. Negative amounts are rejected; cash flow direction is strictly defined by the 'type' attribute (income vs expense).")
    add_bullet_p(doc, "BR-02 (Category Integrity)", "Every transaction must possess a non-empty, trimmed category identifier (e.g., Food, Travel, Rent, Utilities, Salary).")
    add_bullet_p(doc, "BR-03 (Payment Method Whitelist)", "Payment method must strictly match one of the predefined system enums: Cash, UPI, Debit Card, Credit Card, Bank Transfer, Net Banking, or Wallet.")
    add_bullet_p(doc, "BR-04 (Email Uniqueness)", "User registration requires a syntactically valid, unique email address. Duplicate registration attempts return an explicit 'Already Registered' message.")
    add_bullet_p(doc, "BR-05 (Password Verification)", "Password modification requires explicit verification of the user's existing password before the new password hash is committed to the database.")

    add_section_heading(doc, "2.9", "Assumptions and Technical Dependencies")
    add_body_p(
        doc,
        "System functionality is designed under the following realistic technical assumptions:"
    )
    add_bullet_p(doc, "Network Availability", "The client device maintains an active internet connection to communicate with the Express REST API and MongoDB Atlas cloud.")
    add_bullet_p(doc, "Third-Party API Uptime", "The Google Gemini AI service maintains standard cloud availability; in the event of upstream rate limits or outages, the ExpenseX AI service gracefully catches exceptions and serves an informative fallback message.")
    add_bullet_p(doc, "Browser Storage Quota", "The user's web browser permits standard HTML5 LocalStorage operations (typically 5 MB allocation) for caching the active JWT authentication token and Guest Mode dataset.")

    add_section_heading(doc, "2.10", "Use Case Analysis and Modeling")
    add_body_p(
        doc,
        "Use case analysis captures the interaction dynamics between human actors and the ExpenseX software boundary. "
        "The primary actors comprise the Registered User, the Guest User, the Express Backend API, and the Google Gemini AI Engine."
    )
    
    add_subsection_heading(doc, "2.10.1", "Detailed Use Case Descriptions")
    add_bullet_p(doc, "UC-01: User Authentication", "Actor logs in using email and password. System validates credentials via bcrypt. On success, system signs a JWT token and returns it to the client, which caches it in LocalStorage and routes to /dashboard.")
    add_bullet_p(doc, "UC-02: Manage Transactions", "Actor adds, views, edits, or deletes an expense or income entry. System validates fields, executes Mongoose CRUD operation scoped to req.user._id, and returns updated JSON state with toast notifications.")
    add_bullet_p(doc, "UC-03: View Analytics & Charts", "Actor navigates to /analytics. System requests aggregated categorical and monthly expense endpoints. Recharts dynamically renders responsive Pie and Line charts with interactive hover tooltips and drill-down lists.")
    add_bullet_p(doc, "UC-04: Generate AI Financial Insights", "Actor opens /ai and clicks 'Refresh'. Express backend fetches user transactions, aggregates metrics, builds a prompt, queries Gemini 2.5 Flash, parses structured JSON, and displays diagnostic health cards.")
    add_bullet_p(doc, "UC-05: Export Financial Statements", "Actor selects a report format (PDF, Excel, CSV, JSON) and optional date range. Backend streams generated binary file directly to browser with appropriate Content-Disposition headers for instantaneous file download.")

    # Figure 2.1 Use Case Diagram
    fig2_exp = [
        "Figure 2.1 illustrates the comprehensive Use Case Diagram for the ExpenseX platform. The diagram delineates the system "
        "boundary, identifying the Registered User and Guest User as primary human actors, while the Google Gemini API and "
        "MongoDB Atlas Cloud act as secondary system actors.",
        "Core use cases include Authenticate (Login/Register), View Dashboard, Manage Transactions (Add, Edit, Delete, Filter, Search), "
        "Analyze Visual Charts (Category Pie Chart, Monthly Trend Line), Generate AI Financial Insights, Export Reports (PDF, Excel, "
        "CSV, JSON), and Manage User Profile. Dashed lines illustrate <<include>> relationships, such as Manage Transactions including "
        "Verify Token, and <<extend>> relationships, such as Filter Transactions extending View Transactions."
    ]
    add_figure_box(doc, "Figure 2.1", "ExpenseX System-Wide Use Case Diagram", fig2_exp)

    add_section_heading(doc, "2.11", "Dynamic Activity Diagrams")
    add_body_p(
        doc,
        "Activity diagrams model the sequential logic and conditional decision branches governing key system workflows."
    )

    # Figure 2.2 Activity Diagram A
    fig22_exp = [
        "Figure 2.2 depicts the User Authentication & Dashboard Access Activity Diagram. The workflow begins at the Landing Page. "
        "If the user selects Guest Mode, mock state is initialized in LocalStorage and the user immediately enters the Dashboard.",
        "If the user chooses Login or Register, credentials are submitted via HTTP POST. The backend checks email existence and compares "
        "the bcrypt hash. If credentials are invalid, an error toast is rendered and the form is preserved. If valid, a JWT token is "
        "issued, stored in client LocalStorage, and the user is redirected to the dynamic Dashboard."
    ]
    add_figure_box(doc, "Figure 2.2", "Activity Diagram — User Authentication & Dashboard Access", fig22_exp)

    # Figure 2.3 Activity Diagram B
    fig23_exp = [
        "Figure 2.3 presents the Transaction Processing and Visual Chart Rendering Activity Diagram. The user fills the Add Transaction form. "
        "The client validates that amount >= 1 and all mandatory fields are present before dispatching an authenticated POST request to /api/transactions.",
        "The Express backend validates the payload, extracts req.user._id from the verified JWT token, and writes the document to MongoDB. "
        "Upon successful return, the client updates the local state array, triggers a success toast, and dynamically recalculates the "
        "summary balance cards and Recharts analytical graphs without requiring a full page refresh."
    ]
    add_figure_box(doc, "Figure 2.3", "Activity Diagram — Transaction Processing & Visual Rendering", fig23_exp)

    # Figure 2.4 Activity Diagram C
    fig24_exp = [
        "Figure 2.4 portrays the AI Financial Insights Synthesis Activity Diagram. When the user navigates to the AI Insights tab, "
        "the client dispatches a GET request to /api/ai/insights. The backend aggregates all transactions belonging to the user, computing "
        "total income, total expenses, balance, and category-wise spending totals.",
        "These metrics are injected into a structured engineering prompt that mandates strict JSON output. The backend calls the Gemini 2.5 Flash "
        "endpoint. Upon response arrival, markdown code fences are stripped via regular expressions and the string is parsed into a JavaScript object. "
        "If parsing succeeds, the structured JSON is returned to the client and rendered into interactive financial health cards; if an exception occurs, "
        "a graceful fallback object is returned."
    ]
    add_figure_box(doc, "Figure 2.4", "Activity Diagram — AI Financial Insights Pipeline", fig24_exp)

    doc.add_page_break()

    # =========================================================================
    # CHAPTER 3 — EXISTING SYSTEM AND PROPOSED SYSTEM
    # =========================================================================
    add_chapter_heading(doc, "CHAPTER 3", "EXISTING SYSTEM AND PROPOSED SYSTEM")
    
    add_section_heading(doc, "3.1", "Detailed Investigation of Existing Systems")
    add_body_p(
        doc,
        "To establish a solid scientific foundation for ExpenseX, an exhaustive investigation was conducted into the three dominant "
        "paradigms of personal expense tracking currently employed across consumer domains:"
    )
    add_bullet_p(doc, "1. Manual Paper Ledgers and Physical Notebooks", "The oldest accounting methodology, characterized by physical journal entries organized in debit/credit columns. While entirely private and zero-cost, it requires arduous physical recordkeeping, cannot scale, offers zero backup against fire, water, or physical loss, and requires tedious manual arithmetic.")
    add_bullet_p(doc, "2. Electronic Desktop Spreadsheets (Excel / Google Sheets)", "A popular computerized alternative where users set up grid columns for date, category, and amount. While computational math errors are mitigated through sum formulas, spreadsheets remain passive files that lack automated cross-device syncing, responsive mobile views, or intelligent guidance.")
    add_bullet_p(doc, "3. Commercial Native Mobile Applications", "Modern app-store budgeting apps (Mint, Splitwise, Spendee, Money Manager). While visually polished, these apps suffer from aggressive monetization models, intrusive third-party ads, paid paywalls for basic features like CSV/PDF exports, and privacy-invasive tracking of banking credentials.")

    add_section_heading(doc, "3.2", "Problems in Existing Accounting and Tracking Approaches")
    add_body_p(
        doc,
        "Systemic analysis reveals critical bottlenecks across these existing paradigms:"
    )
    add_numbered_p(doc, "1", "High Friction and User Abandonment", "Manual logging requires repetitive typing without intelligent category auto-completion, causing over 70% of users to abandon budgeting within the first month.")
    add_numbered_p(doc, "2", "Data Insecurity and Cloud Lock-In", "Commercial tools frequently trap user data within proprietary database formats, making it exceedingly difficult or expensive to export complete transaction histories if the user chooses to switch platforms.")
    add_numbered_p(doc, "3", "Absence of Behavioral Context", "Existing tools merely display historical tallies. They do not evaluate whether a 40% expenditure on dining out is perilous relative to the user's income or calculate a personalized financial health score.")
    add_numbered_p(doc, "4", "Rigid Infrastructure Overhead", "Traditional enterprise accounting software requires local runtime installations, database setup, and heavy hardware resources, rendering them impractical for everyday personal tracking.")

    add_section_heading(doc, "3.3", "Limitations Matrix of Existing Systems")
    add_body_p(
        doc,
        "The technical and functional limitations of existing systems are summarized below:"
    )
    add_bullet_p(doc, "Computational Incapacity", "Paper ledgers possess zero capacity for automatic summation, category aggregation, or statistical deviation analysis.")
    add_bullet_p(doc, "Formula Brittleness", "Spreadsheet workbooks frequently break when rows are inserted or deleted, disrupting underlying formula ranges (e.g., #REF! or #VALUE! errors).")
    add_bullet_p(doc, "Intrusive Monetization", "Free commercial apps monetize consumer attention through disruptive banner advertisements, video popups, and financial product upsells.")
    add_bullet_p(doc, "Lack of AI Reasoning", "No prevailing traditional tool integrates generative large language models to interpret spending habits and offer dynamic, conversational financial advice.")

    add_section_heading(doc, "3.4", "Proposed ExpenseX Architectural Solution")
    add_body_p(
        doc,
        "ExpenseX eliminates these limitations by introducing a unified, open-source, full-stack web application designed "
        "with modern software engineering best practices. Built on the MERN stack (React 19, Node.js, Express 5, MongoDB Atlas), "
        "ExpenseX delivers a single, cohesive platform that provides:"
    )
    add_bullet_p(doc, "Full Platform Independence", "Runs seamlessly in any modern web browser across Windows, macOS, Linux, Android, and iOS without requiring app store installation.")
    add_bullet_p(doc, "Stateless Cloud Synchronization", "Transactions saved to MongoDB Atlas are instantly reflected across all logged-in devices via RESTful API calls governed by JWT tokens.")
    add_bullet_p(doc, "Zero-Friction Guest Mode", "Empowers prospective users to evaluate all platform features instantly using browser LocalStorage simulation without requiring immediate credential registration.")
    add_bullet_p(doc, "Automated AI Analysis", "Translates raw numbers into natural-language diagnostic advice, financial scores, and alerts via the Google Gemini 2.5 Flash API.")
    add_bullet_p(doc, "Universal Data Portability", "Guarantees complete data sovereignty by enabling one-click streaming exports of ledgers into PDF, Excel, CSV, and JSON formats.")

    add_section_heading(doc, "3.5", "Proposed System Workflow and Operational Life Cycle")
    add_body_p(
        doc,
        "The end-to-end operational life cycle of ExpenseX follows a streamlined five-stage workflow:"
    )
    add_numbered_p(doc, "Stage 1", "Onboarding & Session Creation", "The user accesses the landing page, reviews platform capabilities, and authenticates via Login, Registration, or Guest Mode. The backend validates credentials and issues a stateless JWT token.")
    add_numbered_p(doc, "Stage 2", "Transaction Capture & Ledger Maintenance", "The user records cash flows via the Add Transaction modal. Express validates data types and business constraints, persisting records to MongoDB Atlas.")
    add_numbered_p(doc, "Stage 3", "Metric Aggregation & Visual Rendering", "The frontend queries /api/dashboard and /api/analytics, computing Net Balance and populating dynamic Recharts Pie and Line components.")
    add_numbered_p(doc, "Stage 4", "Intelligent AI Diagnosis", "The user navigates to /ai. The backend aggregates categorical distributions, builds an engineered prompt, invokes the Gemini 2.5 Flash model, and delivers a structured JSON financial health card.")
    add_numbered_p(doc, "Stage 5", "Audit Reporting & Export", "The user filters transactions by date range and downloads an official financial statement formatted in PDF, Excel (.xlsx), CSV, or JSON.")

    add_section_heading(doc, "3.6", "Major Features and Module Highlights")
    add_bullet_p(doc, "Security & Auth Module", "Salted bcrypt password hashing, JWT token signing, authorization middleware, protected SPA route guards, profile updates, and secure password modification.")
    add_bullet_p(doc, "Dashboard Module", "Visual overview featuring Net Balance, Total Income, Total Expenses, Total Transaction Count cards, and a live Recent Transactions feed.")
    add_bullet_p(doc, "Transaction CRUD Module", "Full lifecycle management of monetary entries with type toggle, category picker, payment method selector, date picker, search bar, category filter, and pagination.")
    add_bullet_p(doc, "Interactive Analytics Module", "Recharts-powered Expense Category Pie Chart with interactive drill-down transaction lists, and Monthly Expense Line Chart showing longitudinal trends.")
    add_bullet_p(doc, "AI Financial Insights Module", "Integration with Google Gemini 2.5 Flash, providing Financial Health Scores (0-100), Spending Analyses, Savings Recommendations, Smart Alerts, and Next Month Goals.")
    add_bullet_p(doc, "Multi-Format Export Module", "High-performance server-side document streaming for PDF (PDFKit), Excel (ExcelJS), CSV (json2csv), and JSON formats.")

    add_section_heading(doc, "3.7", "Functional Advantages of ExpenseX")
    add_body_p(
        doc,
        "ExpenseX offers definitive functional advantages over legacy and commercial alternatives:"
    )
    add_bullet_p(doc, "Efficiency & Speed", "Instantaneous UI updates using React 19 virtual DOM reconciliation and lightweight JSON REST APIs.")
    add_bullet_p(doc, "Transparency & Privacy", "Zero third-party trackers, zero advertising banners, and complete data isolation.")
    add_bullet_p(doc, "Actionable Intelligence", "Transforms passive transaction tables into proactive behavioral coaching via generative AI.")
    add_bullet_p(doc, "Zero Operational Cost", "Completely open-source, eliminating recurring user subscription fees.")

    add_section_heading(doc, "3.8", "Technical Comparison Between Existing Systems and ExpenseX")
    add_body_p(
        doc,
        "Table 3.1 provides an exhaustive feature-by-feature comparative analysis contrasting traditional paper logs, electronic spreadsheets, "
        "commercial mobile apps, and the ExpenseX platform:"
    )

    # Table 3.1
    t7_headers = ["Evaluation Criterion", "Paper Ledgers", "Desktop Spreadsheets", "Commercial Mobile Apps", "ExpenseX Platform"]
    t7_data = [
        ["Data Entry Speed", "Slow (Manual pen/paper)", "Moderate (Keyboard typing)", "Fast (Touchscreen forms)", "Fast (Intuitive modal + validation)"],
        ["Mathematical Accuracy", "Low (Human calculation error)", "High (Formula-driven)", "High (Automated backend)", "High (Mongoose + Server validation)"],
        ["Cross-Device Portability", "None (Physical bound book)", "Low (Requires local file sync)", "Moderate (Mobile OS locked)", "Universal (Browser-accessible SPA)"],
        ["Automated Visual Analytics", "None (Manual graphing required)", "Manual (User designs charts)", "Pre-set (Often paywalled)", "Dynamic (Recharts Pie & Line charts)"],
        ["AI Behavioral Coaching", "None", "None", "None or static rule-based", "Advanced (Google Gemini 2.5 Flash)"],
        ["Data Export Formats", "None", "Native XLSX / CSV only", "Limited / Paid subscription", "Full (PDF, Excel, CSV, JSON free)"],
        ["User Privacy & Security", "High (Physical) / Low (No pass)", "Variable (Local password)", "Low (Ad tracking / Data sales)", "High (Stateless JWT + Bcrypt + Zero Ads)"],
        ["Zero-Barrier Trial Mode", "N/A", "N/A", "Rare (Requires email/phone signup)", "Yes (Full Guest Mode simulation)"],
        ["Recurring Licensing Cost", "Minimal (Paper cost)", "Office 365 Subscription fee", "Freemium ($4.99–$9.99/month)", "100% Free & Open Source (MIT)"]
    ]
    add_styled_table(doc, "Table 3.1", "Comparative Analysis Matrix: Existing Systems vs ExpenseX Platform", t7_headers, t7_data, [1.3, 1.1, 1.3, 1.25, 1.3])

    add_section_heading(doc, "3.9", "Scope of Improvement and Long-Term Value")
    add_body_p(
        doc,
        "While ExpenseX successfully resolves the core limitations of existing financial tools, the system is architected with "
        "high extensibility to support future enhancements, including cross-platform mobile apps (React Native), category-specific "
        "budget caps with threshold alerts, recurring subscription schedules, and multi-currency foreign exchange support."
    )

    doc.add_page_break()
