import { db } from "./firebase";
import { collection, getDocs } from "firebase/firestore";

export const fetchWorkers = async () => {
  const querySnapshot = await getDocs(collection(db, "workers"));
  return querySnapshot.docs.map((doc) => ({ id: doc.id, ...doc.data() }));
};

export const fetchSensorData = async () => {
  const workerId = "test_worker"; // Replace with actual worker ID
  const response = await fetch(`/rpi-sensor-data?worker_id=${workerId}`);
  const data = await response.json();
  return data;
};