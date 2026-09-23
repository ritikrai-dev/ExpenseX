import docx
from docx.shared import Inches, Pt, RGBColor
from build_report.styles import (
    FONT_NAME, COLOR_PRIMARY, COLOR_TEXT, COLOR_MUTED,
    add_chapter_heading, add_section_heading, add_subsection_heading,
    add_subsubsection_heading, add_body_p, add_bullet_p, add_numbered_p,
    add_styled_table, add_figure_box, add_callout_box
)

def build_chapters_4_to_5(doc):
    # =========================================================================
    # CHAPTER 4 — SYSTEM DESIGN
    # =========================================================================
    add_chapter_heading(doc, "CHAPTER 4", "SYSTEM DESIGN")
    
    add_section_heading(doc, "4.1", "System Architecture Overview")
    add_body_p(
        doc,
        "System design represents the critical phase in software engineering where abstract functional requirements and "
        "user expectations are transformed into a concrete, robust technical blueprint. For ExpenseX, the overarching design "
        "philosophy centers upon modularity, low coupling, high cohesion, stateless scalability, and strict separation of concerns (SoC). "
        "The system adheres to modern web engineering patterns, decoupling the client presentation layer from server-side business logic "
        "and database persistence."
    )

    add_section_heading(doc, "4.2", "High-Level Three-Tier Architecture")
    add_body_p(
        doc,
        "ExpenseX is structured as an enterprise-grade three-tier distributed web architecture, comprising:"
    )
    add_bullet_p(doc, "1. Presentation Layer (Frontend Client)", "Built with React 19 and bundled via Vite, this layer executes within the end-user's web browser. It manages application routing, component hierarchy, UI state, user input capture, form validation, dynamic Recharts rendering, and asynchronous HTTP communication via fetch and Axios APIs.")
    add_bullet_p(doc, "2. Application & Business Logic Layer (RESTful API Server)", "Implemented using Node.js and Express.js 5, this middle tier acts as the central orchestrator. It receives HTTP requests, enforces Cross-Origin Resource Sharing (CORS) rules, executes JWT token verification middleware, processes business logic across domain controllers, streams generated PDF/Excel documents, and interfaces with the Google Gemini AI inference endpoint.")
    add_bullet_p(doc, "3. Data & Cognitive Intelligence Layer (Persistence & AI Services)", "Comprises MongoDB Atlas, a managed cloud NoSQL database storing user profiles and transaction documents, and Google Cloud's Gemini AI service, which provides large language model cognitive intelligence for financial health scoring.")

    # Figure 4.1 System Architecture
    fig41_exp = [
        "Figure 4.1 illustrates the high-level three-tier system architecture of the ExpenseX platform. At the top tier, the end-user "
        "interacts with the React 19 Single Page Application delivered via Vercel's global Content Delivery Network (CDN). "
        "The client maintains local session state and communicates asynchronously with the backend server via JSON RESTful API calls.",
        "At the middle tier, the Express.js server hosted on Render Cloud intercepts incoming requests. It routes traffic through custom "
        "authentication middleware, validating HMAC-SHA256 signed JSON Web Tokens. Authorized requests are routed to specific controllers: "
        "authControllers, userController, transactionController, dashboardController, analyticsController, aiController, and reportController.",
        "At the bottom tier, the backend communicates with MongoDB Atlas via Mongoose ODM over an encrypted TLS connection. For AI analytics, "
        "the aiService formats aggregated financial statistics and dispatches an authenticated API request to Google's Gemini 2.5 Flash model, "
        "parsing the returned JSON payload before delivering actionable insights back to the client."
    ]
    add_figure_box(doc, "Figure 4.1", "ExpenseX High-Level Three-Tier Architecture Diagram", fig41_exp)

    add_section_heading(doc, "4.3", "Frontend Client Architecture (React 19 & Vite)")
    add_body_p(
        doc,
        "The frontend client is engineered as a responsive Single Page Application (SPA) leveraging the latest React 19 library. "
        "The architecture is characterized by:"
    )
    add_bullet_p(doc, "Component-Driven Design", "The UI is constructed from reusable, self-contained functional components categorized into presentation cards (SummaryCards, AIInsightCard), interactive forms (TransactionForm, PasswordInput), visualizers (ExpenseCategoryChart, MonthlyExpenseChart), layout wrappers (DashboardLayout, Sidebar, Navbar), and full-page views (Dashboard, Transactions, Analytics, AIInsights, Reports, Settings, Landing).")
    add_bullet_p(doc, "Declarative Client Routing", "React Router v7 governs client-side page transitions without incurring full browser page reloads. A custom <Auth> higher-order wrapper inspects localStorage tokens, protecting private routes (/dashboard, /transactions, /analytics, /ai, /reports, /settings) and redirecting unauthenticated visitors to /auth.")
    add_bullet_p(doc, "Next-Generation Bundling via Vite", "Vite 8 utilizes native ES modules (ESM) during development to achieve sub-second server startup and instant Hot Module Replacement (HMR). In production, Vite leverages Rollup to produce highly minified, tree-shaken JavaScript and CSS bundles.")
    add_bullet_p(doc, "Reactive Data Layer & Dual Execution Mode", "The client implements an abstracted data service layer (dataService.js) that inspects application state. When operating in Guest Mode, calls are redirected to demoService.js which simulates responses using browser LocalStorage; in authenticated mode, calls route to apiService.js, dispatching live authenticated HTTP requests to the backend.")

    add_section_heading(doc, "4.4", "Backend Server Architecture (Node.js & Express 5)")
    add_body_p(
        doc,
        "The backend server is architected on Node.js utilizing the Express.js 5 framework. Express organizes functionality into an "
        "asynchronous middleware pipeline. Key architectural highlights include:"
    )
    add_bullet_p(doc, "DNS Resolver Optimization", "To prevent DNS lookup latency and SRV resolution failures common in distributed cloud environments, server.js explicitly configures Google and Cloudflare public DNS resolvers (8.8.8.8, 1.1.1.1) via node:dns.")
    add_bullet_p(doc, "Strict CORS Filtering", "A dynamic Cross-Origin Resource Sharing middleware inspects the Origin header of incoming requests against an explicit whitelist comprising local development URLs (http://localhost:5173) and the production frontend URL (FRONTEND_URL), rejecting unauthorized cross-site requests.")
    add_bullet_p(doc, "Modular Route Separation", "Endpoints are partitioned into discrete domain routers (/api/auth, /api/users, /api/transactions, /api/dashboard, /api/analytics, /api/reports, /api/ai), each delegating to dedicated controller modules.")

    add_section_heading(doc, "4.5", "Database and Storage Architecture (MongoDB Atlas)")
    add_body_p(
        doc,
        "Data persistence is managed through MongoDB Atlas, a managed cloud NoSQL document store. MongoDB's BSON (Binary JSON) storage "
        "paradigm maps natively to JavaScript object representations in Node.js and React, eliminating object-relational impedance mismatch. "
        "Mongoose 8 provides schema-level validation, type casting, middleware hooks, and query compilation, ensuring enterprise-grade data integrity."
    )

    add_section_heading(doc, "4.6", "RESTful API Architectural Design")
    add_body_p(
        doc,
        "ExpenseX adheres strictly to REST (Representational State Transfer) architectural principles:"
    )
    add_bullet_p(doc, "Stateless Communication", "Every request contains all context necessary for execution; the server retains no client session state in memory.")
    add_bullet_p(doc, "Resource-Oriented URI Schema", "Endpoints represent nouns identifying core domain resources (/api/transactions, /api/users/profile, /api/dashboard).")
    add_bullet_p(doc, "Standard HTTP Verbs", "Operations map directly to standard HTTP methods: GET (retrieve resource), POST (create resource), PUT (update resource), and DELETE (remove resource).")
    add_bullet_p(doc, "Semantic HTTP Status Codes", "Responses convey operational outcomes via standard RFC codes: 200 OK, 201 Created, 400 Bad Request, 401 Unauthorized, 404 Not Found, and 500 Internal Server Error.")

    add_section_heading(doc, "4.7", "Authentication and Authorization Architecture (JWT)")
    add_body_p(
        doc,
        "Authentication is architected upon the cryptographic JSON Web Token standard (RFC 7519). Upon successful user registration or login, "
        "the backend signs a compact, URL-safe token containing the user's MongoDB ObjectId (decoded.id), issued at timestamp (iat), "
        "and expiration timestamp (exp set to 7 days). The token is signed using the HMAC-SHA256 algorithm with a cryptographically secure "
        "server-side secret (JWT_SECRET)."
    )
    add_body_p(
        doc,
        "Subsequent client requests include this token in the HTTP Authorization header using the standard Bearer scheme: "
        "'Authorization: Bearer <token>'. The protect middleware intercepts each request, verifies token integrity and expiration, "
        "queries MongoDB to ensure user existence (excluding password hash via .select('-password')), and attaches the active user "
        "document to req.user. This guarantees that all downstream controllers operate strictly within the authenticated user's isolated data sandbox."
    )

    add_section_heading(doc, "4.8", "Data Flow Diagrams (DFD)")
    add_body_p(
        doc,
        "Data Flow Diagrams visualize the algorithmic pathways through which data enters, transforms, and exits the ExpenseX software boundary."
    )

    # Figure 4.2 DFD Level 0
    fig42_exp = [
        "Figure 4.2 portrays the Context-Level Data Flow Diagram (Level 0 DFD) for ExpenseX. The central bubble represents the unified "
        "ExpenseX Software Boundary. The primary external entities comprise the End User (Client Browser), MongoDB Atlas Cloud Database, "
        "and Google Gemini AI Engine.",
        "The User supplies registration credentials, login requests, transaction parameters, date filter criteria, and profile updates. "
        "The ExpenseX system responds with JWT tokens, dashboard summaries, real-time analytics graphs, streamed PDF/Excel audit reports, "
        "and structured AI financial recommendations. The system exchanges BSON document queries and mutation commands with MongoDB, "
        "and dispatches structured prompt payloads to Gemini AI, receiving raw inferential text responses."
    ]
    add_figure_box(doc, "Figure 4.2", "Data Flow Diagram — Context Level (Level 0 DFD)", fig42_exp)

    # Figure 4.3 DFD Level 1
    fig43_exp = [
        "Figure 4.3 details the Level 1 Data Flow Diagram, decomposing the monolithic system boundary into six discrete functional subsystems: "
        "1.0 Authentication & Session Manager, 2.0 User Profile Controller, 3.0 Transaction Lifecycle Engine, 4.0 Dashboard & Analytics Aggregator, "
        "5.0 AI Financial Insights Processor, and 6.0 Multi-Format Document Exporter.",
        "The diagram illustrates the flow of JWT tokens from Process 1.0 into downstream processes 2.0 through 6.0 as an authorization guard. "
        "Processes 2.0, 3.0, 4.0, 5.0, and 6.0 interact directly with two core data stores: D1 (Users Collection) and D2 (Transactions Collection). "
        "Process 5.0 dispatches aggregated financial metrics to external entity E2 (Google Gemini API), transforming the response into structured "
        "JSON cards for user consumption."
    ]
    add_figure_box(doc, "Figure 4.3", "Data Flow Diagram — Subsystem Decomposition (Level 1 DFD)", fig43_exp)

    # Figure 4.4 DFD Level 2
    fig44_exp = [
        "Figure 4.4 presents the detailed Level 2 Data Flow Diagram focusing on the Transaction Management Subsystem (3.0) and AI Processor (5.0). "
        "Process 3.0 is partitioned into 3.1 Input Validation (verifying amount >= 1 and valid enums), 3.2 User Association (injecting req.user._id), "
        "3.3 Database Mutation (Mongoose save/update/deleteOne), and 3.4 Paginated Query Engine (skip/limit computation and date sorting).",
        "Process 5.0 is decomposed into 5.1 Aggregation Pipeline (summing income, expense, and category totals), 5.2 Context Prompt Synthesis "
        "(injecting totals into JSON prompt template), 5.3 Model Invocation (@google/genai SDK execution), and 5.4 JSON Sanitization (regex stripping "
        "of markdown fences and JSON.parse validation)."
    ]
    add_figure_box(doc, "Figure 4.4", "Data Flow Diagram — Detailed Transaction & AI Engine (Level 2 DFD)", fig44_exp)

    add_section_heading(doc, "4.9", "Class Diagrams and Domain Model")
    add_body_p(
        doc,
        "The object-oriented design of ExpenseX bridges Mongoose data schemas, Express middleware controllers, and frontend service abstractions."
    )

    # Figure 4.5 Class Diagram
    fig45_exp = [
        "Figure 4.5 illustrates the Unified Domain Class Diagram for ExpenseX, detailing the attributes, methods, visibility modifiers, "
        "and structural associations across the application layers.",
        "Core entity classes include User (_id: ObjectId, name: String, email: String, password: String, timestamps) and Transaction "
        "(_id: ObjectId, user: ObjectId, type: String, amount: Number, category: String, paymentMethod: String, description: String, "
        "date: Date). A 1-to-Many association links User to Transaction via foreign key referencing.",
        "Controller classes (AuthController, UserController, TransactionController, DashboardController, AnalyticsController, AIController, "
        "ReportController) encapsulate static business methods. The protect middleware enforces dependency injection of User into Express "
        "Request objects, while AIService encapsulates communication with GoogleGenAI client instances."
    ]
    add_figure_box(doc, "Figure 4.5", "Unified Domain Class Diagram (Models, Controllers, Services)", fig45_exp)

    add_section_heading(doc, "4.10", "Component Diagram")
    add_body_p(
        doc,
        "The component architecture defines the physical software modules that constitute ExpenseX and their interconnecting interfaces."
    )

    # Figure 4.6 Component Diagram
    fig46_exp = [
        "Figure 4.6 presents the Component Diagram of ExpenseX, highlighting the decoupled relationship between Client-Side Components "
        "and Server-Side Services.",
        "The Frontend component package comprises Routing (App.jsx, Auth.jsx), Page Views (Dashboard, Transactions, Analytics, AIInsights, Reports, "
        "Settings), UI Components (TransactionTable, TransactionForm, SummaryCards, AIInsightCard, Charts), and Data Services (apiService, demoService).",
        "The Backend component package encompasses Middleware (authMiddleware, CORS), Routing Modules (authRoutes, transactionRoutes, etc.), "
        "Controllers, Utilities (generateToken, promptBuilder, generatePDF, generateExcel, generateCSV), Mongoose Models, and the External "
        "Gemini AI SDK Adapter."
    ]
    add_figure_box(doc, "Figure 4.6", "Component Diagram of Frontend and Backend Subsystems", fig46_exp)

    add_section_heading(doc, "4.11", "Package and Module Dependency Diagram")
    add_body_p(
        doc,
        "The package architecture illustrates how code artifacts are structured into directories and physical npm packages, ensuring "
        "unidirectional dependency flows and zero circular references."
    )

    # Figure 4.7 Package Diagram
    fig47_exp = [
        "Figure 4.7 displays the Package and Module Dependency Diagram for ExpenseX. The monorepo structure cleanly bifurcates into "
        "/client and /server root packages.",
        "The /server package depends on external npm modules (express, mongoose, jsonwebtoken, bcrypt, @google/genai, pdfkit, exceljs, "
        "json2csv, dotenv, cors). Internally, dependencies flow strictly downward: Routes depend on Controllers and Middleware; Controllers "
        "depend on Models, Services, and Utilities; Models depend exclusively on Mongoose.",
        "The /client package depends on react, react-dom, react-router-dom, recharts, react-toastify, and lucide/tabler icons. "
        "Pages depend on Components and Data Services; Data Services depend on native fetch/localStorage."
    ]
    add_figure_box(doc, "Figure 4.7", "Package and Module Dependency Diagram", fig47_exp)

    add_section_heading(doc, "4.12", "Interaction Sequence Diagrams")
    add_body_p(
        doc,
        "Sequence diagrams model the chronological exchange of HTTP messages, database invocations, and asynchronous events across system entities."
    )

    # Figure 4.8 Sequence Diagram Auth
    fig48_exp = [
        "Figure 4.8 details the User Registration and Login Sequence Diagram. The User submits email and password from the AuthPage form. "
        "The client dispatches an HTTP POST request to /api/auth/login. The Express router passes execution to authControllers.login().",
        "The controller queries User.findOne({email}) in MongoDB. If found, bcrypt.compare() cryptographically evaluates the password against "
        "the stored hash. Upon validation, generateToken() signs a JWT token using JWT_SECRET. The server responds with HTTP 200, returning the "
        "token and user profile. The client caches the token in localStorage and triggers React Router navigation to /dashboard."
    ]
    add_figure_box(doc, "Figure 4.8", "Sequence Diagram — User Registration and Login Flow", fig48_exp)

    # Figure 4.9 Sequence Diagram Transaction
    fig49_exp = [
        "Figure 4.9 illustrates the Transaction CRUD Lifecycle Sequence Diagram. The user submits a new entry via the TransactionForm modal. "
        "The client issues a POST /api/transactions request with Authorization: Bearer <token>.",
        "The protect middleware verifies token validity, resolves req.user._id, and invokes transactionController.addTransaction(). "
        "The controller executes Transaction.create(), committing the document to MongoDB Atlas. A 201 Created response is returned with the "
        "created record. The client prepends the new transaction to local state, closes the modal, triggers a React-Toastify alert, "
        "and re-renders the dynamic Recharts graphs."
    ]
    add_figure_box(doc, "Figure 4.9", "Sequence Diagram — Transaction CRUD Lifecycle Flow", fig49_exp)

    # Figure 4.10 Sequence Diagram AI
    fig410_exp = [
        "Figure 4.10 depicts the AI Financial Insight Generation Sequence Diagram. The user accesses the AI Insights page. The client "
        "invokes GET /api/ai/insights. The protect middleware verifies the bearer token and passes execution to aiController.getInsights().",
        "The controller calls aiService.generateInsights(userId). The service queries all transactions for the user, aggregating total income, "
        "total expenses, net balance, and category-wise spending totals. buildPrompt() formats these statistics into a strict JSON template.",
        "aiService initializes the GoogleGenAI client with GEMINI_API_KEY and calls ai.models.generateContent({model: 'gemini-2.5-flash', contents: prompt}). "
        "Upon receiving the text response, regular expressions strip markdown fences (```json ... ```), and JSON.parse() deserializes the string into "
        "a structured object. The result is returned as HTTP 200 and rendered into responsive financial health cards on the client."
    ]
    add_figure_box(doc, "Figure 4.10", "Sequence Diagram — AI Financial Insight Generation Flow", fig410_exp)

    # Figure 4.11 Sequence Diagram Report
    fig411_exp = [
        "Figure 4.11 details the Multi-Format Report Streaming Sequence Diagram. When a user requests a PDF or Excel statement, the client "
        "calls GET /api/reports/pdf or /api/reports/excel with optional query parameters (fromDate, toDate).",
        "The reportController queries MongoDB via Transaction.find().lean() for maximum memory efficiency. For PDF exports, a new PDFDocument "
        "is initialized and piped directly into the HTTP response stream (doc.pipe(res)). For Excel exports, an ExcelJS Workbook is instantiated, "
        "columns and styling applied, and written via workbook.xlsx.write(res). Appropriate Content-Disposition headers trigger instant browser "
        "file download without buffering the entire document on disk."
    ]
    add_figure_box(doc, "Figure 4.11", "Sequence Diagram — Multi-Format Report Streaming Flow", fig411_exp)

    add_section_heading(doc, "4.13", "Cloud Deployment Diagram")
    add_body_p(
        doc,
        "The deployment topology reflects modern multi-cloud distribution, ensuring optimal performance, edge delivery, and database redundancy."
    )

    # Figure 4.12 Deployment Diagram
    fig412_exp = [
        "Figure 4.12 presents the Cloud Deployment and Physical Infrastructure Diagram for ExpenseX. Client devices connect over HTTPS (port 443) "
        "to Vercel's Global Edge Network, which hosts the pre-rendered static assets (HTML5, CSS3, Vite-bundled JavaScript bundles).",
        "API calls route dynamically to the Express.js application server hosted in a containerized environment on Render Cloud. Render maintains "
        "environment variables (PORT, MONGO_URI, JWT_SECRET, GEMINI_API_KEY) in encrypted vaults.",
        "The backend establishes persistent, encrypted TLS connections to MongoDB Atlas, which provisions an automated 3-node replica set cluster "
        "with primary-secondary failover. Cognitive requests travel over secure HTTPS to Google Cloud's Gemini API endpoints."
    ]
    add_figure_box(doc, "Figure 4.12", "Cloud Deployment and Physical Infrastructure Diagram", fig412_exp)

    add_section_heading(doc, "4.14", "Security and Defense-in-Depth Design")
    add_body_p(
        doc,
        "ExpenseX enforces a multi-layered Defense-in-Depth security architecture:"
    )
    add_bullet_p(doc, "Layer 1: Network & Transport Security", "All production traffic is encrypted in transit via Transport Layer Security (TLS 1.3/HTTPS).")
    add_bullet_p(doc, "Layer 2: Edge & Origin Control", "Strict CORS whitelisting in Express blocks unauthorized cross-domain resource requests.")
    add_bullet_p(doc, "Layer 3: Authentication & Token Validation", "Stateless HMAC-SHA256 JWT tokens with 7-day expiration verify user identity on every protected route.")
    add_bullet_p(doc, "Layer 4: Access Control & Data Isolation", "Every database operation explicitly scopes queries to req.user._id, preventing horizontal privilege escalation.")
    add_bullet_p(doc, "Layer 5: Credential Protection", "Passwords undergo salted one-way hashing with bcrypt (10 rounds) prior to database persistence.")

    add_section_heading(doc, "4.15", "Global Error Handling Strategy")
    add_body_p(
        doc,
        "To ensure high system resilience, all asynchronous controller functions are wrapped in standardized try-catch blocks. "
        "In the event of runtime exceptions, controllers log diagnostic details to server consoles while returning clean, standardized "
        "JSON error payloads ({success: false, message: error.message}) with appropriate HTTP status codes (400, 401, 404, 500). "
        "This prevents server crashes and eliminates the leakage of raw stack traces to the public internet."
    )

    add_section_heading(doc, "4.16", "Client and Server Validation Design")
    add_body_p(
        doc,
        "Validation is enforced symmetrically at both client and server boundaries. The frontend prevents submission of empty or malformed "
        "inputs using HTML5 form attributes and React state checks, displaying immediate feedback via toast messages. Symmetrically, the backend "
        "re-evaluates all payloads against Mongoose schema rules, rejecting negative amounts, illegal payment methods, and invalid dates."
    )

    doc.add_page_break()

    # =========================================================================
    # CHAPTER 5 — DATABASE DESIGN
    # =========================================================================
    add_chapter_heading(doc, "CHAPTER 5", "DATABASE DESIGN")
    
    add_section_heading(doc, "5.1", "Database Introduction and Selection Rationale")
    add_body_p(
        doc,
        "The database architecture forms the persistence bedrock of the ExpenseX platform. Selecting the appropriate database management "
        "system (DBMS) required a careful comparative analysis between traditional Relational Database Management Systems (RDBMS like "
        "PostgreSQL or MySQL) and Document-Oriented NoSQL systems (such as MongoDB)."
    )
    add_body_p(
        doc,
        "MongoDB was selected as the optimal data store for ExpenseX based on compelling architectural justifications:"
    )
    add_bullet_p(doc, "Native JSON/BSON Alignment", "Personal financial transactions inherently represent semi-structured documents. MongoDB natively stores records in BSON (Binary JSON), perfectly mirroring JavaScript objects utilized across React and Node.js.")
    add_bullet_p(doc, "Dynamic Schema Evolution", "As ExpenseX evolves to support future features (e.g., custom user tags, recurring transaction intervals, geo-location coordinates), MongoDB allows schema evolution without demanding destructive SQL table migrations.")
    add_bullet_p(doc, "High-Throughput Aggregation Pipeline", "MongoDB features an exceptionally powerful server-side aggregation framework, enabling high-speed summation, grouping, and statistical date extraction directly on database nodes with minimal server memory overhead.")

    add_section_heading(doc, "5.2", "MongoDB Document-Oriented Architecture")
    add_body_p(
        doc,
        "In MongoDB, data is organized hierarchically into databases, collections, and documents. Unlike flat relational rows, documents "
        "can accommodate diverse data types including nested objects, arrays, timestamps, and 128-bit ObjectIds. Mongoose ODM operates as "
        "the modeling layer, enforcing schema definitions, type casting, default values, and operational middleware."
    )

    add_section_heading(doc, "5.3", "Physical Data Model and Database Cluster Topology")
    add_body_p(
        doc,
        "In the production deployment, ExpenseX connects to a high-availability MongoDB Atlas cluster. Atlas automatically provisions a "
        "three-node replica set architecture (one primary node and two secondary replicas) deployed across cloud availability zones. "
        "Write operations are committed to the primary node and asynchronously replicated to secondaries, guaranteeing high data durability "
        "and instantaneous automatic failover in the event of hardware degradation."
    )

    add_section_heading(doc, "5.4", "Entity Relationship (ER) and Document Reference Model")
    add_body_p(
        doc,
        "The conceptual data model of ExpenseX embodies a classic 1-to-Many (1:N) relationship between the User entity and the Transaction "
        "entity. Rather than embedding unbounded transaction arrays inside user documents—which would risk exceeding MongoDB's 16 MB per-document "
        "limit—the database implements normalized referencing. Each Transaction document maintains an indexed foreign reference to its parent User."
    )

    # Figure 5.1 ER Diagram
    fig51_exp = [
        "Figure 5.1 depicts the Entity-Relationship (ER) Schema Model for ExpenseX. The diagram highlights the 1-to-Many relational link "
        "connecting the Users collection to the Transactions collection.",
        "The User entity contains attributes _id (Primary Key), name, email (Unique Indexed), password, createdAt, and updatedAt. "
        "The Transaction entity contains attributes _id (Primary Key), user (Foreign Key referencing User._id), type (Enum: income/expense), "
        "amount (Number >= 1), category (String), paymentMethod (Enum), description (String), date (Date), createdAt, and updatedAt.",
        "Cardinality notation denotes that one User may possess zero, one, or thousands of Transactions (1 to 0..*), while each Transaction "
        "strictly belongs to exactly one User (mandatory 1:1 reverse binding)."
    ]
    add_figure_box(doc, "Figure 5.1", "Entity-Relationship (ER) Schema Model in MongoDB Atlas", fig51_exp)

    add_section_heading(doc, "5.5", "Detailed Collection Schemas")
    add_body_p(
        doc,
        "The physical data dictionaries for the two core collections in ExpenseX are exhaustively detailed in Table 5.1 and Table 5.2:"
    )

    add_subsection_heading(doc, "5.5.1", "Users Collection Schema Specification")
    # Table 5.1
    t8_headers = ["Field Name", "BSON Data Type", "Key Type", "Required", "Default Value", "Validation & Constraints", "Field Description"]
    t8_data = [
        ["_id", "ObjectId", "Primary Key", "Yes", "Auto-generated", "12-byte unique BSON identifier", "Unique immutable system identifier for user"],
        ["name", "String", "Standard Field", "Yes", "None", "trim: true, non-empty", "Full name of the registered user"],
        ["email", "String", "Unique Key", "Yes", "None", "unique: true, lowercase: true, trim: true", "User login email address used for auth"],
        ["password", "String", "Standard Field", "Yes", "None", "bcrypt hash string (60 chars)", "Cryptographically salted bcrypt password hash"],
        ["createdAt", "Date", "System Audit", "Yes", "Date.now", "timestamps: true", "Timestamp when user document was created"],
        ["updatedAt", "Date", "System Audit", "Yes", "Date.now", "timestamps: true", "Timestamp when user document was last updated"]
    ]
    add_styled_table(doc, "Table 5.1", "Users Collection Schema Data Dictionary and Integrity Constraints", t8_headers, t8_data, [0.9, 1.0, 1.0, 0.7, 0.9, 1.5, 1.5])

    add_subsection_heading(doc, "5.5.2", "Transactions Collection Schema Specification")
    # Table 5.2
    t9_headers = ["Field Name", "BSON Data Type", "Key Type", "Required", "Default Value", "Validation & Constraints", "Field Description"]
    t9_data = [
        ["_id", "ObjectId", "Primary Key", "Yes", "Auto-generated", "12-byte unique BSON identifier", "Unique immutable system identifier for transaction"],
        ["user", "ObjectId", "Foreign Key", "Yes", "None", "ref: 'User', indexed", "References _id of the parent User document"],
        ["type", "String", "Standard Field", "Yes", "None", "enum: ['income', 'expense']", "Specifies the monetary flow direction"],
        ["amount", "Number", "Standard Field", "Yes", "None", "min: 1, positive numeric value", "Numerical monetary amount in currency (INR ₹)"],
        ["category", "String", "Standard Field", "Yes", "None", "trim: true, non-empty string", "Category label (Food, Travel, Rent, Salary, etc.)"],
        ["paymentMethod", "String", "Standard Field", "Yes", "None", "enum: [Cash, UPI, Debit Card, Credit Card, Bank Transfer, Net Banking, Wallet]", "Financial vector used to execute the transaction"],
        ["description", "String", "Standard Field", "No", "Empty string \"\"", "trim: true, maxlength: 200", "Optional contextual memo or note by the user"],
        ["date", "Date", "Standard Field", "No", "Date.now", "Valid ISO 8601 date", "Calendar date associated with the transaction"],
        ["createdAt", "Date", "System Audit", "Yes", "Date.now", "timestamps: true", "Timestamp when record was committed to database"],
        ["updatedAt", "Date", "System Audit", "Yes", "Date.now", "timestamps: true", "Timestamp when record was last modified"]
    ]
    add_styled_table(doc, "Table 5.2", "Transactions Collection Schema Data Dictionary and Validation Rules", t9_headers, t9_data, [0.9, 0.85, 0.85, 0.65, 0.85, 1.6, 1.8])

    add_section_heading(doc, "5.6", "Data Types and BSON Representation")
    add_body_p(
        doc,
        "MongoDB stores records using BSON (Binary JSON), which extends JSON with explicit data types. In ExpenseX, timestamps are preserved "
        "as 64-bit UTC dates, amounts are stored as standard double-precision floating-point numbers, and document links utilize 12-byte "
        "binary ObjectIds consisting of a 4-byte timestamp, 5-byte random value, and 3-byte incrementing counter."
    )

    add_section_heading(doc, "5.7", "Relational Referencing and Foreign Key Integrity")
    add_body_p(
        doc,
        "Referential integrity is maintained programmatically via Mongoose. The user field in transactionSchema defines type: "
        "mongoose.Schema.Types.ObjectId with ref: 'User'. Whenever transactions are created or queried, the backend enforces "
        "req.user._id matching, ensuring orphaned transactions are mathematically impossible."
    )

    add_section_heading(doc, "5.8", "Schema Constraints and Mongoose Built-in Validators")
    add_body_p(
        doc,
        "Mongoose schemas enforce strict domain validation rules directly prior to database commits:"
    )
    add_bullet_p(doc, "Required Validators", "name, email, password in User; user, type, amount, category, paymentMethod in Transaction.")
    add_bullet_p(doc, "String Sanitization", "trim: true automatically removes leading/trailing whitespace; lowercase: true ensures case-insensitive email matching.")
    add_bullet_p(doc, "Numerical Range Limits", "amount enforces min: 1, rejecting negative numbers or zero amounts at the driver level.")
    add_bullet_p(doc, "Enumeration Whitelisting", "type restricts values strictly to ['income', 'expense']; paymentMethod restricts to the 7 permitted payment types.")

    add_section_heading(doc, "5.9", "Database Indexing Strategy and Query Optimization")
    add_body_p(
        doc,
        "Database indexing is critical to sustain sub-millisecond query execution as transaction volumes scale. ExpenseX implements "
        "two vital indexing strategies:"
    )
    add_bullet_p(doc, "Unique Single-Field Index", "A unique secondary B-Tree index is maintained on the email field in the users collection. This enforces email uniqueness at the storage engine level and provides O(log N) lookup latency during user login.")
    add_bullet_p(doc, "Compound Secondary Index", "In the transactions collection, queries predominantly filter by user and sort chronologically by date descending ({date: -1}). A compound index on { user: 1, date: -1 } satisfies both the equality filter and sort ordering simultaneously, eliminating costly in-memory sort operations and enabling instantaneous paginated retrieval.")

    add_section_heading(doc, "5.10", "Data Security, Encryption, and Transport Layer TLS")
    add_body_p(
        doc,
        "MongoDB Atlas enforces robust multi-tier security. All connections between the Express server and Atlas nodes require TLS 1.3 "
        "transport encryption. Database credentials (username, password, cluster URI) are stored exclusively in server environment variables "
        "(MONGO_URI) and never committed to source control. Furthermore, database data at rest is encrypted using FIPS 140-2 validated "
        "AES-256 encryption."
    )

    add_section_heading(doc, "5.11", "Core Database Operations and Aggregation Pipelines")
    add_body_p(
        doc,
        "The system executes high-performance database operations across controllers:"
    )
    add_bullet_p(doc, "Paginated Querying", "Transaction.find({user: req.user._id}).sort({date: -1}).skip(skip).limit(limit) delivers paginated chunks, while countDocuments({user: req.user._id}) computes total pages.")
    add_bullet_p(doc, "Category Expense Grouping", "Iterates user expense documents to build an in-memory frequency and sum dictionary per category, formatted for instant Recharts Pie consumption.")
    add_bullet_p(doc, "Longitudinal Monthly Trends", "Extracts the calendar month from transaction.date, grouping total expenditures into an ordered twelve-month array for LineChart rendering.")
    add_bullet_p(doc, "Lean Streaming Queries", "In reportController, Transaction.find({user: req.user._id}).lean() bypasses Mongoose hydration overhead, returning plain JavaScript objects to maximize memory efficiency during large PDF and Excel export generation.")

    add_section_heading(doc, "5.12", "Data Backup, Sharding, and Disaster Recovery")
    add_body_p(
        doc,
        "MongoDB Atlas provides automated continuous cloud backups with point-in-time recovery (PITR). In the event of catastrophic data loss, "
        "the database cluster can be restored to any second within the retention window. Furthermore, Atlas automatically handles replica "
        "synchronization, ensuring seamless data continuity."
    )

    doc.add_page_break()
