from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import random

app = FastAPI(title="EMR – Linker Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- DATA ----------------

emergency: Optional[dict] = None

drivers = {
    "DRV1": {"lat":13.0827,"lng":80.2707,"status":"available"},
    "DRV2": {"lat":13.0835,"lng":80.2695,"status":"available"},
    "DRV3": {"lat":13.0815,"lng":80.2715,"status":"available"},
}

hospitals = {
    "Apollo": {"lat":13.0810,"lng":80.2710,"beds":3,"icu":2,"cardio":True},
    "Govt GH": {"lat":13.0890,"lng":80.2665,"beds":5,"icu":1,"cardio":False}
}

# ---------------- API ----------------

@app.get("/")
def home():
    return {"status":"EMR Backend Running"}

# ---------------- USER ----------------
@app.post("/create_emergency")
def create_emergency(data:dict):
    global emergency
    emergency = {
        "lat": data["lat"],
        "lng": data["lng"],
        "status": "waiting",
        "driver": None,
        "hospital": None
    }
    return {"message":"Emergency Created","emergency":emergency}

# ---------------- DRIVER ----------------
@app.get("/emergency")
def get_emergency():
    if emergency is None:
        return {"message":"No active emergency"}
    return emergency

@app.post("/driver_accept")
def driver_accept(data:dict):
    global emergency

    if emergency is None:
        return {"error":"No emergency to accept"}

    driver = data["driver"]

    if driver not in drivers:
        return {"error":"Invalid driver ID"}

    drivers[driver]["status"] = "busy"
    emergency["status"] = "accepted"
    emergency["driver"] = driver

    return {"message":"Driver Accepted","driver":driver}

# ---------------- HOSPITAL ----------------
@app.post("/reserve_hospital")
def reserve_hospital(data:dict):
    global emergency

    if emergency is None:
        return {"error":"No active emergency"}

    hospital = data["hospital"]

    if hospital not in hospitals:
        return {"error":"Invalid hospital"}

    if hospitals[hospital]["beds"] <= 0:
        return {"error":"No beds available"}

    hospitals[hospital]["beds"] -= 1
    emergency["hospital"] = hospital
    emergency["status"] = "hospital_reserved"

    return {"message":"Hospital Reserved","hospital":hospital}

# ---------------- LIVE STATUS ----------------
@app.get("/status")
def status():
    # simulate driver movement
    for d in drivers:
        if drivers[d]["status"] == "busy":
            drivers[d]["lat"] += random.uniform(-0.0002,0.0002)
            drivers[d]["lng"] += random.uniform(-0.0002,0.0002)

    return {
        "emergency": emergency,
        "drivers": drivers,
        "hospitals": hospitals
    }
