
import React, { useEffect, useState } from 'react';

export default function ForecastDashboard() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('/api/forecast')
      .then(res => res.json())
      .then(data => {
        setData([{
          id: 'item-001',
          name: data.item,
          currentStock: 23,
          forecastedDemand: data.forecast,
          alert: data.alert
        }]);
      });
  }, []);

  return (
    <div>
      <h1>Forecast Dashboard</h1>
      {data ? (
        <table>
          <thead>
            <tr>
              <th>Item</th>
              <th>Current Stock</th>
              <th>Forecasted Demand</th>
              <th>Alert</th>
            </tr>
          </thead>
          <tbody>
            {data.map(item => (
              <tr key={item.id}>
                <td>{item.name}</td>
                <td>{item.currentStock}</td>
                <td>{item.forecastedDemand}</td>
                <td className="alert">{item.alert}</td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p>Loading forecast...</p>
      )}
    </div>
  );
}
