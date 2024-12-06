# DormKit

## Overview
DormKit is a prototype “smart dorm” system designed to allow users to control various electronics within their dormitory from anywhere on the UVM campus. Inspired by Apple’s “HomeKit,” DormKit leverages a combination of a Flask web application, a Raspberry Pi, and an Arduino Uno to provide seamless control over dormitory devices such as doors and lighting systems.

## Features
- Remote Control: Lock/unlock doors and turn lights on/off via a web interface.
- Real-Time Feedback: Displays current states of devices and environmental data.
- Integrated Hub: A dedicated hub interface running on a Raspberry Pi for local control and monitoring.
- Weather Integration: Fetches and displays real-time weather information.
- Expandable Architecture: Easily add more devices and functionalities as needed.

## Directory Structure
```
DormKit/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   │   ├── js/
│   │   │   └── buttons.js
│   │   └── images/
│   │       ├── button.png
│   │       ├── door.png
│   │       ├── font.ttf
│   │       ├── light.png
│   │       ├── off.png
│   │       └── on.png
│   └── templates/
│       └── buttons.html
├── hardware/
│   ├── HC_05.py
│   ├── HC-05.ino
│   └── states.txt
├── hub/
│   ├── hub.py
│   └── textures/
│       ├── button.png
│       ├── door.png
│       ├── font.ttf
│       ├── light.png
│       ├── off.png
│       └── on.png
├── scripts/
│   ├── main.py
│   └── main.sh
├── config/
│   └── config.py
├── tests/
│   └── test_hardware.py
├── .gitignore
├── README.md
├── requirements.txt
└── LICENSE
```

### Key Directories and Files
- app/: Contains the Flask web application.
    - static/: Holds static assets like CSS, JavaScript, and images.
    - templates/: HTML templates for rendering web pages.
- hardware/: Scripts and configurations for hardware interactions.
    - HC_05.py: Manages Bluetooth communication with the HC-05 module.
    - HC-05.ino: Arduino sketch for handling Bluetooth commands.
- hub/: The hub application that provides a local interface and monitors system states.
    - hub.py: Main script for the hub interface.
- scripts/: Utility scripts to run and manage the application.
    - main.py: Entry point script.
    - main.sh: Shell script to launch multiple processes concurrently.
- config/: Configuration files.
    - config.py: Central configuration settings for the application.
- tests/: Automated tests to ensure code reliability.
    - test_hardware.py: Tests for hardware interaction modules.
- requirements.txt: Lists all Python dependencies required to run the application.

## Installation
### Prerequisites
- Hardware:
    - Raspberry Pi (with Raspbian OS installed)
    - Arduino Uno
    - HC-05 Bluetooth Module
    - 5-inch HDMI LCD (e.g., from Waveshare)
    - Necessary wiring and power supplies
- Software:
    - Python 3.10.2 or higher
    - Arduino IDE
    - Flask framework

### Setup Steps
**1**. Clone the Repository**
```bash
git clone https://github.com/aaronperkel/DormKit.git
cd DormKit
```

**2. Install Python Dependencies**

It’s recommended to use a virtual environment.
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**3. Configure the HC-05 Bluetooth Module**

Ensure the HC-05 is properly connected to the Raspberry Pi and paired.
```bash
sudo rfcomm bind 2 98:D3:61:F7:14:36
```

**4. Arduino Setup**
- Open the HC-05.ino file in the Arduino IDE.
- Upload the sketch to your Arduino Uno.

**5. LCD Screen Setup**
- Follow the Waveshare LCD Setup Guide to configure the LCD with your Raspberry Pi.

**6.Configure Environment Variables**
- Create a `.env` file in the `config/` directory if needed.
- Add necessary environment variables such as API keys.

## Usage
**1. Start the Application**

Navigate to the `scripts/` directory and run the main script.
```bash
cd scripts/
bash main.sh
```
This will launch both the Flask web server and the hub interface concurrently.

**2. Accessing the Web Interface**

Open a web browser and navigate to `http://<Raspberry_Pi_IP_Address>/` to access the DormKit web interface.

**3. Using the Hub Interface**

The hub interface will display on the connected LCD screen, showing device states, weather information, and providing local controls.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.