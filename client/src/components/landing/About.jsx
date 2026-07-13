import "./About.css";

export default function About() {
  return (
    <section className="about" id="about">

      <div className="about-content">

        <span className="section-badge">
          About ExpenseX
        </span>

        <h2>
          Smart Finance.
          <br />
          Simple Experience.
        </h2>

        <p>
          ExpenseX is a modern AI-powered expense management platform
          designed to simplify personal finance. Whether you're a
          student, freelancer, or professional, ExpenseX helps you
          monitor income, manage expenses, visualize spending trends,
          generate intelligent financial insights, and export
          professional reports—all from one secure and intuitive
          dashboard.
        </p>

        <p>
          ExpenseX
          focuses on delivering speed, security, and an exceptional
          user experience while helping users make smarter financial
          decisions.
        </p>

      </div>

      <div className="about-grid">

        <div className="about-card">
          <i className="ti ti-device-laptop"></i>
          <h3>Modern Interface</h3>
          <p>
            A clean, responsive dashboard designed for effortless
            financial management across all devices.
          </p>
        </div>

        <div className="about-card">
          <i className="ti ti-brain"></i>
          <h3>AI Powered</h3>
          <p>
            Get personalized financial recommendations generated
            from your spending behavior using AI.
          </p>
        </div>

        <div className="about-card">
          <i className="ti ti-lock"></i>
          <h3>Secure Platform</h3>
          <p>
            JWT authentication and secure APIs keep your personal
            financial data protected.
          </p>
        </div>

        <div className="about-card">
          <i className="ti ti-chart-pie"></i>
          <h3>Powerful Analytics</h3>
          <p>
            Understand your finances with interactive charts,
            summaries, and exportable reports.
          </p>
        </div>

      </div>

    </section>
  );
}