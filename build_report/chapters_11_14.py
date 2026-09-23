import docx
from docx.shared import Inches, Pt, RGBColor
from build_report.styles import (
    FONT_NAME, COLOR_PRIMARY, COLOR_TEXT, COLOR_MUTED,
    add_chapter_heading, add_section_heading, add_subsection_heading,
    add_subsubsection_heading, add_body_p, add_bullet_p, add_numbered_p,
    add_styled_table, add_figure_box, add_callout_box, add_code_block
)

def build_chapters_11_to_14(doc):
    # =========================================================================
    # CHAPTER 11 — DEPLOYMENT AND MAINTENANCE
    # =========================================================================
    add_chapter_heading(doc, "CHAPTER 11", "DEPLOYMENT AND MAINTENANCE")
    
    add_section_heading(doc, "11.1", "Deployment Overview and Cloud Topology")
    add_body_p(
        doc,
        "Deployment transitions a locally developed software codebase into a hardened, highly available, production-grade cloud environment. "
        "ExpenseX adopts a modern multi-cloud serverless and containerized deployment architecture, distributing workloads between Vercel "
        "(frontend edge hosting), Render (backend containerized API runtime), MongoDB Atlas (managed cloud database), and Google Cloud "
        "(generative AI inference)."
    )

    add_section_heading(doc, "11.2", "Frontend Hosting on Vercel Edge Network")
    add_body_p(
        doc,
        "The React 19 Single Page Application is deployed onto Vercel's Global Edge Network. When changes are committed to the GitHub main branch, "
        "Vercel triggers an automated CI/CD pipeline, executing npm install and npm run build. Vite compiles, minifies, and tree-shakes the source "
        "into optimized static HTML, CSS, and JS artifacts."
    )
    add_body_p(
        doc,
        "Because React Router handles routing on the client side, accessing direct URLs (such as /dashboard or /analytics) on a traditional web server "
        "would trigger HTTP 404 Not Found errors. To resolve this, ExpenseX configures vercel.json with an explicit SPA rewrite rule:"
    )
    add_code_block(
        doc,
        """// vercel.json - Client-Side Single Page Application Routing Rule
{
  "rewrites": [
    {
      "source": "/(.*)",
      "destination": "/index.html"
    }
  ]
}""",
        "Listing 11.1: Single-Page Application Rewrite Configuration in vercel.json"
    )

    add_section_heading(doc, "11.3", "Backend Hosting on Render Cloud")
    add_body_p(
        doc,
        "The Node.js and Express 5 backend is deployed as a Web Service on Render Cloud. Render connects to the GitHub repository, installing dependencies "
        "via npm install and booting the server using npm start (node server.js). Render dynamically assigns an external HTTPS port, bound in Express via "
        "process.env.PORT || 5000."
    )

    add_section_heading(doc, "11.4", "Database Provisioning on MongoDB Atlas")
    add_body_p(
        doc,
        "Database hosting is managed via MongoDB Atlas M0 cluster running MongoDB 8.0. Network security is enforced by whitelisting trusted IP addresses, "
        "and an administrative user with readWrite privileges is provisioned. The Mongoose driver connects using connection string pooling with encrypted "
        "TLS/SSL sockets."
    )

    add_section_heading(doc, "11.5", "DNS Configuration and Custom Domain Routing")
    add_body_p(
        doc,
        "As highlighted in Chapter 6, Node's internal DNS resolution on certain cloud environments can encounter timeouts resolving MongoDB SRV records. "
        "server.js explicitly sets nameservers to Google (8.8.8.8) and Cloudflare (1.1.1.1) via dns.setServers(), guaranteeing reliable cloud DNS resolution."
    )

    add_section_heading(doc, "11.6", "Environment Configuration and Secrets Deployment")
    add_body_p(
        doc,
        "Production environment variables are securely injected into hosting dashboards rather than hardcoded in source control:"
    )
    add_bullet_p(doc, "Frontend Variables (Vercel)", "VITE_API_URL pointing to the production Render backend endpoint.")
    add_bullet_p(doc, "Backend Variables (Render)", "PORT, MONGO_URI (MongoDB Atlas SRV string), JWT_SECRET (256-bit cryptographic key), GEMINI_API_KEY (Google Cloud API key), and FRONTEND_URL (for CORS origin validation).")

    add_section_heading(doc, "11.7", "Production Build Optimization and Tree-Shaking")
    add_body_p(
        doc,
        "Vite leverages Rollup under the hood to perform dead-code elimination (tree-shaking), split heavy vendor libraries (such as Recharts, "
        "Axios, and React Icons) into separate asynchronous chunks, and gzip-compress static assets, reducing initial bundle transfer sizes to under 180 KB."
    )

    add_section_heading(doc, "11.8", "System Monitoring, Logging, and Uptime Health")
    add_body_p(
        doc,
        "Runtime operational health is monitored via Render server logs and MongoDB Atlas telemetry charts. Telemetry tracks CPU utilization, "
        "memory consumption, active database connections, and HTTP response status codes. Any 500-level error is logged with diagnostic timestamps."
    )

    add_section_heading(doc, "11.9", "Backup, Replication, and Disaster Recovery")
    add_body_p(
        doc,
        "MongoDB Atlas executes automated daily snapshots with point-in-time recovery. The 3-node replica set provides automatic failover: "
        "if the primary database node becomes unreachable, a secondary node is elected as primary within 3 seconds, ensuring zero data loss."
    )

    add_section_heading(doc, "11.10", "Software Maintenance Lifecycle")
    add_body_p(
        doc,
        "Software maintenance represents the ongoing operational phase following initial deployment, ensuring ExpenseX remains reliable, "
        "secure, and aligned with evolving operating system and web browser standards."
    )

    add_subsection_heading(doc, "11.11", "Corrective Maintenance Operations")
    add_body_p(
        doc,
        "Corrective maintenance rectifies residual bugs reported in production. Activities include handling edge-case JSON syntax variations "
        "from LLM inference, addressing token expiration race conditions during long user sessions, and refining date-range boundary queries."
    )

    add_subsection_heading(doc, "11.12", "Adaptive Maintenance Strategies")
    add_body_p(
        doc,
        "Adaptive maintenance modifies the software to accommodate changes in external dependencies and third-party APIs. Activities include "
        "updating the @google/genai SDK as Google releases newer model iterations, adapting to future Node.js LTS engine requirements, and "
        "updating browser compatibility polyfills."
    )

    add_subsection_heading(doc, "11.13", "Perfective Maintenance Roadmap")
    add_body_p(
        doc,
        "Perfective maintenance enhances existing capabilities based on user feedback. Activities include optimizing database indexing on "
        "transaction collections to sustain sub-10ms query times as transaction volumes exceed 100,000 records, introducing dark-mode UI themes, "
        "and enriching PDF export styling."
    )

    add_subsection_heading(doc, "11.14", "Preventive Maintenance and Security Audits")
    add_body_p(
        doc,
        "Preventive maintenance anticipates and preempts potential future failures. Activities include running automated npm audit scans "
        "to patch vulnerable third-party sub-dependencies, renewing TLS/SSL certificates, refactoring legacy functions, and conducting "
        "periodic code quality reviews."
    )

    doc.add_page_break()

    # =========================================================================
    # CHAPTER 12 — PROJECT MANAGEMENT
    # =========================================================================
    add_chapter_heading(doc, "CHAPTER 12", "PROJECT MANAGEMENT")
    
    add_section_heading(doc, "12.1", "Software Development Life Cycle (SDLC) Methodology")
    add_body_p(
        doc,
        "ExpenseX was executed utilizing the Agile Scrum framework. Given the exploratory nature of generative AI integration and "
        "rapid UI design iterations, traditional Waterfall methodologies were deemed overly rigid. Agile allowed for bi-weekly sprints, "
        "continuous integration, and immediate architectural refinement based on testing feedback."
    )

    add_section_heading(doc, "12.2", "Agile Scrum Iteration Breakdown")
    add_body_p(
        doc,
        "The project was organized across eight two-week sprints:"
    )
    add_bullet_p(doc, "Sprint 1 (Weeks 1-2)", "Project inception, feasibility study, fact-finding surveys, and Software Requirements Specification (SRS).")
    add_bullet_p(doc, "Sprint 2 (Weeks 3-4)", "System architecture design, UML modeling, database schema design, and Figma prototyping.")
    add_bullet_p(doc, "Sprint 3 (Weeks 5-6)", "Backend initialization, Express server setup, MongoDB Atlas integration, and JWT authentication middleware.")
    add_bullet_p(doc, "Sprint 4 (Weeks 7-8)", "Transaction CRUD APIs, paginated querying, and initial frontend React 19 component scaffolding.")
    add_bullet_p(doc, "Sprint 5 (Weeks 9-10)", "Frontend dashboard assembly, transaction modals, table filtering, and Guest Demo mode implementation.")
    add_bullet_p(doc, "Sprint 6 (Weeks 11-12)", "Recharts visual analytics (Pie & Line charts), Google Gemini 2.5 Flash AI integration, and prompt engineering.")
    add_bullet_p(doc, "Sprint 7 (Weeks 13-14)", "Multi-format report export engine (PDFKit, ExcelJS, json2csv), security hardening, and OWASP audit.")
    add_bullet_p(doc, "Sprint 8 (Weeks 15-16)", "Comprehensive unit/integration testing, cloud deployment on Vercel and Render, and Black Book documentation.")

    add_section_heading(doc, "12.3", "Project Schedule and Key Milestones")
    add_body_p(
        doc,
        "All planned milestones—spanning proposal approval, design freeze, core API completion, AI pipeline verification, and production release—were "
        "achieved within the prescribed academic timeline, validating project management discipline."
    )

    add_section_heading(doc, "12.4", "Task Allocation and Responsibilities Matrix")
    add_body_p(
        doc,
        "As an individual capstone project developed by [INSERT STUDENT NAME] (Ritik Rai) under the academic supervision of [INSERT PROJECT GUIDE NAME] "
        "(Dr. Bhakti Chaudhari), responsibilities encompassed the entire full-stack lifecycle: requirements engineering, UI/UX design, database modeling, "
        "backend API engineering, AI prompt design, testing, cloud deployment, and technical writing."
    )

    add_section_heading(doc, "12.5", "Comprehensive Risk Management Plan (Table 12.1)")
    add_body_p(
        doc,
        "Proactive risk management identified potential technical and operational obstacles early, establishing concrete mitigation strategies. "
        "Table 12.1 details the risk management matrix:"
    )

    # Table 12.1 Risk
    t14_headers = ["Risk ID", "Risk Event Description", "Likelihood", "Impact", "Initial Severity", "Proactive Mitigation Strategy Adopted"]
    t14_data = [
        ["RSK-01", "Gemini AI API rate limiting or quota exhaustion", "Medium", "High", "High", "Server-side caching; manual refresh trigger; safe fallback JSON object returned on exception"],
        ["RSK-02", "Malformed LLM response breaking frontend JSON parser", "High", "High", "Critical", "Strict negative prompt constraints; regex markdown fence stripping; try-catch JSON parsing"],
        ["RSK-03", "Cloud DNS timeout when resolving MongoDB SRV records", "Medium", "Critical", "High", "Configured explicit public DNS resolvers (8.8.8.8, 1.1.1.1) in server.js via node:dns"],
        ["RSK-04", "Heavy PDF/Excel exports causing backend memory leaks", "Medium", "Medium", "Medium", "Utilized .lean() Mongoose queries and direct HTTP stream piping (doc.pipe(res))"],
        ["RSK-05", "Cross-tenant data leakage via ID manipulation", "Low", "Critical", "High", "Enforced mandatory user: req.user._id scoping on every database read, update, and delete query"],
        ["RSK-06", "Client-side SPA 404 routing errors on direct URL access", "High", "Medium", "Medium", "Configured vercel.json rewrite rules redirecting all sub-routes to index.html"],
        ["RSK-07", "Project schedule slip due to full-stack scope creep", "Medium", "High", "High", "Disciplined bi-weekly Agile Scrum sprints; deferred complex native features to Future Scope"]
    ]
    add_styled_table(doc, "Table 12.1", "Comprehensive Project Risk Assessment and Mitigation Strategies", t14_headers, t14_data, [0.7, 1.6, 0.8, 0.7, 0.9, 2.05])

    add_section_heading(doc, "12.6", "Resource Planning and Development Budget")
    add_body_p(
        doc,
        "By leveraging open-source frameworks (React, Node, Express, MongoDB) and cloud free tiers (Vercel, Render, Atlas, Google AI Studio), "
        "the total financial development expenditure was maintained at ₹0, demonstrating exemplary resource efficiency."
    )

    add_section_heading(doc, "12.7", "Key Development Challenges Encountered")
    add_bullet_p(doc, "Challenge 1: Stripping Markdown Code Fences from LLM Returns", "Initial calls to Gemini returned JSON enclosed within ```json ... ``` blocks, which caused JSON.parse() to throw severe syntax errors.")
    add_bullet_p(doc, "Challenge 2: Multi-Page Client-Side Routing on Vercel", "Directly loading routes like /analytics on Vercel triggered standard HTTP 404 errors because the web server looked for physical .html files.")
    add_bullet_p(doc, "Challenge 3: High-Memory Overhead in Binary Report Generation", "Generating large PDF statements by buffering complete binary blobs in server RAM risked crashing the Node.js event loop.")
    add_bullet_p(doc, "Challenge 4: Cloud DNS SRV Resolution Failures", "Intermittent timeouts occurred during MongoDB Atlas connection handshakes on containerized hosting environments.")

    add_section_heading(doc, "12.8", "Technical Solutions Adopted")
    add_bullet_p(doc, "Solution to Challenge 1", "Implemented defensive chained regex replacements (.replace(/```json/g, '').replace(/```/g, '').trim()) in aiService.js prior to parsing.")
    add_bullet_p(doc, "Solution to Challenge 2", "Created vercel.json specifying universal rewrite rules to route all subpaths back to index.html.")
    add_bullet_p(doc, "Solution to Challenge 3", "Engineered streaming pipelines using PDFKit's doc.pipe(res) and ExcelJS's workbook.xlsx.write(res), streaming chunks directly to the HTTP response.")
    add_bullet_p(doc, "Solution to Challenge 4", "Configured node:dns with dns.setServers(['8.8.8.8', '1.1.1.1']) in server.js before calling connectDB().")

    doc.add_page_break()

    # =========================================================================
    # CHAPTER 13 — LIMITATIONS AND FUTURE SCOPE
    # =========================================================================
    add_chapter_heading(doc, "CHAPTER 13", "LIMITATIONS AND FUTURE SCOPE")
    
    add_section_heading(doc, "13.1", "Current System Limitations")
    add_body_p(
        doc,
        "While ExpenseX successfully achieves its core software engineering objectives, honest academic evaluation requires "
        "documenting the technical and operational boundaries of the current implementation."
    )

    add_subsection_heading(doc, "13.2", "Technical Architectural Constraints")
    add_bullet_p(doc, "Upstream AI Dependency", "Insight generation relies on the availability of Google Cloud's Gemini API endpoints; severe external network outages temporarily restrict AI features to fallback messages.")
    add_bullet_p(doc, "Single Currency Base", "The current database and UI enforce a single currency baseline (Indian Rupee ₹), lacking dynamic multi-currency conversions.")

    add_subsection_heading(doc, "13.3", "Functional Domain Constraints")
    add_bullet_p(doc, "Absence of Automatic SMS Ingestion", "Due to browser security sandboxing, the web app cannot automatically parse local banking SMS messages, requiring manual form input.")
    add_bullet_p(doc, "Lack of Recurring Subscriptions", "The current system does not automatically create recurring transactions (e.g., monthly Netflix or gym subscriptions) on a scheduled cron basis.")

    add_subsection_heading(doc, "13.4", "Security and Authorization Constraints")
    add_bullet_p(doc, "Client-Side Token Storage", "Tokens are currently stored in browser localStorage. While protected against CSRF, future versions should transition to secure httpOnly cookies.")

    add_subsection_heading(doc, "13.5", "Scalability and Storage Considerations")
    add_body_p(
        doc,
        "Under the free-tier MongoDB Atlas M0 cluster, storage is capped at 512 MB. While sufficient for thousands of transactions, "
        "enterprise scaling will necessitate automated archival or migration to dedicated Atlas M10+ tiers."
    )

    add_section_heading(doc, "13.6", "Future Scope Roadmap (Table 13.1)")
    add_body_p(
        doc,
        "Table 13.1 outlines the phased implementation roadmap planned for subsequent releases of the ExpenseX platform:"
    )

    # Table 13.1 Roadmap
    t15_headers = ["Phase", "Proposed Feature / Enhancement", "Target Release", "Engineering Complexity", "Expected User Benefit"]
    t15_data = [
        ["Phase 2.0", "Cross-Platform Mobile Application", "v2.0.0", "High", "Native Android and iOS mobile app built with React Native / Expo"],
        ["Phase 2.1", "Automated Category Budget Caps & Push Alerts", "v2.1.0", "Medium", "Set monthly spending limits per category with warning notifications"],
        ["Phase 2.2", "Recurring Transactions & Subscription Engine", "v2.2.0", "Medium", "Automated cron-based logging for monthly rent, utilities, and subscriptions"],
        ["Phase 2.3", "Bank Account Aggregator & SMS Parsing", "v2.3.0", "High", "Automated transaction ingestion via Account Aggregator framework & mobile SMS"],
        ["Phase 2.4", "Multi-Currency & Real-Time Forex Support", "v2.4.0", "Medium", "Dynamic currency selector with live exchange rates for international travelers"],
        ["Phase 2.5", "Predictive Financial Time-Series Forecasting", "v2.5.0", "High", "Hybrid ARIMA/LSTM models projecting 60-day balance trajectories"],
        ["Phase 2.6", "Collaborative Shared / Split Expenses", "v2.6.0", "High", "Shared household ledgers and peer-to-peer bill splitting with debt settlement"]
    ]
    add_styled_table(doc, "Table 13.1", "Future Enhancements Roadmap and Phase-Wise Implementation Plan", t15_headers, t15_data, [0.8, 1.8, 0.9, 1.25, 2.0])

    add_subsection_heading(doc, "13.6.1", "Cross-Platform Mobile App (React Native/Expo)")
    add_body_p(
        doc,
        "Porting the React frontend logic to React Native and Expo will allow ExpenseX to distribute native mobile apps on Google Play "
        "and Apple App Store, unlocking device hardware features including biometric fingerprint login and native camera receipt scanning."
    )

    add_subsection_heading(doc, "13.6.2", "Automated Category-Wise Budget Caps & Alerts")
    add_body_p(
        doc,
        "Users will define monthly budget thresholds per category (e.g., ₹8,000 for Food). As spending approaches 80% and 100% of the threshold, "
        "the system will trigger immediate visual alerts and push notifications."
    )

    add_subsection_heading(doc, "13.6.3", "Recurring Transactions & Subscription Tracker")
    add_body_p(
        doc,
        "An automated cron engine on Node.js will execute daily, checking for scheduled recurring transactions and committing them to the ledger "
        "automatically, accompanied by an upcoming renewal calendar."
    )

    add_subsection_heading(doc, "13.6.4", "Bank Account Aggregator & SMS Parsing")
    add_body_p(
        doc,
        "Integration with India's RBI-regulated Account Aggregator (AA) ecosystem will enable encrypted, user-consented direct bank statement "
        "synchronization, eliminating manual entry while preserving data sovereignty."
    )

    add_subsection_heading(doc, "13.6.5", "Multi-Currency & Real-Time Forex Support")
    add_body_p(
        doc,
        "Integrating a live foreign exchange API (e.g., Open Exchange Rates) will allow users to record transactions in USD, EUR, GBP, or AED, "
        "automatically normalizing values into the base INR currency."
    )

    add_subsection_heading(doc, "13.6.6", "Predictive Time-Series Forecasting (ARIMA/LSTM)")
    add_body_p(
        doc,
        "By applying machine learning time-series models on 6+ months of user history, ExpenseX will forecast future month-end account balances "
        "and simulate the financial impact of major prospective expenditures."
    )

    add_subsection_heading(doc, "13.6.7", "Collaborative Split-Expense Management")
    add_body_p(
        doc,
        "Enabling multi-user household groups will allow roommates and families to log shared grocery and utility bills, automatically computing "
        "optimal debt settlement pathways."
    )

    doc.add_page_break()

    # =========================================================================
    # CHAPTER 14 — CONCLUSION
    # =========================================================================
    add_chapter_heading(doc, "CHAPTER 14", "CONCLUSION")
    
    add_section_heading(doc, "14.1", "Summary of Problem Addressed")
    add_body_p(
        doc,
        "In the contemporary digital economy, frictionless cashless payments have created widespread budgetary blindness among students, "
        "freelancers, and households. Traditional tracking methods—such as manual paper ledgers and static spreadsheets—suffer from high human "
        "computational errors, physical fragility, and cognitive fatigue. Concurrently, prevailing commercial applications frequently monetize "
        "user privacy through aggressive advertising and lock essential export features behind monthly subscription paywalls."
    )

    add_section_heading(doc, "14.2", "Summary of System Developed")
    add_body_p(
        doc,
        "To resolve these challenges, ExpenseX — Smart Expense Tracker was engineered and successfully deployed as a robust, full-stack, "
        "cloud-native web application. Built on the MERN stack (React 19, Node.js, Express.js 5, MongoDB Atlas), ExpenseX provides a secure, "
        "centralized platform featuring stateless JWT authentication, salted bcrypt password hashing, dynamic CRUD transaction management, "
        "paginated data retrieval, interactive Recharts visualizations (Pie and Line charts), and an industrial-grade multi-format export engine "
        "generating downloadable PDF, Excel, CSV, and JSON statements."
    )

    add_section_heading(doc, "14.3", "Software Engineering Principles Demonstrated")
    add_body_p(
        doc,
        "The project exemplifies rigorous software engineering methodologies throughout its lifecycle: modular component architecture, "
        "unidirectional dependency flows, strict REST API design, schema-level database validation via Mongoose, Defense-in-Depth security, "
        "defensive prompt engineering with Google Gemini 2.5 Flash, streaming I/O memory optimization, and comprehensive multi-tiered testing."
    )

    add_section_heading(doc, "14.4", "Technical Competencies Acquired")
    add_body_p(
        doc,
        "The conception, implementation, and deployment of ExpenseX provided deep practical competencies in full-stack architecture, "
        "asynchronous JavaScript event loops, NoSQL data modeling, cryptographic security, LLM prompt engineering, cloud edge deployment "
        "on Vercel and Render, and university-standard technical documentation."
    )

    add_section_heading(doc, "14.5", "Concluding Remarks and Final Evaluation")
    add_body_p(
        doc,
        "ExpenseX bridges the critical gap between passive financial recording and active behavioral empowerment. By demonstrating that "
        "modern open-source technologies and generative AI can be harmoniously synthesized into a high-performance, private, and zero-cost "
        "application, ExpenseX stands as a comprehensive, production-ready, and academically exemplary final-year software project."
    )

    doc.add_page_break()
