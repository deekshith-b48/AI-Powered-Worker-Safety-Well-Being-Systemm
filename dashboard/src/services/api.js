import { db } from "./firebase";
import { collection, getDocs } from "firebase/firestore";

export const fetchWorkers = async () => {
  const querySnapshot = await getDocs(collection(db, "workers"));
  return querySnapshot.docs.map((doc) => ({ id: doc.id, ...doc.data() }));
};