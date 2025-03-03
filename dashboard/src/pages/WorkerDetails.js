import React from "react";

const WorkerDetails = ({ worker }) => {
  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold">{worker.name}</h2>
      <p>Heart Rate: {worker.heart_rate} bpm</p>
      <p>Temperature: {worker.temperature}°C</p>
      <p>Risk Level: {worker.risk_level}</p>
    </div>
  );
};

export default WorkerDetails;