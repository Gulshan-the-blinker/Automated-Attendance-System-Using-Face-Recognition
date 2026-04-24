# Automated Attendance System Using Face Recognition

## Overview
This project implements an automated attendance management system using face recognition and deep learning. The system detects and recognizes registered users through a webcam and records attendance automatically.

## Features
✔ Real-time face recognition  
✔ Automated attendance logging  
✔ Duplicate attendance prevention  
✔ CSV based record storage  
✔ DeepFace powered recognition  

---

## Tech Stack
- Python
- OpenCV
- DeepFace
- Pandas
- NumPy

---

## System Architecture
Webcam Input
↓
Face Detection
↓
Face Recognition
↓
Attendance Logging
↓
CSV Database

---

## Installation

```bash
pip install opencv-python
pip install pandas numpy
pip install deepface
pip install tf-keras
```

---

## Run Project

```bash
python main.py
```

Press:
- C → Capture and recognize
- Q → Quit

---

## Folder Structure

Attendance_System/
├── main.py
├── Attendance.csv
├── requirements.txt
└── faces/

---

## Sample Output

Name, Time, Date, Status  
GULSHAN, 10:15:22, 24-04-2026, Present

---

## Results
- Recognition Accuracy: ~98%
- Contactless Attendance
- Reduced Manual Errors

---

## Future Enhancements
- Anti-spoof detection
- Cloud database integration
- GUI dashboard
- Multi-user live detection

---

## Author
Gulshan Gautam  
M.Tech Information Technology  
IIEST Shibpur
