import React, { useEffect, useState } from "react";
import { fetchWorkers } from "../services/api";
import WorkerCard from "../components/WorkerCard";

const Dashboard = () => {
  const [workers, setWorkers] = useState([]);

  useEffect(() => {
    const getWorkers = async () => {
      const data = await fetchWorkers();
      setWorkers(data);
    };
    getWorkers();
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-3xl font-bold">Worker Safety Dashboard</h1>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mt-4">
        {workers.map((worker) => (
          <WorkerCard key={worker.id} worker={worker} />
        ))}
      </div>
    </div>
  );
};

export default Dashboard;