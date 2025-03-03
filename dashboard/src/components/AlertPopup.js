import React from "react";

const AlertPopup = ({ message, onClose }) => {
  return (
    <div className="fixed top-5 right-5 bg-red-500 text-white p-4 rounded shadow-lg">
      <p>{message}</p>
      <button className="mt-2 bg-white text-red-500 px-2 py-1 rounded" onClick={onClose}>Close</button>
    </div>
  );
};

export default AlertPopup;