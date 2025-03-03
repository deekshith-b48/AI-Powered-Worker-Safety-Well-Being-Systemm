import React from "react";

const WorkerCard = ({ worker }) => {
  return (
    <div className={`p-4 border rounded-lg ${worker.risk_level === "high" ? "bg-red-200" : "bg-green-200"}`}>
      <h2 className="text-xl font-bold">{worker.name}</h2>
      <p>Heart Rate: {worker.heart_rate} bpm</p>
      <p>Temperature: {worker.temperature}°C</p>
      <p>Risk Level: <strong>{worker.risk_level.toUpperCase()}</strong></p>
    </div>
  );
};

export default WorkerCard;