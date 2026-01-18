# EMR – Emergency Medical Response System

Real-time emergency response platform connecting
Users, Ambulance Drivers, and Hospitals.

## Features
- User emergency creation
- Driver live tracking & hospital reservation
- Hospital dashboard with bed availability
- Real-time updates

## Tech Stack
- FastAPI
- HTML/CSS/JS
- Leaflet Maps

Demo Video
https://www.loom.com/share/517c3926c8dd4729bb103bd2e94a8cee

Running Instructions

Python 3.9+
Git
Any modern browser (Chrome / Edge)

🔹 1. Clone Repository
git clone https://github.com/yourusername/EMR-System.git
cd EMR-System

🔹 2. Backend Setup
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

🔹 3. Run Backend Server
uvicorn app:app --reload
✔ Server will start at:
http://127.0.0.1:8000

🔹 4. Frontend Setup
Open the following files directly in browser:
frontend/index.html    → User App
frontend/driver.html   → Ambulance Driver App
frontend/hospital.html → Hospital Admin Dashboard

🔹 5. Demo Flow
Open index.html → Create Emergency
Open driver.html → Accept Emergency
Reserve Hospital from Driver Dashboard
Open hospital.html → Update beds
