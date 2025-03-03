# Installation Guide

## 1️⃣ Prerequisites
- Python 3.8+
- Node.js 16+
- Raspberry Pi OS (for IoT components)
- Firebase Account (for cloud storage)

## 2️⃣ Steps to Install
```bash
# Clone the Repository
git clone https://github.com/your-repo/worker-safety-system.git
cd worker-safety-system

# Backend Setup
cd backend/
pip install -r requirements.txt
python app.py &

# Dashboard Setup
cd ../dashboard/
npm install
npm start
```

## 3️⃣ Final Setup
- Ensure all sensors and Raspberry Pi connections are properly configured.
- Access the dashboard from `http://localhost:3000`