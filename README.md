# Embedded-system-performance-monitor

A lightweight, real-time system performance monitoring application built with Python, Tkinter and Raspberry Pi Pico microcontroller. This application provides an intuitive GUI to monitor essential system metrics including CPU usage, RAM consumption, disk utilisation and network activity

![Screenshot 2024-06-28 000232](https://github.com/user-attachments/assets/2fa2e504-bf39-4d67-8509-4c9459aa1cc2)
![working system prototype](https://github.com/user-attachments/assets/ed5fee59-d838-4630-ba72-3da3f751a456)


## Features

- Real-time CPU usage monitoring
- RAM usage tracking
- Disk usage monitoring
- Network data usage display
- Clean, dark-themed GUI
- Cross-platform compatibility (Windows, macOS, Linux)

## Requirements

- Python 3.6+
- psutil library

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/pc-performance-monitor.git
cd pc-performance-monitor
```

2. Install dependencies:
```bash
pip install psutil
```

3. Run the application:
```bash
python Performance_monitor.py
```

Dependencies

- psutil - Cross-platform system and process utilities
- tkinter - GUI toolkit (included with Python)

Usage

- Execute the Python script
- A compact window will appear displaying real-time system metrics
- The interface updates automatically every second
- Close the window to exit the application
