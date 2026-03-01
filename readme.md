# 🚀 Smart Cleaning Vehicle Simulator

## 📌 Project Overview

This project simulates a Smart Cleaning Vehicle using Python and Object-Oriented Programming (OOP).

It mimics real embedded hardware components such as:

- DC Motors
- Dust Sensor (GP2Y10 Simulation)
- Ultrasonic Sensor (HC-SR04 Simulation)
- Arduino-style control logic

The system automatically:
- Detects obstacles
- Measures dust levels
- Activates cleaning motors when required

---

## 🧠 System Architecture

The project follows modular OOP design:

- `Motor` → Simulates motor behavior
- `DustSensor` → Simulates dust detection
- `UltrasonicSensor` → Simulates obstacle detection
- `Vehicle` → Simulates movement
- `CleaningSystem` → Main controller (like Arduino brain)

---

## ⚙️ How It Works

1. Detect obstacle distance
2. If obstacle < 20 cm → Stop
3. Else move forward
4. Detect dust level
5. If dust > 50 → Activate vacuum & broom motors

---

## 🛠️ Technologies Used

- Python
- Object-Oriented Programming
- Git
- GitHub

---

## 🚀 Future Improvements

- Add CLI interactive control
- Convert into REST API using FastAPI
- Add database logging
- Add GUI version

---

## 👨‍💻 Author

Pawan Verma
