import "./Preview.css";

export default function Preview() {

    const features = [

        "Modern Dashboard",
        "AI Financial Insights",
        "Interactive Analytics",
        "Professional Reports",
        "Secure Authentication",
        "Fully Responsive"

    ];

    return (

        <section className="preview" id="preview">

            <div className="preview-content">

                <span className="section-badge">
                    Product Preview
                </span>

                <h2>
                    Experience ExpenseX
                </h2>

                <p>
                    Discover a modern finance management platform
                    designed to simplify tracking expenses,
                    understanding spending habits, and making
                    smarter financial decisions through powerful
                    analytics and AI.
                </p>

                <div className="preview-buttons">

                    <a
                        href="https://mini-project-rouge-gamma.vercel.app/"
                        target="_blank"
                        className="primary-btn"
                    >
                        Live Demo
                    </a>

                </div>

                <div className="preview-tags">

                    {

                        features.map((item)=>(

                            <span key={item}>

                                ✓ {item}

                            </span>

                        ))

                    }

                </div>

            </div>

            <div className="browser">

                <div className="browser-top">

                    <span></span>

                    <span></span>

                    <span></span>

                </div>

                <img

                    src="/dashboard-preview.png"

                    alt="ExpenseX Dashboard"

                />

            </div>

        </section>

    );

}