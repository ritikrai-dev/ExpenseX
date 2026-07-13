import "./footer.css";

export default function Footer() {

    return (

        <footer
            className="footer"
            id="contact"
        >

            <div className="footer-top">

                <div className="footer-contact">

                    <span className="section-tag">
                        Contact
                    </span>

                    <h2>
                        Let's Build Something Amazing
                    </h2>

                    <p>
                        Have a question, feedback, or collaboration
                        opportunity? Feel free to reach out.
                    </p>

                    <form className="contact-form">

                        <input
                            type="text"
                            placeholder="Your Name"
                        />

                        <input
                            type="email"
                            placeholder="Your Email"
                        />

                        <textarea
                            rows="6"
                            placeholder="Your Message"
                        ></textarea>

                        <button className="primary-btn">

                            Send Message

                        </button>

                    </form>

                </div>

                <div className="footer-links">

                    <div>

                        <h3>
                            Quick Links
                        </h3>

                        <a href="#home">Home</a>

                        <a href="#features">Features</a>

                        <a href="#about">About</a>

                        <a href="/auth">
                            Login
                        </a>

                    </div>

                    <div>

                        <h3>
                            Connect
                        </h3>

                        <a
                            href="https://github.com/ritikrai-dev"
                            target="_blank"
                        >
                            GitHub
                        </a>

                        <a
                            href="https://linkedin.com/in/ritikrai-dev"
                            target="_blank"
                        >
                            LinkedIn
                        </a>

                        <a
                            href="https://ritikrai-dev.github.io/portfolio/"
                            target="_blank"
                        >
                            Portfolio
                        </a>

                        <a href="mailto:cs.ritikrai@gmail.com">

                            Email

                        </a>

                    </div>

                </div>

            </div>

            <div className="footer-bottom">

                <div>

                    <h2>
                        ExpenseX
                    </h2>

                    <p>

                        AI Powered Expense Management

                    </p>

                </div>

                <p>

                    © 2026 ExpenseX • Made with ❤️ by Ritik Rai

                </p>

            </div>

        </footer>

    );

}