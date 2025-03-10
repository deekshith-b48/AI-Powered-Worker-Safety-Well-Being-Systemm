# 🛡️ AI-Powered Worker Safety & Well-Being System 🛠️

Welcome to the **AI-Powered Worker Safety & Well-Being System** repository! This project aims to leverage AI technology to enhance worker safety and well-being in various environments.

## 🚀 Features

- 🧠 AI-driven safety monitoring
- 📊 Real-time data analysis
- 🏭 Industrial safety applications
- 📈 Predictive analytics for well-being
- 📡 IoT integration

## 🛠️ Technologies Used

- 🐍 Python
- 📡 IoT Devices
- 🧠 Machine Learning Models
- ⚛️ React.js
- ☁️ Firebase

## 📂 Project Structure

```plaintext
AI-Powered-Worker-Safety-Well-Being-Systemm/
├── backend/               # Flask API for sensor processing & AI Risk Analysis
│   ├── app.py             # Main Flask server
│   ├── database.py        # Firebase integration
│   ├── ai_model.py        # AI-based risk analysis
│   ├── notifications.py   # SMS & email alert system
│   ├── requirements.txt   # Python dependencies
│
├── raspberry_pi/          # IoT device code (Raspberry Pi)
│   ├── main.py            # Collects & sends sensor data
│   ├── sensors/           
│   │   ├── fingerprint.py # Handles fingerprint authentication
│   │   ├── ultrasonic.py  # Distance detection
│   │   ├── pir.py         # Motion detection
│   │   ├── sound.py       # Distress call detection
│   │   ├── temperature.py # Environmental monitoring
│   ├── alerts.py          # Controls LEDs & Speaker alerts
│   ├── config.py          # WiFi & server connection settings
│
├── dashboard/             # React.js Web Dashboard
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   │   ├── Home.js    # Worker status dashboard
│   │   │   ├── Alerts.js  # Safety alerts & notifications
│   │   │   ├── Feedback.js# Worker stress feedback system
│   │   ├── App.js         # Main app structure
│   │   ├── api.js         # Fetches data from Flask backend
│   ├── public/
│   ├── package.json       # Frontend dependencies
│
├── cloud/                 # Cloud AI Processing & Firebase Database
│   ├── firebase_config.json # Firebase authentication settings
│   ├── ai_analysis.py     # Cloud-based AI model for risk detection
│   ├── functions/
│   │   ├── process_data.py # Processes incoming worker data
│   │   ├── send_alerts.py  # Triggers notifications
│
├── docs/                  # Documentation & Setup Guides
│   ├── INSTALL.md         # How to set up & deploy
│   ├── ARCHITECTURE.md    # System workflow explanation
│
├── README.md              # Project Overview & Instructions
```

## 👨‍💻 Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/deekshith-b48/AI-Powered-Worker-Safety-Well-Being-Systemm.git
   cd AI-Powered-Worker-Safety-Well-Being-Systemm
   ```

2. **Install backend dependencies:**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Run the backend server:**
   ```bash
   python app.py
   ```

4. **Navigate to the dashboard directory and install frontend dependencies:**
   ```bash
   cd ../dashboard
   npm install
   ```

5. **Run the React app:**
   ```bash
   npm start
   ```

## 🤝 Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any enhancements or bug fixes.

## 📄 License

This project is open-source and available under the MIT License.

## 📞 Contact

For any inquiries or support, please reach out to [deekshith-b48](https://github.com/deekshith-b48).
