
import React, { useState } from 'react';
import './styles.css';
import Login from './components/Login';
import ForecastDashboard from './components/ForecastDashboard';

function App() {
  const [loggedIn, setLoggedIn] = useState(false);

  return (
    <div className="app">
      <img src="/logo.svg" alt="StockSage logo" className="logo" />
      {loggedIn ? (
        <ForecastDashboard />
      ) : (
        <Login onLogin={() => setLoggedIn(true)} />
      )}
    </div>
  );
}

export default App;
