// src/App.tsx
import Signup from './pages/Signup';
import './App.css'; // optional styling

function App() {
  return (
    <div className="app-container">
      <header className="app-header">
        <h1>Welcome to PetBook</h1>
        <p>Create your profile and introduce your pet to the world</p>
      </header>

      <main className="app-main">
        <Signup />
      </main>

      <footer className="app-footer">
        <p>&copy; 2025 PetBook. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default App;
