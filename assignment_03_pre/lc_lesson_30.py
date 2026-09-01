import subprocess
# Clear screen on Windows
subprocess.run("cls", shell=True)

# ============================================================
# SETUP — Run this cell before anything else
# ============================================================
import csv        # reading and writing CSV files
import json       # reading and writing JSON files
import os         # file existence checks

NETWORK = {
    "7":  {"name":"Harbour Express", "stops":["Central Bus Stand","Fort","Harbour","Navy Nagar","Colaba"],            "base_fare":20.0,"is_ac":True, "capacity":60,"operator":"BEST"},
    "12": {"name":"Airport Shuttle", "stops":["Majestic","MG Road","Hebbal","Airport T1","Airport T2"],             "base_fare":35.0,"is_ac":True, "capacity":45,"operator":"KSRTC"},
    "31": {"name":"City Loop",       "stops":["KR Market","Shivajinagar","MG Road","Richmond","Jayanagar"],          "base_fare":12.0,"is_ac":False,"capacity":80,"operator":"BMTC"},
    "42": {"name":"North Connector", "stops":["Yeshwanthpur","Peenya","Tumkur Road","Nelamangala","Dobbaspet"],      "base_fare":18.0,"is_ac":False,"capacity":80,"operator":"BMTC"},
    "55": {"name":"South Express",   "stops":["Majestic","Jayanagar","JP Nagar","Bannerghatta Rd","Electronic City"],"base_fare":15.0,"is_ac":True, "capacity":60,"operator":"BMTC"},
    "88": {"name":"Tech Corridor",   "stops":["Silk Board","HSR Layout","Koramangala","Indiranagar","MG Road"],      "base_fare":22.0,"is_ac":True, "capacity":50,"operator":"KSRTC"},
}

TRIP_LOG = []

# Simulate a day of trips (reuse from Lesson 2)
raw_trips = [
    ("7",6,12),("7",7,54),("7",8,60),("7",9,58),("7",12,32),("7",17,55),("7",18,59),("7",21,18),
    ("12",5,8),("12",7,40),("12",8,44),("12",9,43),("12",13,20),("12",17,42),("12",18,45),("12",20,30),
    ("31",6,45),("31",7,78),("31",8,80),("31",9,75),("31",11,40),("31",14,35),("31",17,79),("31",19,72),
    ("42",6,30),("42",7,72),("42",8,78),("42",17,74),("42",18,76),("42",21,28),
    ("55",7,55),("55",8,58),("55",9,52),("55",17,56),("55",18,59),("55",20,35),
    ("88",7,48),("88",8,50),("88",9,49),("88",17,47),("88",18,50),("88",19,44),
]
for rid, hour, pax in raw_trips:
    info    = NETWORK[rid]
    is_peak = (7 <= hour <= 10) or (17 <= hour <= 20)
    fare    = round(pax * info["base_fare"] * (1.15 if is_peak else 1.0), 2)
    TRIP_LOG.append({"route_id":rid,"route_name":info["name"],"hour":hour,
                     "passengers":pax,"capacity":info["capacity"],
                     "fare_collected":fare,"is_peak":is_peak,"is_ac":info["is_ac"]})

print(f"✅ NETWORK: {len(NETWORK)} routes")
print(f"✅ TRIP_LOG: {len(TRIP_LOG)} trips")
print(TRIP_LOG[0].keys())

######################################
#--- 1. Write TRIP_LOG to a CSV file ---
######################################
#FIELDNAMES = ["route_name","route_id","hour","passengers",
#              "capacity","fare_collected","is_peak","is_ac"]
FIELDNAMES = ["route_name","route_id","hour","passengers",
              "capacity","fare_collected","is_peak"]
#FIELDNAMES = TRIP_LOG[0].keys()

with open("trips_semo_4.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=FIELDNAMES, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(TRIP_LOG)
print("✅ Written the trips_semo.csv file")
print(f'    File size: {os.path.getsize("trips_semo.csv")} bytes')
######################################
#--- 2. Read it back and inspect ---
######################################
def load_trips(filename="citysmart_trips.csv"):
    """
    Load trips from a CSV file and return as a list of dicts.
    Restores all types correctly — CSV gives strings for everything.

    Returns:
        list of trip dicts with correct Python types
    """
    trips = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            trips.append({
                "route_id"      : row["route_id"],              # stays str
                "route_name"    : row["route_name"],
                "hour"          : int(row["hour"]),      # cast to int
                "passengers"    : int(row["passengers"]),
                "capacity"      : int(row["capacity"]),
                "fare_collected": float(row["fare_collected"]),  # cast to float
                "is_peak"       : row["is_peak"] == "True",  # str→bool: compare to "True"
                "is_ac"         : row["is_ac"]   == "True",
            })
    return trips

loaded_trips = load_trips('trips_semo.csv')
print(f"\n✅ Loaded {len(loaded_trips)} trips from CSV")
print(f"   First row: {loaded_trips[0]}")
print(f"   Types:     hour={type(loaded_trips[0]["hour"])}, "
      f"fare={type(loaded_trips[0]["fare_collected"])}, "
      f"is_peak={type(loaded_trips[0]["is_peak"])}")
######################################
#--- 3. Write NETWORK to JSON ---
######################################
with open("lc_network_demo.json", "w") as f:
    json.dump(NETWORK, f, indent=2)

print("\n✅ Written lc_network_demo.json")
######################################
#--- 4. Read NETWORK back from JSON ---
######################################
with open("lc_network_demo.json", "r") as f:
    loaded_network = json.load(f)

print(f"✅ Loaded {len(loaded_network)} routes from JSON")
print(f"   Route 7 base_fare type: {type(loaded_network["7"]["base_fare"]).__name__}")
print(f"   ← JSON preserved the float type — no manual casting needed!")
######################################
#--- 5. Show raw file content (first 3 lines of CSV) ---
######################################
print("\n--- Raw CSV (first 3 lines) ---")
with open("trips_semo.csv", "r") as f:
    for i, line in enumerate(f):
        print(f"  {line.rstrip()}")
        if i == 2: break
######################################
#EXERCISE 3.1 — Save and reload CitySmart data (Mandatory)
######################################
FIELDNAMES = ["route_id","route_name","hour","passengers",
              "capacity","fare_collected","is_peak","is_ac"]
#--- TASK 1: Write save_trips() ---
def save_trips(trips, filename="citysmart_trips.csv"):
    """
    Save a list of trip dicts to a CSV file.

    Parameters:
        trips    : list of trip dicts (e.g. TRIP_LOG)
        filename : str — output file path

    Returns:
        int — number of trips written
    """
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()              # write the header row
        writer.writerows(trips)         # write all trip dicts at once
    return len(trips)
#--- TASK 2: Write load_trips() ---
def load_trips(filename="citysmart_trips.csv"):
    """
    Load trips from a CSV file and return as a list of dicts.
    Restores all types correctly — CSV gives strings for everything.

    Returns:
        list of trip dicts with correct Python types
    """
    trips = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            trips.append({
                "route_id"      : row["route_id"],              # stays str
                "route_name"    : row["route_name"],
                "hour"          : int(row["hour"]),      # cast to int
                "passengers"    : int(row["passengers"]),
                "capacity"      : int(row["capacity"]),
                "fare_collected": float(row["fare_collected"]),  # cast to float
                "is_peak"       : row["is_peak"] == "True",  # str→bool: compare to "True"
                "is_ac"         : row["is_ac"]   == "True",
            })
    return trips
#--- TASK 3: Round-trip test ---
n = save_trips(TRIP_LOG)
print(f"✅ Saved {n} trips to citysmart_trips.csv")

reloaded = load_trips()
print(f"✅ Loaded {len(reloaded)} trips from citysmart_trips.csv")

# Spot-check: compare first trip from memory vs loaded from file
original = TRIP_LOG[0]
from_file = reloaded[0]

print("\n=== Round-trip check — first trip ===")
print(f"  route_id      : original={original['route_id']!r}  loaded={from_file['route_id']!r}")
print(f"  passengers    : original={original['passengers']}  loaded={from_file['passengers']}  type={type(from_file['passengers']).__name__}")
print(f"  fare_collected: original={original['fare_collected']}  loaded={from_file['fare_collected']}  type={type(from_file['fare_collected']).__name__}")
print(f"  is_peak       : original={original['is_peak']}  loaded={from_file['is_peak']}  type={type(from_file['is_peak']).__name__}")

assert original["passengers"]     == from_file["passengers"],     "passengers mismatch!"
assert original["fare_collected"] == from_file["fare_collected"], "fare mismatch!"
assert original["is_peak"]        == from_file["is_peak"],        "is_peak mismatch!"
print("\n✅ All values match — round-trip successful!")