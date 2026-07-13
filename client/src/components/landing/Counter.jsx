import { useEffect, useRef, useState } from "react";
import "./stats.css";

const stats = [
  {
    number: 25,
    suffix: "+",
    label: "Active Users",
    icon: "ti ti-users",
  },
  {
    number: 500,
    suffix: "+",
    label: "Transactions Processed",
    icon: "ti ti-receipt",
  },
  {
    number: 120,
    suffix: "+",
    label: "Reports Generated",
    icon: "ti ti-file-export",
  },
  {
    number: 99.9,
    suffix: "%",
    label: "System Uptime",
    icon: "ti ti-shield-check",
  },
];

function Counters({ end, suffix }) {
  const [count, setCount] = useState(0);
  const [started, setStarted] = useState(false);

  const ref = useRef();

useEffect(() => {
    const observer = new IntersectionObserver(
        ([entry]) => {

            if (entry.isIntersecting) {

                setStarted(true);

            } else {

                setStarted(false);

                setCount(0);

            }

        },
        {
            threshold: 0.4,
        }
    );

    if (ref.current) {

        observer.observe(ref.current);

    }

    return () => observer.disconnect();

}, []);

 useEffect(() => {

    if (!started) return;

    let current = 0;

    const increment = end / 80;

    const timer = setInterval(() => {

        current += increment;

        if (current >= end) {

            setCount(end);

            clearInterval(timer);

        } else {

            setCount(current);

        }

    }, 20);

    return () => clearInterval(timer);

}, [started, end]);

  return (
    <h2 ref={ref}>
      {Number.isInteger(end) ? Math.floor(count) : count.toFixed(1)}
      {suffix}
    </h2>
  );
}

export default function Counter() {
  return (
    <section className="stats-section">

      <div className="section-heading">

        <span className="section-tag">
          Our Growth
        </span>

        <h2>
          Trusted by Growing Users
        </h2>

        <p>
          ExpenseX is helping users manage their finances with
          powerful analytics, AI insights, and secure expense tracking.
        </p>

      </div>

      <div className="stats-grid">

        {stats.map((item) => (
          <div
            className="stats-card"
            key={item.label}
          >
            <div className="stats-icon">
              <i className={item.icon}></i>
            </div>

            <Counters
              end={item.number}
              suffix={item.suffix}
            />

            <p>{item.label}</p>

          </div>
        ))}

      </div>

    </section>
  );
}