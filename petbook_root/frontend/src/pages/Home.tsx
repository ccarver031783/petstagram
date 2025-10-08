import './Home.css';

export default function Home() {
  return (
    <main className="home">
      <section className="hero">
        <h1>Welcome to PetBook</h1>
        <p>Your local playground for fullstack mastery.</p>
      </section>

      <section className="features">
        <h2>Features</h2>
        <ul>
          <li>React + Vite frontend</li>
          <li>Django backend</li>
          <li>KOPF orchestration</li>
        </ul>
      </section>

      <footer className="footer">
        <p>Built with 💙 and 🧠 by Chris</p>
      </footer>
    </main>
  );
}
