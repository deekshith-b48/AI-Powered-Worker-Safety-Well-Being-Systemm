import React, { useState, useEffect } from "react";
import Dashboard from "./pages/Dashboard";
import { fetchSensorData } from "./services/api";

function App() {
  const [sensorData, setSensorData] = useState(null);

  useEffect(() => {
    const getSensorData = async () => {
      const data = await fetchSensorData();
      setSensorData(data);
    };

    getSensorData();
  }, []);

  return (
    <div className="min-h-screen bg-gray-100 p-4">
      <Dashboard />
      {sensorData && (
        <div>
          <h2>Sensor Data</h2>
          <pre>{JSON.stringify(sensorData, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;