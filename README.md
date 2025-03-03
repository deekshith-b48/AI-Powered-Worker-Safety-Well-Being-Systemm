## README - AI-Powered Worker Safety & Well-Being System

### Overview
This system ensures worker safety using IoT sensors, real-time monitoring, and AI-based analytics. It detects hazardous conditions, worker distress, and environmental factors to prevent accidents and improve well-being.

### Features
- **Fingerprint Authentication**: Ensures authorized worker access.
- **Distance Detection**: Monitors proximity to restricted zones.
- **Motion Detection**: Identifies unusual worker activity.
- **Sound Detection**: Recognizes distress calls.
- **Temperature Monitoring**: Prevents heat-related hazards.
- **Real-time Alerts**: Triggers alarms via LED and speakers.
- **Cloud Integration**: Sends data for real-time analysis.

### Folder Structure
```
raspberry_pi/
│   ├── main.py  # Collects & sends sensor data
│   ├── sensors/
│   │   ├── fingerprint.py  # Handles fingerprint authentication
│   │   ├── ultrasonic.py  # Distance detection
│   │   ├── pir.py  # Motion detection
│   │   ├── sound.py  # Distress call detection
│   │   ├── temperature.py  # Environmental monitoring
│   ├── alerts.py  # Controls LEDs & Speaker alerts
│   ├── config.py  # WiFi & server connection settings
```

### Installation
1. **Set up Raspberry Pi**
   - Install Raspberry Pi OS.
   - Enable SPI & I2C interfaces.
2. **Install Dependencies**
   ```sh
   pip install requests
   ```
3. **Configure Server URL**
   - Update `config.py` with your server IP.
4. **Run the System**
   ```sh
   python3 main.py
   ```

### Usage
- The system continuously monitors the environment and sends alerts when necessary.
- Data is sent to the cloud for real-time tracking.
- Supervisors receive alerts on worker safety concerns.

### Contributing
- Fork the repository
- Make improvements
- Submit a pull request

### License
This project is licensed under MIT License.
# AI-Powered-Worker-Safety-Well-Being-System
