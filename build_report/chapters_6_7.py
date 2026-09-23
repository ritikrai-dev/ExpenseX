import docx
from docx.shared import Inches, Pt, RGBColor
from build_report.styles import (
    FONT_NAME, COLOR_PRIMARY, COLOR_TEXT, COLOR_MUTED,
    add_chapter_heading, add_section_heading, add_subsection_heading,
    add_subsubsection_heading, add_body_p, add_bullet_p, add_numbered_p,
    add_styled_table, add_figure_box, add_callout_box, add_code_block
)

def build_chapters_6_to_7(doc):
    # =========================================================================
    # CHAPTER 6 — SYSTEM IMPLEMENTATION & CODING
    # =========================================================================
    add_chapter_heading(doc, "CHAPTER 6", "SYSTEM IMPLEMENTATION & CODING")
    
    add_section_heading(doc, "6.1", "Development Environment and Software Toolchain")
    add_body_p(
        doc,
        "System implementation represents the operational realization of the ExpenseX design blueprints into production-grade "
        "executable source code. The project was constructed utilizing a contemporary full-stack JavaScript environment centered on "
        "Node.js v20.x, npm v10.x, React 19, Express 5, and MongoDB Atlas. Development was conducted within Visual Studio Code, "
        "leveraging integrated terminal workflows, ESLint code analysis, and Postman API testing."
    )

    add_section_heading(doc, "6.2", "Project Folder Hierarchy (Full-Stack Monorepo Breakdown)")
    add_body_p(
        doc,
        "ExpenseX is organized as a clean, decoupled monorepo bifurcated into two primary directories: /client (the frontend application) "
        "and /server (the backend REST API microservice). The physical directory structure is detailed below:"
    )

    code_folder_tree = """ExpenseX/
├── client/                     # Frontend Single Page Application (React 19 + Vite)
│   ├── public/                 # Static brand assets (logo1.png, logo.jpg, index.css)
│   ├── src/
│   │   ├── assets/             # Reusable UI widgets (PasswordInput.jsx)
│   │   ├── components/         # Modular presentation & layout components
│   │   │   ├── data/           # Data services (api.js, apiService.js, dataService.js, demoService.js)
│   │   │   ├── landing/        # Marketing portal components (Hero, Features, BarGraph, etc.)
│   │   │   ├── AIInsightCard.jsx
│   │   │   ├── AddTransactionModal.jsx
│   │   │   ├── DashboardHeader.jsx
│   │   │   ├── DashboardLayout.jsx
│   │   │   ├── ExpenseCategoryChart.jsx
│   │   │   ├── MonthlyExpenseChart.jsx
│   │   │   ├── Navbar.jsx
│   │   │   ├── Pagination.jsx
│   │   │   ├── RecentTransactions.jsx
│   │   │   ├── ReportSummary.jsx
│   │   │   ├── SearchBar.jsx
│   │   │   ├── Sidebar.jsx
│   │   │   ├── SummaryCards.jsx
│   │   │   ├── TransactionFilter.jsx
│   │   │   ├── TransactionForm.jsx
│   │   │   └── TransactionTable.jsx
│   │   ├── pages/              # Primary route views (Dashboard, Transactions, AIInsights, etc.)
│   │   ├── style/              # Modular component stylesheets (.css)
│   │   ├── utils/              # Route guards and authentication utilities (Auth.jsx)
│   │   ├── App.jsx             # Top-level client routing configuration
│   │   └── main.jsx            # Application entry point & DOM root mounting
│   ├── package.json            # Frontend dependency specifications
│   ├── vercel.json             # Edge deployment & SPA rewrite routing
│   └── vite.config.js          # Vite build engine configuration
│
├── server/                     # Backend REST API Service (Node.js + Express 5)
│   ├── config/
│   │   └── db.js               # Mongoose MongoDB connection initializer
│   ├── controllers/            # Core business logic controllers
│   │   ├── aiController.js
│   │   ├── analyticsController.js
│   │   ├── authControllers.js
│   │   ├── dashboardController.js
│   │   ├── reportController.js
│   │   ├── transactionController.js
│   │   └── userController.js
│   ├── middleware/
│   │   └── authMiddleware.js   # JWT verification & route protection middleware
│   ├── models/                 # Mongoose data schema definitions
│   │   ├── Transaction.js
│   │   └── User.js
│   ├── routes/                 # Express REST endpoint route declarations
│   ├── services/
│   │   └── aiService.js        # Google Gemini AI inference pipeline
│   ├── utils/                  # Cryptographic, prompt & export generation helpers
│   │   ├── generateCSV.js
│   │   ├── generateExcel.js
│   │   ├── generatePDF.js
│   │   ├── generateToken.js
│   │   └── promptBuilder.js
│   ├── package.json            # Backend dependency specifications
│   └── server.js               # Express application entry point & listener
│
├── requesApi/                  # VS Code REST Client test files (.rest)
└── README.md                   # Architectural overview and installation guide"""
    add_code_block(doc, code_folder_tree, "Listing 6.1: Physical Folder Hierarchy of ExpenseX")

    add_section_heading(doc, "6.3", "Backend Core Implementation")
    
    add_subsection_heading(doc, "6.3.1", "Express Server Initialization & DNS Optimization")
    add_body_p(
        doc,
        "The server entry point (server.js) initializes the Express 5 application and configures low-level networking. "
        "A critical engineering enhancement implemented in ExpenseX is explicit DNS resolver tuning. Cloud serverless platforms "
        "frequently experience lookup failures when resolving MongoDB SRV records. To guarantee uninterrupted connectivity, "
        "server.js explicitly registers public Google and Cloudflare nameservers via node:dns before attempting database connection."
    )
    add_body_p(
        doc,
        "Furthermore, server.js configures dynamic Cross-Origin Resource Sharing (CORS) with origin validation, strictly allowing requests "
        "originating from the local Vite development server and the deployed production frontend on Vercel while rejecting untrusted sources."
    )

    add_code_block(
        doc,
        """// server.js - Server Configuration and CORS Whitelist
import express from "express";
import dotenv from "dotenv";
import cors from "cors";
import dns from "node:dns";

dns.setServers(["8.8.8.8", "1.1.1.1"]); // Resilient DNS servers

import connectDB from "./config/db.js";
dotenv.config();
await connectDB();

const app = express();
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

const allowedOrigins = [
  "http://localhost:5173",
  process.env.FRONTEND_URL,
];

app.use(
  cors({
    origin(origin, callback) {
      if (!origin || allowedOrigins.includes(origin)) {
        return callback(null, true);
      }
      return callback(null, false);
    },
    credentials: true,
  })
);""",
        "Listing 6.2: Server Setup and Secure CORS Middleware in server.js"
    )

    add_subsection_heading(doc, "6.3.2", "MongoDB Atlas Cloud Connectivity")
    add_body_p(
        doc,
        "Database connectivity is encapsulated within config/db.js. The module connects asynchronously to MongoDB Atlas using "
        "mongoose.connect(process.env.MONGO_URI), establishing an encrypted TLS connection pool that persists across all incoming API requests."
    )

    add_subsection_heading(doc, "6.3.3", "JWT Protection Middleware and Token Generation")
    add_body_p(
        doc,
        "Route security is enforced through custom middleware (middleware/authMiddleware.js). When a request hits a protected endpoint, "
        "the protect function intercepts the Authorization header, extracts the Bearer token, verifies its signature against JWT_SECRET "
        "using jwt.verify(), queries MongoDB for the associated user record (excluding password), and attaches the user document to req.user. "
        "If the token is missing, expired, or tampered with, the middleware terminates execution with HTTP 401 Unauthorized."
    )

    add_code_block(
        doc,
        """// middleware/authMiddleware.js - Stateless JWT Authorization Guard
import jwt from "jsonwebtoken";
import User from "../models/User.js";

const protect = async (req, res, next) => {
  let token;
  try {
    if (req.headers.authorization && req.headers.authorization.startsWith("Bearer")) {
      token = req.headers.authorization.split(" ")[1];
    }
    if (!token) {
      return res.status(401).json({ success: false, message: "Not authorized" });
    }
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = await User.findById(decoded.id).select("-password");
    next();
  } catch (error) {
    return res.status(401).json({ success: false, message: "Invalid or expired token" });
  }
};
export default protect;""",
        "Listing 6.3: Stateless JWT Authorization Guard in authMiddleware.js"
    )

    add_section_heading(doc, "6.4", "Backend Controllers and Business Logic")
    
    add_subsection_heading(doc, "6.4.1", "Authentication Controller (Registration & Login)")
    add_body_p(
        doc,
        "The authControllers.js module manages user onboarding and authentication. In registerUser, incoming payloads ({name, email, password}) "
        "are checked for duplicates via User.findOne({email}). If unique, the password is encrypted via bcrypt.hash(password, 10). "
        "A new User document is persisted, and a 7-day signed JWT token is returned alongside sanitized user details. "
        "In login, the stored hash is verified via bcrypt.compare(); upon match, a fresh JWT is issued."
    )

    add_subsection_heading(doc, "6.4.2", "User Profile and Password Management")
    add_body_p(
        doc,
        "Encapsulated in userController.js, getProfile returns the currently authenticated user's name and email. updateProfile allows users "
        "to modify their display credentials. The changePassword controller enforces cryptographic security: it demands currentPassword, "
        "newPassword, and confirmPassword, verifies the existing password via bcrypt.compare(), validates password matching, hashes the new "
        "password with 10 salt rounds, and commits the updated credential to MongoDB."
    )

    add_subsection_heading(doc, "6.4.3", "Transaction Controller (Full CRUD Operations)")
    add_body_p(
        doc,
        "The transactionController.js file provides high-performance transaction management:"
    )
    add_bullet_p(doc, "addTransaction", "Validates presence of type, amount, category, and paymentMethod. Inserts a new Transaction document with user: req.user._id, returning HTTP 201 Created.")
    add_bullet_p(doc, "getTransactions", "Implements paginated retrieval. Reads query parameters page (default 1) and limit (default 10). Calculates skip = (page - 1) * limit, counts total matching records via countDocuments, sorts by {date: -1}, and returns the current slice alongside totalPages.")
    add_bullet_p(doc, "getTransactionById", "Retrieves a single transaction matching both _id: req.params.id and user: req.user._id, guaranteeing cross-tenant data isolation.")
    add_bullet_p(doc, "updateTransaction", "Enforces user ownership, dynamically updating only fields provided in req.body before executing transaction.save().")
    add_bullet_p(doc, "deleteTransaction", "Verifies ownership and permanently removes the document via transaction.deleteOne().")

    add_subsection_heading(doc, "6.4.4", "Dashboard Aggregation Controller")
    add_body_p(
        doc,
        "In dashboardController.js, getDashboard aggregates cash flows across the authenticated user's entire history. The controller queries "
        "all user transactions sorted by createdAt descending. It computes totalIncome, totalExpense, derives net balance (totalIncome - totalExpense), "
        "counts total transactions, and extracts the 5 most recent transactions for display in the dashboard overview feed."
    )

    add_subsection_heading(doc, "6.4.5", "Analytics Aggregation Controller")
    add_body_p(
        doc,
        "In analyticsController.js, getCategoryAnalytics filters user transactions for type === 'expense' and aggregates spending totals "
        "into a key-value category map ({Food: 5400, Travel: 1200, ...}), which is formatted directly for Recharts PieChart rendering. "
        "Symmetrically, getMonthlyExpense extracts the calendar month from transaction.date, aggregating expenses across all 12 calendar months "
        "into a chronologically ordered array [{month: 'January', amount: 12000}, ...] for LineChart rendering."
    )

    add_subsection_heading(doc, "6.4.6", "AI Insights Service and Controller")
    add_body_p(
        doc,
        "The AI integration pipeline is divided between controllers/aiController.js, services/aiService.js, and utils/promptBuilder.js. "
        "aiService.generateInsights(userId) computes total income, total expense, balance, and category-wise spending. "
        "buildPrompt(summary) injects these figures into an expert financial persona prompt that strictly mandates valid JSON output without "
        "markdown code fences. The service calls GoogleGenAI with model 'gemini-2.5-flash', cleans the returned text using regex replacements "
        "(stripping ```json and ```), and parses the text with JSON.parse(). If parsing fails, a safe fallback JSON object is returned."
    )

    add_code_block(
        doc,
        """// services/aiService.js - Google Gemini 2.5 Flash Inference Pipeline
export const generateInsights = async (userId) => {
  const transactions = await Transaction.find({ user: userId });
  let totalIncome = 0, totalExpense = 0;
  const categoryWiseExpense = {};

  transactions.forEach((t) => {
    if (t.type === "income") totalIncome += t.amount;
    else {
      totalExpense += t.amount;
      categoryWiseExpense[t.category] = (categoryWiseExpense[t.category] || 0) + t.amount;
    }
  });

  const summary = { totalIncome, totalExpense, balance: totalIncome - totalExpense,
                    totalTransactions: transactions.length, categoryWiseExpense };
  const prompt = buildPrompt(summary);

  const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });
  const response = await ai.models.generateContent({
    model: "gemini-2.5-flash",
    contents: prompt,
  });

  const cleaned = response.text.replace(/```json/g, "").replace(/```/g, "").trim();
  try {
    return JSON.parse(cleaned);
  } catch {
    return { summary: "Unable to parse AI response.", insights: [], recommendations: [] };
  }
};""",
        "Listing 6.4: AI Financial Inference Engine in aiService.js"
    )

    add_subsection_heading(doc, "6.4.7", "Multi-Format Report Controller (PDF, Excel, CSV, JSON)")
    add_body_p(
        doc,
        "In reportController.js, ExpenseX provides streaming export engines for four major document formats:"
    )
    add_bullet_p(doc, "exportPDF", "Initializes a PDFDocument instance from pdfkit, sets Content-Type to application/pdf with attachment filename expense-report.pdf, and pipes the document stream directly into res. It renders report headers, summary totals (Income, Expense, Balance), and formats individual transaction rows with dates, categories, and amounts.")
    add_bullet_p(doc, "exportExcel", "Instantiates an ExcelJS.Workbook, adds an 'Expense Report' worksheet, defines styled columns with custom widths, sets header font to bold, populates transaction rows, and streams the workbook via workbook.xlsx.write(res) with application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.")
    add_bullet_p(doc, "exportCSV", "Fetches transactions via .lean(), transforms fields into a clean data array, and executes Parser({fields}).parse(data) via json2csv, streaming standard CSV text with attachment header expense-report.csv.")
    add_bullet_p(doc, "exportJSON", "Serializes transaction records into a structured JSON payload with system generation timestamps and total counts, setting Content-Disposition to attachment filename expense-report.json.")

    add_section_heading(doc, "6.5", "Frontend Core Implementation")
    
    add_subsection_heading(doc, "6.5.1", "Client Architecture, Vite Bundler & Entry Point")
    add_body_p(
        doc,
        "The frontend is mounted in main.jsx, wrapping the root <App /> component with BrowserRouter from react-router-dom and ToastContainer "
        "from react-toastify to deliver real-time non-blocking alert toasts."
    )

    add_subsection_heading(doc, "6.5.2", "Client-Side Routing and Protected Route Guards")
    add_body_p(
        doc,
        "In App.jsx, public routes / and /auth render the Landing portal and AuthPage respectively. Protected application views (/dashboard, "
        "/transactions, /analytics, /ai, /reports, /settings) are wrapped within the <Auth> component (utils/Auth.jsx) and rendered inside "
        "<DashboardLayout>. <Auth> inspects localStorage: if neither a valid token nor demoMode flag is detected, it redirects to /auth."
    )

    add_subsection_heading(doc, "6.5.3", "Data Abstraction Layer (Dual Live & Demo Mode)")
    add_body_p(
        doc,
        "The frontend implements an abstracted data service layer in components/data/dataService.js. The isDemo() utility detects whether "
        "the user is evaluating the system in Guest Mode (demoMode === 'true' and no token). If true, calls resolve instantaneously through "
        "demoService.js using browser LocalStorage; if false, calls dispatch live authenticated HTTP requests through apiService.js."
    )

    add_subsection_heading(doc, "6.5.4", "Dashboard Layout and Real-Time Summary Cards")
    add_body_p(
        doc,
        "The Dashboard.jsx view renders DashboardHeader, SummaryCards, and BarGraph. SummaryCards maps the dashboard summary object into "
        "four responsive metric cards: Net Balance (₹), Total Income (₹), Total Expenses (₹), and Total Transaction Counts, each styled with "
        "distinctive color gradients and Tabler icons."
    )

    add_subsection_heading(doc, "6.5.5", "Transaction Management (Table, Search, Form, Modal)")
    add_body_p(
        doc,
        "In Transactions.jsx, users interact with a complete transaction management interface. The component maintains transactions state, "
        "page, search query, and filter category. Search filtering executes in real time across categories, descriptions, and payment methods. "
        "The AddTransactionModal houses TransactionForm, handling both creation and editing through an onSubmit prop, while TransactionTable "
        "renders individual rows with color-coded badges, formatted dates, and Edit/Delete action buttons."
    )

    add_subsection_heading(doc, "6.5.6", "Analytics and Recharts Visualizations")
    add_body_p(
        doc,
        "In Analytics.jsx, ExpenseCategoryChart uses Recharts <PieChart> and <Pie> to render category expenditure shares. Clicking any pie "
        "slice dynamically filters the underlying transaction list to display only expenses within that category, computing a localized total. "
        "MonthlyExpenseChart renders a responsive <LineChart> with CartesianGrid, XAxis (months), YAxis (amounts), and smooth monotone splines."
    )

    add_subsection_heading(doc, "6.5.7", "AI Insights Interface Component")
    add_body_p(
        doc,
        "In AIInsights.jsx and AIInsightCard.jsx, the client renders the structured Gemini response. The interface displays a prominent "
        "Financial Health status badge, an overall numerical score (0-100), a detailed Spending Analysis paragraph, Savings Recommendations, "
        "Highest Expense Category callout, Smart Alert bullet items, Personalized Tips, and a target Next Month Goal."
    )

    add_subsection_heading(doc, "6.5.8", "Reports Generation Portal Component")
    add_body_p(
        doc,
        "In Reports.jsx, users view an overall ReportSummary card and access two export sections: Complete Report Export (instant PDF and Excel "
        "downloads) and Date-Filtered Export (allowing users to pick fromDate and toDate inputs before downloading filtered PDF or Excel statements)."
    )

    add_subsection_heading(doc, "6.5.9", "User Profile and Password Settings Interface")
    add_body_p(
        doc,
        "Settings.jsx provides two secure forms: a Profile Settings form allowing modification of full name and email address, and a "
        "Password Change form requiring current password verification, new password entry, and confirmation matching."
    )

    add_subsection_heading(doc, "6.5.10", "Landing Page & Marketing Portal")
    add_body_p(
        doc,
        "Landing.jsx serves as the public gateway, featuring a responsive Navbar, Hero section with call-to-action buttons ('Get Started' "
        "and 'Try Demo'), interactive Features grid, live animated Counter stats, interactive Preview mockup, and Contact form."
    )

    add_section_heading(doc, "6.6", "Input Validation and Sanitization Rules Matrix")
    add_body_p(
        doc,
        "Table 6.1 documents the full-stack validation and sanitization matrix enforced across ExpenseX:"
    )

    # Table 6.1
    t10_headers = ["Field / Parameter", "Data Type", "Client-Side Check", "Server-Side Mongoose Rule", "Sanitization Strategy", "Error Response Message"]
    t10_data = [
        ["User Name", "String", "required, non-empty", "required: true, trim: true", "Strips leading/trailing whitespace", "\"Please fill all required fields\""],
        ["User Email", "String", "type='email', regex format", "required: true, unique: true, lowercase: true", "Converts to lowercase, trims whitespace", "\"Already Registered\" / \"Invalid Email\""],
        ["User Password", "String", "required, min length 6", "required: true, minlength: 6", "10-round salted bcrypt hashing", "\"Password must be at least 6 characters\""],
        ["Transaction Type", "String", "select: income | expense", "required: true, enum: ['income', 'expense']", "Strict whitelist equality matching", "\"Invalid transaction type\""],
        ["Transaction Amount", "Number", "type='number', min=1", "required: true, min: 1", "parseFloat() casting; rejects NaN/negative", "\"Amount must be a positive number >= 1\""],
        ["Transaction Category", "String", "required, text input", "required: true, trim: true", "Strips whitespace; default category fallback", "\"Category is required\""],
        ["Payment Method", "String", "required, select input", "enum: [Cash, UPI, Debit Card, Credit Card, ...]", "Strict enum validation against whitelist", "\"Invalid payment method specified\""],
        ["Transaction Date", "Date", "type='date' picker", "type: Date, default: Date.now", "ISO 8601 Date object parsing", "\"Invalid date format provided\""],
        ["Current Password", "String", "required input", "Verified via bcrypt.compare()", "Zero plaintext storage in memory", "\"Current password is incorrect\""]
    ]
    add_styled_table(doc, "Table 6.1", "Full-Stack Input Validation and Sanitization Matrix", t10_headers, t10_data, [1.1, 0.75, 1.1, 1.25, 1.1, 1.2])

    add_section_heading(doc, "6.7", "Error Handling and Toast Notification Pipeline")
    add_body_p(
        doc,
        "The system coordinates user notifications through React-Toastify. When API calls succeed, positive alerts ('Transaction added', "
        "'Welcome back! 🎉') appear for 800–2000 ms. When validation fails or server errors occur, error toasts display the server-supplied "
        "error message, maintaining clear communication with the user."
    )

    add_section_heading(doc, "6.8", "Responsive Design and CSS Grid/Flexbox Layouts")
    add_body_p(
        doc,
        "ExpenseX implements fluid CSS Grid and Flexbox layouts. The Sidebar collapses into a slide-out drawer on screens narrower than "
        "768 px, toggled via a hamburger menu icon in Navbar.jsx. Summary cards transition from a 4-column desktop grid to a 2-column tablet "
        "grid and a 1-column mobile layout, ensuring seamless usability across all device form factors."
    )

    doc.add_page_break()

    # =========================================================================
    # CHAPTER 7 — SOFTWARE TESTING
    # =========================================================================
    add_chapter_heading(doc, "CHAPTER 7", "SOFTWARE TESTING")
    
    add_section_heading(doc, "7.1", "Introduction to Software Testing in ExpenseX")
    add_body_p(
        doc,
        "Software testing is an indispensable engineering discipline dedicated to verifying that the developed application conforms "
        "to specified requirements, operates reliably under boundary conditions, maintains data integrity, and resists malicious or "
        "erroneous inputs. In ExpenseX, testing was integrated continuously across every sprint cycle."
    )

    add_section_heading(doc, "7.2", "Testing Objectives and Philosophy")
    add_body_p(
        doc,
        "The primary testing objectives comprised:"
    )
    add_numbered_p(doc, "1", "Functional Verification", "Verifying that all 15 functional requirements (FR-01 to FR-15) execute without deviation.")
    add_numbered_p(doc, "2", "Cryptographic & Security Validation", "Validating that unauthorized requests without Bearer tokens are categorically rejected and password hashes cannot be decoded.")
    add_numbered_p(doc, "3", "Mathematical & Aggregation Precision", "Ensuring that balance calculations (Income - Expense) and category aggregations remain 100% mathematically accurate across thousands of records.")
    add_numbered_p(doc, "4", "Generative AI Resilience", "Verifying that the Gemini AI integration parses responses cleanly and degrades gracefully during API latency or quota exhaustion.")
    add_numbered_p(doc, "5", "Cross-Platform Ergonomics", "Confirming fluid responsiveness and zero layout distortion across desktop, tablet, and mobile viewports.")

    add_section_heading(doc, "7.3", "Testing Methodologies Adopted")
    add_subsection_heading(doc, "7.3.1", "Unit Testing")
    add_body_p(
        doc,
        "Individual functions—such as generateToken.js, promptBuilder.js, date parsers, and Mongoose schema validation hooks—were tested "
        "in isolation to confirm correct outputs for diverse valid and boundary inputs."
    )

    add_subsection_heading(doc, "7.3.2", "Integration Testing")
    add_body_p(
        doc,
        "Integration testing evaluated the communication interfaces between coupled subsystems: Express routers communicating with Mongoose "
        "models, the protect middleware passing authenticated users to controllers, and aiService communicating with Google Cloud's Gemini API."
    )

    add_subsection_heading(doc, "7.3.3", "System Testing")
    add_body_p(
        doc,
        "The entire integrated application was tested end-to-end against real-world scenarios: registering a user, logging in, adding 20 transactions, "
        "inspecting charts, generating an AI insight, downloading a PDF statement, and updating profile credentials."
    )

    add_subsection_heading(doc, "7.3.4", "Functional & Black-Box Testing")
    add_body_p(
        doc,
        "Black-box test cases evaluated system behavior from an external user perspective, submitting edge-case inputs (empty passwords, "
        "negative amounts, illegal payment strings, future dates) to confirm strict error handling."
    )

    add_subsection_heading(doc, "7.3.5", "UI and Usability Testing")
    add_body_p(
        doc,
        "Conducted with focus group users to assess navigational flow, modal readability, form clarity, and visual feedback responsiveness."
    )

    add_subsection_heading(doc, "7.3.6", "API Testing via Postman & REST Clients")
    add_body_p(
        doc,
        "All REST endpoints were systematically tested using VS Code REST Client (.rest scripts) and Postman, validating JSON request payloads, "
        "bearer token headers, HTTP status codes, and response bodies."
    )

    add_subsection_heading(doc, "7.3.7", "Security and Penetration Testing")
    add_body_p(
        doc,
        "Attempted SQL/NoSQL injection payloads, cross-site scripting (XSS) strings in transaction descriptions, forged JWT tokens, and expired "
        "tokens to confirm robust defense mechanisms."
    )

    add_subsection_heading(doc, "7.3.8", "Cross-Browser and Responsive Testing")
    add_body_p(
        doc,
        "Verified UI rendering across Google Chrome, Mozilla Firefox, Apple Safari, Microsoft Edge, and mobile emulators (iPhone 14, Pixel 7, iPad)."
    )

    add_section_heading(doc, "7.4", "Test Environment and Hardware/Software Setup")
    add_body_p(
        doc,
        "Testing was conducted on a Windows 11 host with Node.js v20.11, running Chrome DevTools, Postman v11, and connected to a live "
        "MongoDB Atlas cloud cluster and Google AI Studio Gemini API."
    )

    add_section_heading(doc, "7.5", "Comprehensive Test Cases Suite (Table 7.1)")
    add_body_p(
        doc,
        "Table 7.1 details the comprehensive test suite executed across all modules of ExpenseX:"
    )

    # Table 7.1 Test Cases
    t11_headers = ["Test ID", "Module", "Test Scenario", "Preconditions", "Test Input Data", "Expected Output", "Observed Result", "Status"]
    t11_data = [
        ["TC-01", "Auth", "Register with valid credentials", "Unique email", "name: 'Ritik', email: 'cs.ritik@test.com', pass: 'Test@123'", "HTTP 201 + JWT Token + User object", "HTTP 201 + Token returned + Redirection", "Pass"],
        ["TC-02", "Auth", "Register with duplicate email", "Email cs.ritik@test.com exists", "Same email, new password", "HTTP 200 {message: 'Already Registered'}", "Error toast 'Already Registered'", "Pass"],
        ["TC-03", "Auth", "Login with invalid password", "User exists", "email: 'cs.ritik@test.com', pass: 'WrongPass'", "HTTP 200 {message: 'Invalid Password'}", "Error toast 'Invalid Password' displayed", "Pass"],
        ["TC-04", "Auth", "Login with non-existent email", "Email not registered", "email: 'unknown@user.com', pass: 'AnyPass'", "HTTP 200 {message: 'Invalid'}", "Error toast 'Invalid' displayed", "Pass"],
        ["TC-05", "Auth", "Login with valid credentials", "Valid registered user", "Correct email and password", "HTTP 200 + Token + Redirection to /dashboard", "Token saved in localStorage; dashboard loads", "Pass"],
        ["TC-06", "Guest", "Trigger Guest Demo Mode", "No prior session", "Click 'Continue as Guest'", "demoMode='true' set in localStorage; mock data loads", "Dashboard opens instantly with demo stats", "Pass"],
        ["TC-07", "Dashboard", "Fetch dashboard metrics", "Authenticated user", "GET /api/dashboard with Bearer Token", "HTTP 200 + {balance, totalIncome, totalExpense, recent}", "Metrics match mathematical sum of transactions", "Pass"],
        ["TC-08", "Transaction", "Add valid income transaction", "Logged-in user", "type: 'income', amount: 50000, category: 'Salary', method: 'Bank Transfer'", "HTTP 201 + created transaction doc", "Transaction saved; balance increases by 50,000", "Pass"],
        ["TC-09", "Transaction", "Add valid expense transaction", "Logged-in user", "type: 'expense', amount: 2500, category: 'Food', method: 'UPI'", "HTTP 201 + created transaction doc", "Transaction saved; expense increases by 2,500", "Pass"],
        ["TC-10", "Transaction", "Add transaction with negative amount", "Logged-in user", "type: 'expense', amount: -500, category: 'Travel'", "Validation error; request rejected", "Frontend blocks form submission (amount >= 1)", "Pass"],
        ["TC-11", "Transaction", "Add transaction missing required fields", "Logged-in user", "type: 'expense', amount: 1000, category: '' (empty)", "HTTP 400 'Please fill all required fields'", "HTTP 400 returned; error toast shown", "Pass"],
        ["TC-12", "Transaction", "Fetch paginated transactions", "User has 25 transactions", "GET /api/transactions?page=1&limit=10", "HTTP 200 with 10 transactions, totalPages: 3", "10 records rendered; Pagination shows Page 1 of 3", "Pass"],
        ["TC-13", "Transaction", "Update existing transaction", "Transaction exists", "PUT /api/transactions/:id with amount: 3000", "HTTP 200 + updated document", "Table updates immediately with ₹3,000", "Pass"],
        ["TC-14", "Transaction", "Delete existing transaction", "Transaction exists", "DELETE /api/transactions/:id", "HTTP 200 'Transaction deleted successfully'", "Confirmation dialog accepted; row deleted", "Pass"],
        ["TC-15", "Analytics", "Fetch category analytics", "User has expenses", "GET /api/analytics/category", "HTTP 200 with category totals object", "Recharts Pie Chart renders slices with colors", "Pass"],
        ["TC-16", "Analytics", "Drill-down on category pie slice", "Category chart loaded", "Click on 'Food' pie segment", "Filtered list of Food transactions displayed", "Table updates showing only Food items & sum", "Pass"],
        ["TC-17", "Analytics", "Fetch monthly expense trend", "Multi-month expenses", "GET /api/analytics/monthly-expense", "HTTP 200 with 12-month array", "Line Chart renders monthly spending curve", "Pass"],
        ["TC-18", "AI Insights", "Generate AI insights successfully", "Transactions exist", "GET /api/ai/insights with Bearer Token", "HTTP 200 with structured JSON health cards", "AI cards render: Score, Analysis, Alerts, Goals", "Pass"],
        ["TC-19", "AI Insights", "Handle AI fallback on empty transactions", "Zero transactions", "GET /api/ai/insights", "Safe JSON fallback object returned", "Displays 'No AI insights available' placeholder", "Pass"],
        ["TC-20", "Reports", "Export full PDF report", "Transactions exist", "GET /api/reports/pdf", "HTTP 200 + application/pdf binary stream", "expense-report.pdf downloads; opens cleanly", "Pass"],
        ["TC-21", "Reports", "Export full Excel spreadsheet", "Transactions exist", "GET /api/reports/excel", "HTTP 200 + .xlsx binary workbook", "expense-report.xlsx downloads with bold headers", "Pass"],
        ["TC-22", "Reports", "Export CSV data", "Transactions exist", "GET /api/reports/csv", "HTTP 200 + text/csv comma-separated file", "expense-report.csv downloads; opens in Excel", "Pass"],
        ["TC-23", "Profile", "Update profile full name", "Logged in", "PUT /api/users/profile with name: 'Ritik R.'", "HTTP 200 'Profile updated successfully'", "Navbar avatar and text update to 'Ritik R.'", "Pass"],
        ["TC-24", "Profile", "Change password with wrong current pass", "Logged in", "currentPassword: 'wrong', newPassword: 'new'", "HTTP 400 'Current password is incorrect.'", "Error toast displayed; password unchanged", "Pass"],
        ["TC-25", "Security", "Access protected route without token", "Logged out", "GET /api/transactions with no Bearer token", "HTTP 401 'Not authorized'", "HTTP 401 returned; redirected to /auth", "Pass"]
    ]
    add_styled_table(doc, "Table 7.1", "Comprehensive Software Testing Suite (Unit, Integration, Security)", t11_headers, t11_data, [0.65, 0.85, 1.25, 0.85, 1.0, 1.1, 1.1, 0.5])

    add_section_heading(doc, "7.6", "Test Data and Execution Results Analysis")
    add_body_p(
        doc,
        "Execution results demonstrate robust stability across all test modules. Table 7.2 presents the quantitative test summary:"
    )

    # Table 7.2 Summary
    t12_headers = ["Testing Subsystem", "Total Test Cases", "Passed Cases", "Failed Cases", "Defect Density", "Pass Percentage (%)"]
    t12_data = [
        ["User Authentication & Security", "5", "5", "0", "0.00", "100.0%"],
        ["Guest Simulation Mode", "1", "1", "0", "0.00", "100.0%"],
        ["Dashboard & Metric Aggregations", "1", "1", "0", "0.00", "100.0%"],
        ["Transaction Lifecycle (CRUD)", "7", "7", "0", "0.00", "100.0%"],
        ["Analytics & Visual Charting", "3", "3", "0", "0.00", "100.0%"],
        ["Google Gemini AI Inference", "2", "2", "0", "0.00", "100.0%"],
        ["Multi-Format Document Reporting", "3", "3", "0", "0.00", "100.0%"],
        ["Profile & Password Management", "2", "2", "0", "0.00", "100.0%"],
        ["Authorization & Route Guards", "1", "1", "0", "0.00", "100.0%"],
        ["Total / System Aggregate", "25", "25", "0", "0.00", "100.0%"]
    ]
    add_styled_table(doc, "Table 7.2", "Summary Matrix of Test Execution Results and Pass Percentages", t12_headers, t12_data, [1.6, 1.0, 0.9, 0.9, 1.0, 1.1])

    add_section_heading(doc, "7.7", "Defect Handling, Severity Classification & Resolution")
    add_body_p(
        doc,
        "During sprint testing, defects were logged, classified by severity (Critical, High, Medium, Low), and systematically remediated. "
        "Notable resolved defects included stripping markdown code fences from Gemini responses, resolving MongoDB SRV DNS lookups "
        "via explicit nameservers, and enforcing lean queries in report generation to prevent memory spikes."
    )

    doc.add_page_break()
