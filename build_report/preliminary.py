import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from build_report.styles import (
    FONT_NAME, COLOR_PRIMARY, COLOR_TEXT, COLOR_MUTED,
    set_run_font, add_chapter_heading, add_section_heading,
    add_subsection_heading, add_body_p, add_bullet_p
)

def build_preliminary_pages(doc, logo_path=None):
    # ================= 1. TITLE PAGE =================
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_before = Pt(12)
    p_inst.paragraph_format.space_after = Pt(2)
    r = p_inst.add_run("Nirmala Memorial Foundation College of Commerce and Science\n")
    set_run_font(r, name=FONT_NAME, size_pt=15, bold=True, color=COLOR_PRIMARY)
    r_sub = p_inst.add_run("Kandivali (East), Mumbai - 400101\nPermanently Affiliated to the University of Mumbai\nAccredited by NAAC with B++ CGPA: 2.86 in 2nd cycle | ISO 9001-2015 Certified\nRecognized under Section 2(f) & 12(B) of the UGC Act 1956")
    set_run_font(r_sub, name=FONT_NAME, size_pt=10, italic=True, color=COLOR_MUTED)

    p_div = doc.add_paragraph()
    p_div.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_div.paragraph_format.space_before = Pt(8)
    p_div.paragraph_format.space_after = Pt(12)
    r_dept = p_div.add_run("DEPARTMENT OF COMPUTER SCIENCE")
    set_run_font(r_dept, name=FONT_NAME, size_pt=14, bold=True, color=COLOR_PRIMARY)

    # Logo Box / Placeholder
    p_logo = doc.add_paragraph()
    p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_logo.paragraph_format.space_before = Pt(6)
    p_logo.paragraph_format.space_after = Pt(10)
    
    # Try adding expense logo or placeholder
    if logo_path and os.path.exists(logo_path):
        try:
            p_logo.add_run().add_picture(logo_path, width=Inches(1.3))
            p_logo_note = doc.add_paragraph()
            p_logo_note.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r_clg_ph = p_logo_note.add_run("[INSERT COLLEGE LOGO HERE]")
            set_run_font(r_clg_ph, name=FONT_NAME, size_pt=10, bold=True, italic=True, color=COLOR_MUTED)
        except Exception:
            r_ph = p_logo.add_run("[INSERT COLLEGE LOGO HERE]")
            set_run_font(r_ph, name=FONT_NAME, size_pt=11, bold=True, italic=True, color=COLOR_PRIMARY)
    else:
        r_ph = p_logo.add_run("[INSERT COLLEGE LOGO HERE]")
        set_run_font(r_ph, name=FONT_NAME, size_pt=11, bold=True, italic=True, color=COLOR_PRIMARY)

    p_rep = doc.add_paragraph()
    p_rep.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_rep.paragraph_format.space_before = Pt(8)
    p_rep.paragraph_format.space_after = Pt(4)
    r_rep = p_rep.add_run("A PROJECT REPORT\nON")
    set_run_font(r_rep, name=FONT_NAME, size_pt=13, bold=True, color=RGBColor(0x37, 0x41, 0x51))

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(4)
    p_title.paragraph_format.space_after = Pt(12)
    r_title = p_title.add_run("ExpenseX — Smart Expense Tracker\n(AI-Powered Full-Stack Financial Management Platform)")
    set_run_font(r_title, name=FONT_NAME, size_pt=18, bold=True, color=COLOR_PRIMARY)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_before = Pt(8)
    p_sub.paragraph_format.space_after = Pt(2)
    r_subby = p_sub.add_run("Submitted by\n")
    set_run_font(r_subby, name=FONT_NAME, size_pt=12, italic=True)
    r_name = p_sub.add_run("[INSERT STUDENT NAME]\n(Ritik Rai)\n")
    set_run_font(r_name, name=FONT_NAME, size_pt=13, bold=True, color=COLOR_PRIMARY)
    r_roll = p_sub.add_run("Seat / Roll Number: [INSERT ROLL NUMBER / SEAT NUMBER]\nClass: T.Y.B.Sc. Computer Science (Semester VI)")
    set_run_font(r_roll, name=FONT_NAME, size_pt=11, bold=False)

    p_deg = doc.add_paragraph()
    p_deg.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_deg.paragraph_format.space_before = Pt(10)
    p_deg.paragraph_format.space_after = Pt(2)
    r_deg = p_deg.add_run("In partial fulfillment for the award of the degree of\n")
    set_run_font(r_deg, name=FONT_NAME, size_pt=11, italic=True)
    r_deg_name = p_deg.add_run("BACHELOR OF SCIENCE (COMPUTER SCIENCE)\n")
    set_run_font(r_deg_name, name=FONT_NAME, size_pt=13, bold=True, color=COLOR_PRIMARY)

    p_guide = doc.add_paragraph()
    p_guide.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_guide.paragraph_format.space_before = Pt(10)
    p_guide.paragraph_format.space_after = Pt(2)
    r_ug = p_guide.add_run("Under the Guidance of\n")
    set_run_font(r_ug, name=FONT_NAME, size_pt=11, italic=True)
    r_gname = p_guide.add_run("[INSERT PROJECT GUIDE NAME]\n(Dr. Bhakti Chaudhari / Project Guide)\n")
    set_run_font(r_gname, name=FONT_NAME, size_pt=12.5, bold=True, color=COLOR_PRIMARY)
    r_ay = p_guide.add_run("Academic Year: 2024 – 2025")
    set_run_font(r_ay, name=FONT_NAME, size_pt=11, bold=True)

    doc.add_page_break()

    # ================= 2. CERTIFICATE =================
    p_c_inst = doc.add_paragraph()
    p_c_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_c_inst.paragraph_format.space_before = Pt(10)
    p_c_inst.paragraph_format.space_after = Pt(2)
    r = p_c_inst.add_run("Nirmala Memorial Foundation College of Commerce and Science\n")
    set_run_font(r, name=FONT_NAME, size_pt=14, bold=True, color=COLOR_PRIMARY)
    r_sub = p_c_inst.add_run("Kandivali (East), Mumbai - 400101\nPermanently Affiliated to the University of Mumbai\nAccredited by NAAC with B++ CGPA: 2.86 in 2nd cycle | ISO 9001-2015 Certified\nRecognized under Section 2(f) & 12(B) of the UGC Act 1956")
    set_run_font(r_sub, name=FONT_NAME, size_pt=9.5, italic=True, color=COLOR_MUTED)

    p_cert_title = doc.add_paragraph()
    p_cert_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cert_title.paragraph_format.space_before = Pt(18)
    p_cert_title.paragraph_format.space_after = Pt(16)
    r_c = p_cert_title.add_run("CERTIFICATE")
    set_run_font(r_c, name=FONT_NAME, size_pt=18, bold=True, color=COLOR_PRIMARY)

    cert_text = (
        "This is to certify that the project entitled \"ExpenseX — Smart Expense Tracker\", "
        "is a bonafide work carried out and successfully completed by Mr. / Ms. [INSERT STUDENT NAME] "
        "(Ritik Rai), bearing Seat / Roll Number: [INSERT ROLL NUMBER / SEAT NUMBER], "
        "student of T.Y.B.Sc. Computer Science, Semester VI, in partial fulfillment of the requirements "
        "for the award of the degree of Bachelor of Science in Computer Science from the "
        "University of Mumbai during the Academic Year 2024 – 2025.\n\n"
        "The project work has been duly examined, reviewed, and approved as satisfying the academic "
        "standards prescribed by the Department of Computer Science and the University of Mumbai."
    )
    p_c_body = doc.add_paragraph()
    p_c_body.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_c_body.paragraph_format.line_spacing = 1.15
    p_c_body.paragraph_format.space_after = Pt(40)
    r_cb = p_c_body.add_run(cert_text)
    set_run_font(r_cb, name=FONT_NAME, size_pt=12, bold=False)

    # Signature Block Table
    sig_table = doc.add_table(rows=2, cols=3)
    sig_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for r in sig_table.rows:
        for c in r.cells:
            c.width = Inches(2.1)
    
    cell_top = sig_table.rows[0].cells
    cell_top[0].text = "______________________\n[INSERT GUIDE NAME]\nProject Guide / Prof-in-Charge"
    cell_top[1].text = "______________________\n[INSERT CO-ORDINATOR NAME]\nCo-ordinator, Dept of CS"
    cell_top[2].text = "______________________\n[INSERT EXAMINER NAME]\nExternal Examiner"
    
    cell_bot = sig_table.rows[1].cells
    cell_bot[0].text = "\n\n______________________\nCollege Seal & Date"
    cell_bot[1].text = "\n\n______________________\nHead of Department"
    cell_bot[2].text = "\n\n______________________\nPrincipal"
    
    for r in sig_table.rows:
        for c in r.cells:
            p = c.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in p.runs:
                set_run_font(run, name=FONT_NAME, size_pt=10, bold=True, color=RGBColor(0x37, 0x41, 0x51))

    doc.add_page_break()

    # ================= 3. DECLARATION =================
    p_dec_title = doc.add_paragraph()
    p_dec_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_dec_title.paragraph_format.space_before = Pt(18)
    p_dec_title.paragraph_format.space_after = Pt(18)
    r_dec = p_dec_title.add_run("DECLARATION")
    set_run_font(r_dec, name=FONT_NAME, size_pt=18, bold=True, color=COLOR_PRIMARY)

    dec_text_1 = (
        "I, [INSERT STUDENT NAME] (Ritik Rai), hereby declare that the project entitled "
        "\"ExpenseX — Smart Expense Tracker\" submitted in partial fulfillment for the award "
        "of the degree of Bachelor of Science in Computer Science to the Department of "
        "Computer Science, Nirmala Memorial Foundation College of Commerce and Science, "
        "affiliated to the University of Mumbai, during the Academic Year 2024 – 2025, "
        "is an authentic record of original software engineering work undertaken independently by me."
    )
    add_body_p(doc, dec_text_1)

    dec_text_2 = (
        "I further confirm that the matter embodied in this Black Book project report has not "
        "formed the basis for the award of any other Degree, Diploma, Associateship, Fellowship, "
        "or any other similar title in any college, university, or academic institution.\n\n"
        "All algorithms, system architectures, database designs, REST API implementations, and "
        "front-end modules described herein represent original development except where specifically "
        "attributed through academic citations and references. All open-source packages and cloud services "
        "employed (React, Node.js, Express, MongoDB, Google Gemini API) have been utilized strictly in "
        "accordance with their respective open licenses."
    )
    add_body_p(doc, dec_text_2)

    p_sig = doc.add_paragraph()
    p_sig.paragraph_format.space_before = Pt(60)
    p_sig.paragraph_format.line_spacing = 1.15
    r_sig = p_sig.add_run(
        "Signature of the Student: _____________________________\n"
        "Name: [INSERT STUDENT NAME] (Ritik Rai)\n"
        "Roll No / Seat No: [INSERT ROLL NUMBER / SEAT NUMBER]\n"
        "Class: T.Y.B.Sc. Computer Science (Semester VI)\n"
        "Place: Mumbai\n"
        "Date: [INSERT SUBMISSION DATE]"
    )
    set_run_font(r_sig, name=FONT_NAME, size_pt=11.5, bold=True)

    doc.add_page_break()

    # ================= 4. ACKNOWLEDGEMENT =================
    p_ack_title = doc.add_paragraph()
    p_ack_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_ack_title.paragraph_format.space_before = Pt(18)
    p_ack_title.paragraph_format.space_after = Pt(18)
    r_ack = p_ack_title.add_run("ACKNOWLEDGEMENT")
    set_run_font(r_ack, name=FONT_NAME, size_pt=18, bold=True, color=COLOR_PRIMARY)

    ack_1 = (
        "The successful completion of this final-year software engineering project, \"ExpenseX — Smart Expense Tracker\", "
        "has been a rewarding and intellectually enriching endeavor. I take this opportunity to convey my deep sense "
        "of gratitude, sincere appreciation, and heartfelt respect to all those who provided guidance, technical "
        "insight, academic encouragement, and infrastructural facilities throughout the course of this work."
    )
    add_body_p(doc, ack_1)

    ack_2 = (
        "First and foremost, I express my profound gratitude to my respected Project Guide, [INSERT PROJECT GUIDE NAME] "
        "(Dr. Bhakti Chaudhari), Department of Computer Science, for invaluable mentorship, constructive critique, "
        "patient advice, and continuous encouragement during every stage of project development. Their expertise in "
        "system architecture, requirements engineering, and academic documentation substantially elevated the quality "
        "of this work and sharpened my technical problem-solving perspective."
    )
    add_body_p(doc, ack_2)

    ack_3 = (
        "I extend my sincere thanks to the Head of the Department of Computer Science and the Co-ordinator "
        "for fostering a rigorous, collaborative, and innovation-driven learning environment. I am also deeply "
        "thankful to the Principal, Nirmala Memorial Foundation College of Commerce and Science, for providing "
        "the requisite institutional infrastructure, modern computing laboratories, and high-speed network access "
        "essential for full-stack software development and cloud API testing."
    )
    add_body_p(doc, ack_3)

    ack_4 = (
        "I also thank all faculty members, laboratory assistants, and technical staff of the Computer Science "
        "Department for their continuous assistance and technical cooperation. I am equally indebted to my "
        "peers, classmates, and friends who actively assisted during system testing, participated in usability surveys, "
        "and provided invaluable constructive feedback on the user interface and responsive behavior."
    )
    add_body_p(doc, ack_4)

    ack_5 = (
        "Finally, I convey my deepest love, gratitude, and heartfelt indebtedness to my parents and family members. "
        "Their unconditional love, endless sacrifices, moral support, and unwavering confidence in my abilities have "
        "been my pillars of strength and the ultimate inspiration behind the successful completion of this project."
    )
    add_body_p(doc, ack_5)

    p_ack_sign = doc.add_paragraph()
    p_ack_sign.paragraph_format.space_before = Pt(30)
    r_as = p_ack_sign.add_run(
        "Thank you all.\n\n"
        "[INSERT STUDENT NAME] (Ritik Rai)\n"
        "T.Y.B.Sc. Computer Science (Semester VI)\n"
        "Nirmala Memorial Foundation College of Commerce and Science, Mumbai"
    )
    set_run_font(r_as, name=FONT_NAME, size_pt=11, bold=True)

    doc.add_page_break()

    # ================= 5. ABSTRACT & KEYWORDS =================
    p_abs_title = doc.add_paragraph()
    p_abs_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_abs_title.paragraph_format.space_before = Pt(18)
    p_abs_title.paragraph_format.space_after = Pt(16)
    r_abs = p_abs_title.add_run("ABSTRACT")
    set_run_font(r_abs, name=FONT_NAME, size_pt=18, bold=True, color=COLOR_PRIMARY)

    abstract_text = (
        "In the contemporary economic landscape, personal financial discipline and real-time expense monitoring have "
        "become critical competencies for students, working professionals, and households. However, traditional "
        "approaches—such as manual paper-based ledger recording and standalone spreadsheet workbooks—exhibit substantial "
        "deficiencies, including human computational error, lack of automated category classification, absent mobile "
        "accessibility, and zero algorithmic guidance. Conversely, existing commercial budgeting applications are often "
        "encumbered by intrusive advertisements, aggressive privacy-invasive monetization models, complex enterprise interfaces, "
        "and rigid subscription paywalls. To address these systemic limitations, this project introduces \"ExpenseX — Smart "
        "Expense Tracker\", an advanced, full-stack, cloud-native web application designed and implemented utilizing modern "
        "software engineering principles and the MERN (React 19, Node.js, Express.js, MongoDB Atlas) technology stack.\n\n"
        "ExpenseX delivers a unified digital ecosystem featuring secure JSON Web Token (JWT) stateless authentication, "
        "cryptographic password hashing via bcrypt, and a responsive single-page architecture built with Vite. The platform "
        "provides seamless CRUD (Create, Read, Update, Delete) transaction management with strict server-side validation, "
        "dynamic pagination, search, and multi-criteria category filtering. Financial data is visualized through interactive, "
        "responsive Recharts components, including drill-down categorical Pie Charts and longitudinal Monthly Expense trend "
        "Line Charts. A defining architectural innovation of ExpenseX is its deep integration with the Google Gemini 2.5 Flash "
        "Artificial Intelligence API via the official @google/genai SDK. By synthesizing aggregated categorical summaries into "
        "rigorous structured prompts, the system extracts real-time, deterministic JSON-formatted financial health scores (0–100), "
        "spending diagnostics, smart overspending alerts, and actionable next-month financial targets without transmitting sensitive "
        "personal identifiers. Furthermore, ExpenseX features an industrial-grade multi-format export engine supporting dynamic "
        "PDF generation via PDFKit, professional styled Excel spreadsheets via ExcelJS, standard CSV formats via json2csv, and "
        "raw JSON exports. Comprehensive functional, integration, and security testing confirms high system throughput, low latency, "
        "and robust resilience, establishing ExpenseX as a scalable, secure, and production-ready personal financial management solution."
    )
    add_body_p(doc, abstract_text)

    # Keywords Section
    p_kw = doc.add_paragraph()
    p_kw.paragraph_format.space_before = Pt(14)
    p_kw.paragraph_format.space_after = Pt(6)
    r_kw_lbl = p_kw.add_run("Keywords: ")
    set_run_font(r_kw_lbl, name=FONT_NAME, size_pt=11.5, bold=True, color=COLOR_PRIMARY)
    r_kws = p_kw.add_run(
        "Expense Tracking, MERN Stack, React 19, Node.js, Express.js, MongoDB Atlas, Mongoose ODM, "
        "RESTful Architecture, JSON Web Tokens (JWT), Google Gemini API, Artificial Intelligence, "
        "Data Visualization, Recharts, PDFKit, ExcelJS, Software Development Life Cycle (SDLC)."
    )
    set_run_font(r_kws, name=FONT_NAME, size_pt=11, italic=True)

    doc.add_page_break()

    # ================= 6. TABLE OF CONTENTS =================
    p_toc_title = doc.add_paragraph()
    p_toc_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_toc_title.paragraph_format.space_before = Pt(18)
    p_toc_title.paragraph_format.space_after = Pt(16)
    r_toc = p_toc_title.add_run("TABLE OF CONTENTS")
    set_run_font(r_toc, name=FONT_NAME, size_pt=18, bold=True, color=COLOR_PRIMARY)

    toc_entries = [
        ("PRELIMINARY PAGES", ""),
        ("Title Page", "i"),
        ("Certificate", "ii"),
        ("Declaration", "iii"),
        ("Acknowledgement", "iv"),
        ("Abstract", "v"),
        ("Keywords", "vi"),
        ("Table of Contents", "vii"),
        ("List of Figures", "x"),
        ("List of Tables", "xii"),
        ("", ""),
        ("CHAPTER 1 — PRELIMINARY INVESTIGATION", "1"),
        ("1.1 Organizational and Domain Overview", "1"),
        ("1.2 Description of the System", "3"),
        ("1.3 Limitations of Present and Traditional Systems", "5"),
        ("1.4 Proposed ExpenseX System and Advantages", "7"),
        ("    1.4.1 Proposed System Architecture & Core Capabilities", "7"),
        ("    1.4.2 Distinct Technical Advantages", "9"),
        ("1.5 Objectives of the Project", "10"),
        ("1.6 Scope of the Project", "11"),
        ("1.7 Need for the System", "13"),
        ("1.8 Problem Definition and Formal Statement", "14"),
        ("1.9 Comprehensive Feasibility Study", "15"),
        ("    1.9.1 Technical Feasibility", "15"),
        ("    1.9.2 Economic and Financial Feasibility", "17"),
        ("    1.9.3 Operational Feasibility", "18"),
        ("    1.9.4 Schedule and Milestone Feasibility", "19"),
        ("1.10 Project Stakeholder Identification", "20"),
        ("1.11 Hardware and Software Requirements", "21"),
        ("1.12 Project Planning, SDLC Model and Gantt Chart", "23"),
        ("", ""),
        ("CHAPTER 2 — SYSTEM ANALYSIS AND REQUIREMENTS", "25"),
        ("2.1 Fact Finding Techniques", "25"),
        ("    2.1.1 Questionnaires and Surveys", "25"),
        ("    2.1.2 Prototyping and Iterative Wireframing", "27"),
        ("    2.1.3 Market and Literature Study", "28"),
        ("2.2 Stakeholder Profiles and Persona Analysis", "29"),
        ("2.3 User Requirements", "30"),
        ("2.4 Functional Requirements Matrix", "31"),
        ("2.5 Non-Functional Requirements Specification", "34"),
        ("2.6 Hardware and Software Specifications", "36"),
        ("2.7 User Roles and Access Levels", "37"),
        ("2.8 System Constraints and Business Rules", "38"),
        ("2.9 Assumptions and Technical Dependencies", "39"),
        ("2.10 Use Case Analysis and Modeling", "40"),
        ("    2.10.1 Actor Identification", "40"),
        ("    2.10.2 Detailed Use Case Descriptions", "41"),
        ("    2.10.3 Use Case Diagram", "43"),
        ("2.11 Dynamic Activity Diagrams", "44"),
        ("    2.11.1 Authentication & Onboarding Activity", "44"),
        ("    2.11.2 Transaction Processing Activity", "46"),
        ("    2.11.3 AI Insights Synthesis Activity", "47"),
        ("", ""),
        ("CHAPTER 3 — EXISTING SYSTEM AND PROPOSED SYSTEM", "49"),
        ("3.1 Detailed Investigation of Existing Systems", "49"),
        ("3.2 Problems in Existing Accounting and Tracking Approaches", "50"),
        ("3.3 Limitations Matrix of Existing Systems", "52"),
        ("3.4 Proposed ExpenseX Architectural Solution", "53"),
        ("3.5 Proposed System Workflow and Operational Life Cycle", "55"),
        ("3.6 Major Features and Module Highlights", "57"),
        ("3.7 Functional Advantages of ExpenseX", "59"),
        ("3.8 Technical Comparison Between Existing Systems and ExpenseX", "60"),
        ("3.9 Scope of Improvement and Long-Term Value", "62"),
        ("", ""),
        ("CHAPTER 4 — SYSTEM DESIGN", "63"),
        ("4.1 System Architecture Overview", "63"),
        ("4.2 High-Level Three-Tier Architecture", "64"),
        ("4.3 Frontend Client Architecture (React 19 & Vite)", "66"),
        ("4.4 Backend Server Architecture (Node.js & Express 5)", "68"),
        ("4.5 Database and Storage Architecture (MongoDB Atlas)", "70"),
        ("4.6 RESTful API Architectural Design", "71"),
        ("4.7 Authentication and Authorization Architecture (JWT)", "73"),
        ("4.8 Data Flow Diagrams (DFD)", "75"),
        ("    4.8.1 Context-Level DFD (Level 0)", "75"),
        ("    4.8.2 Detailed DFD Level 1", "76"),
        ("    4.8.3 Transaction and AI DFD Level 2", "78"),
        ("4.9 Class Diagrams and Domain Model", "79"),
        ("4.10 Component Diagram", "81"),
        ("4.11 Package and Module Dependency Diagram", "83"),
        ("4.12 Interaction Sequence Diagrams", "85"),
        ("    4.12.1 Authentication & Token Issuance Sequence", "85"),
        ("    4.12.2 Transaction Creation and Audit Sequence", "87"),
        ("    4.12.3 AI Insight Generation Sequence", "89"),
        ("    4.12.4 Multi-Format Report Streaming Sequence", "91"),
        ("4.13 Cloud Deployment Diagram", "92"),
        ("4.14 Security and Defense-in-Depth Design", "94"),
        ("4.15 Global Error Handling Strategy", "96"),
        ("4.16 Client and Server Validation Design", "97"),
        ("", ""),
        ("CHAPTER 5 — DATABASE DESIGN", "99"),
        ("5.1 Database Introduction and Selection Rationale", "99"),
        ("5.2 MongoDB Document-Oriented Architecture", "101"),
        ("5.3 Physical Data Model and Database Cluster Topology", "102"),
        ("5.4 Entity Relationship (ER) and Document Reference Model", "103"),
        ("5.5 Detailed Collection Schemas", "105"),
        ("    5.5.1 Users Collection Schema Specification", "105"),
        ("    5.5.2 Transactions Collection Schema Specification", "107"),
        ("5.6 Data Types and BSON Representation", "109"),
        ("5.7 Relational Referencing and Foreign Key Integrity", "110"),
        ("5.8 Schema Constraints and Mongoose Built-in Validators", "111"),
        ("5.9 Database Indexing Strategy and Query Optimization", "112"),
        ("5.10 Data Security, Encryption, and Transport Layer TLS", "113"),
        ("5.11 Core Database Operations and Aggregation Pipelines", "114"),
        ("5.12 Data Backup, Sharding, and Disaster Recovery", "116"),
        ("", ""),
        ("CHAPTER 6 — SYSTEM IMPLEMENTATION & CODING", "118"),
        ("6.1 Development Environment and Software Toolchain", "118"),
        ("6.2 Project Folder Hierarchy (Full-Stack Monorepo Breakdown)", "119"),
        ("6.3 Backend Core Implementation", "122"),
        ("    6.3.1 Express Server Initialization & DNS Optimization", "122"),
        ("    6.3.2 MongoDB Atlas Cloud Connectivity", "124"),
        ("    6.3.3 JWT Protection Middleware and Token Generation", "125"),
        ("6.4 Backend Controllers and Business Logic", "127"),
        ("    6.4.1 Authentication Controller (Registration & Login)", "127"),
        ("    6.4.2 User Profile and Password Management", "129"),
        ("    6.4.3 Transaction Controller (Full CRUD Operations)", "131"),
        ("    6.4.4 Dashboard Aggregation Controller", "134"),
        ("    6.4.5 Analytics Aggregation Controller", "136"),
        ("    6.4.6 AI Insights Service and Controller", "138"),
        ("    6.4.7 Multi-Format Report Controller (PDF, Excel, CSV, JSON)", "141"),
        ("6.5 Frontend Core Implementation", "145"),
        ("    6.5.1 Client Architecture, Vite Bundler & Entry Point", "145"),
        ("    6.5.2 Client-Side Routing and Protected Route Guards", "146"),
        ("    6.5.3 Data Abstraction Layer (Dual Live & Demo Mode)", "148"),
        ("    6.5.4 Dashboard Layout and Real-Time Summary Cards", "150"),
        ("    6.5.5 Transaction Management (Table, Search, Form, Modal)", "152"),
        ("    6.5.6 Analytics and Recharts Visualizations", "155"),
        ("    6.5.7 AI Insights Interface Component", "157"),
        ("    6.5.8 Reports Generation Portal Component", "159"),
        ("    6.5.9 User Profile and Password Settings Interface", "161"),
        ("    6.5.10 Landing Page & Marketing Portal", "163"),
        ("6.6 Input Validation and Sanitization Rules Matrix", "165"),
        ("6.7 Error Handling and Toast Notification Pipeline", "168"),
        ("6.8 Responsive Design and CSS Grid/Flexbox Layouts", "170"),
        ("", ""),
        ("CHAPTER 7 — SOFTWARE TESTING", "172"),
        ("7.1 Introduction to Software Testing in ExpenseX", "172"),
        ("7.2 Testing Objectives and Philosophy", "173"),
        ("7.3 Testing Methodologies Adopted", "174"),
        ("    7.3.1 Unit Testing", "174"),
        ("    7.3.2 Integration Testing", "175"),
        ("    7.3.3 System Testing", "176"),
        ("    7.3.4 Functional & Black-Box Testing", "177"),
        ("    7.3.5 UI and Usability Testing", "178"),
        ("    7.3.6 API Testing via Postman & REST Clients", "179"),
        ("    7.3.7 Security and Penetration Testing", "180"),
        ("    7.3.8 Cross-Browser and Responsive Testing", "181"),
        ("7.4 Test Environment and Hardware/Software Setup", "182"),
        ("7.5 Comprehensive Test Cases Suite (Table 7.1)", "183"),
        ("7.6 Test Data and Execution Results Analysis", "189"),
        ("    7.6.1 User Authentication Test Results", "189"),
        ("    7.6.2 Transaction CRUD Test Results", "191"),
        ("    7.6.3 Analytics & Visualization Test Results", "193"),
        ("    7.6.4 AI Insights Generation Test Results", "194"),
        ("    7.6.5 Report Export Test Results", "196"),
        ("    7.6.6 Summary of Execution Results (Table 7.2)", "197"),
        ("7.7 Defect Handling, Severity Classification & Resolution", "198"),
        ("", ""),
        ("CHAPTER 8 — SECURITY ANALYSIS AND MEASURES", "200"),
        ("8.1 Security Requirements in Personal Financial Software", "200"),
        ("8.2 Authentication Security and Stateless Architecture", "201"),
        ("8.3 JSON Web Token (JWT) Security Specifications", "202"),
        ("8.4 Cryptographic Password Protection (Bcrypt Hashing)", "204"),
        ("8.5 Authorization and User Isolation Controls", "205"),
        ("8.6 REST API Endpoint Protection", "207"),
        ("8.7 Input Validation and Injection Attack Mitigation", "208"),
        ("8.8 Database Access Security and Network Isolation", "209"),
        ("8.9 Environment Variable Isolation and Secret Management", "210"),
        ("8.10 Gemini AI API Key Protection", "211"),
        ("8.11 Session Handling and Client-Side Storage Considerations", "212"),
        ("8.12 OWASP Top 10 Web Vulnerability Assessment (Table 8.1)", "213"),
        ("8.13 Error Information Exposure and Sanitization", "215"),
        ("8.14 Recommended Security Enhancements for Production", "216"),
        ("", ""),
        ("CHAPTER 9 — ARTIFICIAL INTELLIGENCE INTEGRATION", "218"),
        ("9.1 Introduction to Generative AI in Personal Finance", "218"),
        ("9.2 Architectural Purpose and Role of AI in ExpenseX", "219"),
        ("9.3 Google Gemini 2.5 Flash Model Overview", "220"),
        ("9.4 Financial Insights Domain Architecture", "221"),
        ("9.5 End-to-End Technical Data Flow Pipeline", "222"),
        ("9.6 AI Prompt Engineering and Dynamic Synthesis", "224"),
        ("9.7 Structured JSON Enforcement and Response Parsing", "226"),
        ("9.8 AI Output Metrics and Diagnostics Categories", "228"),
        ("9.9 Client-Side Interactive AI Rendering", "230"),
        ("9.10 Financial and Operational Benefits of AI Integration", "232"),
        ("9.11 Technical Limitations and Hallucination Mitigation", "233"),
        ("9.12 Data Privacy and Regulatory Considerations", "234"),
        ("9.13 Third-Party Security and API Quota Management", "235"),
        ("9.14 Graceful Failure Handling and Fallback Architecture", "236"),
        ("9.15 Future Roadmap for Predictive AI Analytics", "237"),
        ("", ""),
        ("CHAPTER 10 — RESULTS AND DISCUSSION", "239"),
        ("10.1 Operational Implementation Overview", "239"),
        ("10.2 Landing and Authentication Results", "240"),
        ("10.3 Dashboard Overview and Metrics Results", "242"),
        ("10.4 Transaction Management Results", "245"),
        ("10.5 Analytics and Interactive Visualization Results", "248"),
        ("10.6 AI-Powered Financial Health Results", "251"),
        ("10.7 Multi-Format Report Generation Results", "254"),
        ("10.8 Profile and Security Management Results", "257"),
        ("10.9 Responsive and Mobile Adaptation Results", "259"),
        ("10.10 Performance, Usability, and Analytical Discussion", "261"),
        ("", ""),
        ("CHAPTER 11 — DEPLOYMENT AND MAINTENANCE", "264"),
        ("11.1 Deployment Overview and Cloud Topology", "264"),
        ("11.2 Frontend Hosting on Vercel Edge Network", "265"),
        ("11.3 Backend Hosting on Render Cloud", "267"),
        ("11.4 Database Provisioning on MongoDB Atlas", "269"),
        ("11.5 DNS Configuration and Custom Domain Routing", "271"),
        ("11.6 Environment Configuration and Secrets Deployment", "272"),
        ("11.7 Production Build Optimization and Tree-Shaking", "274"),
        ("11.8 System Monitoring, Logging, and Uptime Health", "275"),
        ("11.9 Backup, Replication, and Disaster Recovery", "277"),
        ("11.10 Software Maintenance Lifecycle", "278"),
        ("11.11 Corrective Maintenance Operations", "279"),
        ("11.12 Adaptive Maintenance Strategies", "280"),
        ("11.13 Perfective Maintenance Roadmap", "281"),
        ("11.14 Preventive Maintenance and Security Audits", "282"),
        ("", ""),
        ("CHAPTER 12 — PROJECT MANAGEMENT", "284"),
        ("12.1 Software Development Life Cycle (SDLC) Methodology", "284"),
        ("12.2 Agile Scrum Iteration Breakdown", "286"),
        ("12.3 Project Schedule and Key Milestones", "287"),
        ("12.4 Task Allocation and Responsibilities Matrix", "289"),
        ("12.5 Comprehensive Risk Management Plan (Table 12.1)", "290"),
        ("12.6 Resource Planning and Development Budget", "292"),
        ("12.7 Key Development Challenges Encountered", "293"),
        ("12.8 Technical Solutions Adopted", "295"),
        ("", ""),
        ("CHAPTER 13 — LIMITATIONS AND FUTURE SCOPE", "297"),
        ("13.1 Current System Limitations", "297"),
        ("13.2 Technical Architectural Constraints", "299"),
        ("13.3 Functional Domain Constraints", "300"),
        ("13.4 Security and Authorization Constraints", "301"),
        ("13.5 Scalability and Storage Considerations", "302"),
        ("13.6 Future Scope Roadmap (Table 13.1)", "303"),
        ("    13.6.1 Cross-Platform Mobile App (React Native/Expo)", "304"),
        ("    13.6.2 Automated Category-Wise Budget Caps & Alerts", "305"),
        ("    13.6.3 Recurring Transactions & Subscription Tracker", "306"),
        ("    13.6.4 Bank Account Aggregator & SMS Parsing", "307"),
        ("    13.6.5 Multi-Currency & Real-Time Forex Support", "308"),
        ("    13.6.6 Predictive Time-Series Forecasting (ARIMA/LSTM)", "309"),
        ("    13.6.7 Collaborative Split-Expense Management", "310"),
        ("", ""),
        ("CHAPTER 14 — CONCLUSION", "311"),
        ("14.1 Summary of Problem Addressed", "311"),
        ("14.2 Summary of System Developed", "312"),
        ("14.3 Software Engineering Principles Demonstrated", "313"),
        ("14.4 Technical Competencies Acquired", "314"),
        ("14.5 Concluding Remarks and Final Evaluation", "315"),
        ("", ""),
        ("REFERENCES (IEEE FORMAT)", "316"),
        ("GLOSSARY OF TECHNICAL TERMS", "319"),
        ("APPENDICES", "323"),
        ("Appendix A — Approved Project Proposal", "323"),
        ("Appendix B — Plagiarism Evaluation Certificate", "324"),
        ("Appendix C — User Research Survey Questionnaire", "325"),
        ("Appendix D — Empirical Survey Datasheet and Metrics", "327"),
        ("Appendix E — Stakeholder Interview Transcripts", "329"),
        ("Appendix F — Complete REST API Reference Manual", "331"),
        ("Appendix G — Complete Screenshot Index & UI Atlas", "335"),
        ("Appendix H — Code Repository Setup and Deployment Guide", "337")
    ]

    toc_table = doc.add_table(rows=len(toc_entries), cols=2)
    toc_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for r in toc_table.rows:
        r.cells[0].width = Inches(5.4)
        r.cells[1].width = Inches(0.85)

    for idx, (title, page) in enumerate(toc_entries):
        row = toc_table.rows[idx]
        c0, c1 = row.cells[0], row.cells[1]
        c0.text = title
        c1.text = page
        
        p0 = c0.paragraphs[0]
        p1 = c1.paragraphs[0]
        p1.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p0.paragraph_format.space_before = Pt(1)
        p0.paragraph_format.space_after = Pt(2)
        p1.paragraph_format.space_before = Pt(1)
        p1.paragraph_format.space_after = Pt(2)
        
        is_chapter = title.startswith("CHAPTER") or title in ["PRELIMINARY PAGES", "REFERENCES (IEEE FORMAT)", "GLOSSARY OF TECHNICAL TERMS", "APPENDICES"]
        for run in p0.runs:
            set_run_font(run, name=FONT_NAME, size_pt=10.5 if not is_chapter else 11, bold=is_chapter, color=COLOR_PRIMARY if is_chapter else COLOR_TEXT)
        for run in p1.runs:
            set_run_font(run, name=FONT_NAME, size_pt=10.5, bold=is_chapter, color=COLOR_PRIMARY if is_chapter else COLOR_MUTED)

    doc.add_page_break()

    # ================= 7. LIST OF FIGURES =================
    p_lof_title = doc.add_paragraph()
    p_lof_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_lof_title.paragraph_format.space_before = Pt(18)
    p_lof_title.paragraph_format.space_after = Pt(16)
    r_lof = p_lof_title.add_run("LIST OF FIGURES")
    set_run_font(r_lof, name=FONT_NAME, size_pt=18, bold=True, color=COLOR_PRIMARY)

    figures_list = [
        ("Figure 1.1", "Project Schedule and Milestone Gantt Chart", "24"),
        ("Figure 2.1", "ExpenseX System-Wide Use Case Diagram", "43"),
        ("Figure 2.2", "Activity Diagram — User Authentication & Dashboard Access", "45"),
        ("Figure 2.3", "Activity Diagram — Transaction Processing & Visual Rendering", "46"),
        ("Figure 2.4", "Activity Diagram — AI Financial Insights Pipeline", "48"),
        ("Figure 4.1", "ExpenseX High-Level Three-Tier Architecture Diagram", "65"),
        ("Figure 4.2", "Data Flow Diagram — Context Level (Level 0 DFD)", "75"),
        ("Figure 4.3", "Data Flow Diagram — Subsystem Decomposition (Level 1 DFD)", "77"),
        ("Figure 4.4", "Data Flow Diagram — Detailed Transaction & AI Engine (Level 2 DFD)", "78"),
        ("Figure 4.5", "Unified Domain Class Diagram (Models, Controllers, Services)", "80"),
        ("Figure 4.6", "Component Diagram of Frontend and Backend Subsystems", "82"),
        ("Figure 4.7", "Package and Module Dependency Diagram", "84"),
        ("Figure 4.8", "Sequence Diagram — User Registration and Login Flow", "86"),
        ("Figure 4.9", "Sequence Diagram — Transaction CRUD Lifecycle Flow", "88"),
        ("Figure 4.10", "Sequence Diagram — AI Financial Insight Generation Flow", "90"),
        ("Figure 4.11", "Sequence Diagram — Multi-Format Report Streaming Flow", "91"),
        ("Figure 4.12", "Cloud Deployment and Physical Infrastructure Diagram", "93"),
        ("Figure 5.1", "Entity-Relationship (ER) Schema Model in MongoDB Atlas", "104"),
        ("Figure 10.1", "ExpenseX Landing Portal & Marketing Presentation Interface", "241"),
        ("Figure 10.2", "User Authentication Interface (Sign-In & Registration Modal)", "242"),
        ("Figure 10.3", "Dynamic Financial Dashboard with Balance & Summary Metric Cards", "244"),
        ("Figure 10.4", "Recent Transactions Feed & Real-Time Activity Mini-Chart", "245"),
        ("Figure 10.5", "Paginated Transaction Management Interface with Search & Filters", "247"),
        ("Figure 10.6", "Add and Edit Transaction Modal Form with Input Validation", "248"),
        ("Figure 10.7", "Transaction Deletion Warning and Confirmation Dialog", "248"),
        ("Figure 10.8", "Interactive Expense Category Pie Chart with Drill-Down Listing", "250"),
        ("Figure 10.9", "Longitudinal Monthly Expense Trend Line Chart", "251"),
        ("Figure 10.10", "AI Financial Health Score Card & Spending Diagnostic Panel", "253"),
        ("Figure 10.11", "AI Smart Alerts and Actionable Personalized Recommendations", "254"),
        ("Figure 10.12", "Comprehensive Reports Portal with Dynamic Date Filter Controls", "256"),
        ("Figure 10.13", "Exported PDF Financial Statement Layout (PDFKit Engine)", "256"),
        ("Figure 10.14", "Exported Excel (.xlsx) Formatted Spreadsheet (ExcelJS Engine)", "257"),
        ("Figure 10.15", "Exported Standard CSV and JSON File Representations", "257"),
        ("Figure 10.16", "User Profile Management and Password Update Settings Screen", "258"),
        ("Figure 10.17", "Mobile Responsive View — Collapsible Drawer & Fluid Cards", "260")
    ]

    lof_table = doc.add_table(rows=len(figures_list), cols=3)
    lof_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for r in lof_table.rows:
        r.cells[0].width = Inches(1.2)
        r.cells[1].width = Inches(4.3)
        r.cells[2].width = Inches(0.75)

    for idx, (f_id, f_title, f_page) in enumerate(figures_list):
        row = lof_table.rows[idx]
        c0, c1, c2 = row.cells[0], row.cells[1], row.cells[2]
        c0.text = f_id
        c1.text = f_title
        c2.text = f_page
        
        p0, p1, p2 = c0.paragraphs[0], c1.paragraphs[0], c2.paragraphs[0]
        p2.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        for p in [p0, p1, p2]:
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(2)
            
        for run in p0.runs:
            set_run_font(run, name=FONT_NAME, size_pt=10, bold=True, color=COLOR_PRIMARY)
        for run in p1.runs:
            set_run_font(run, name=FONT_NAME, size_pt=10, bold=False, color=COLOR_TEXT)
        for run in p2.runs:
            set_run_font(run, name=FONT_NAME, size_pt=10, bold=False, color=COLOR_MUTED)

    doc.add_page_break()

    # ================= 8. LIST OF TABLES =================
    p_lot_title = doc.add_paragraph()
    p_lot_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_lot_title.paragraph_format.space_before = Pt(18)
    p_lot_title.paragraph_format.space_after = Pt(16)
    r_lot = p_lot_title.add_run("LIST OF TABLES")
    set_run_font(r_lot, name=FONT_NAME, size_pt=18, bold=True, color=COLOR_PRIMARY)

    tables_list = [
        ("Table 1.1", "Hardware Environment Specifications for Development & Client Devices", "21"),
        ("Table 1.2", "Software Environment and Development Toolchain Specifications", "22"),
        ("Table 1.3", "Project Schedule, Sprint Breakdown, and Planned vs Executed Dates", "23"),
        ("Table 2.1", "Comprehensive Functional Requirements Matrix (FR-01 to FR-15)", "32"),
        ("Table 2.2", "Non-Functional Software Quality Requirements Specification", "35"),
        ("Table 2.3", "User Roles, Permissions, and Access Privilege Matrix", "37"),
        ("Table 3.1", "Comparative Analysis Matrix: Existing Systems vs ExpenseX Platform", "61"),
        ("Table 5.1", "Users Collection Schema Data Dictionary and Integrity Constraints", "106"),
        ("Table 5.2", "Transactions Collection Schema Data Dictionary and Validation Rules", "108"),
        ("Table 6.1", "Full-Stack Input Validation and Sanitization Matrix", "166"),
        ("Table 7.1", "Comprehensive Software Testing Suite (Unit, Integration, Security)", "184"),
        ("Table 7.2", "Summary Matrix of Test Execution Results and Pass Percentages", "197"),
        ("Table 8.1", "OWASP Top 10 Security Assessment and Implemented Mitigations", "214"),
        ("Table 12.1", "Comprehensive Project Risk Assessment and Mitigation Strategies", "291"),
        ("Table 13.1", "Future Enhancements Roadmap and Phase-Wise Implementation Plan", "303"),
        ("Table F.1", "Comprehensive ExpenseX REST API Specification Matrix", "332")
    ]

    lot_table = doc.add_table(rows=len(tables_list), cols=3)
    lot_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for r in lot_table.rows:
        r.cells[0].width = Inches(1.2)
        r.cells[1].width = Inches(4.3)
        r.cells[2].width = Inches(0.75)

    for idx, (t_id, t_title, t_page) in enumerate(tables_list):
        row = lot_table.rows[idx]
        c0, c1, c2 = row.cells[0], row.cells[1], row.cells[2]
        c0.text = t_id
        c1.text = t_title
        c2.text = t_page
        
        p0, p1, p2 = c0.paragraphs[0], c1.paragraphs[0], c2.paragraphs[0]
        p2.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        for p in [p0, p1, p2]:
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(2)
            
        for run in p0.runs:
            set_run_font(run, name=FONT_NAME, size_pt=10, bold=True, color=COLOR_PRIMARY)
        for run in p1.runs:
            set_run_font(run, name=FONT_NAME, size_pt=10, bold=False, color=COLOR_TEXT)
        for run in p2.runs:
            set_run_font(run, name=FONT_NAME, size_pt=10, bold=False, color=COLOR_MUTED)

    doc.add_page_break()
