import subprocess
# Clear screen on Windows
subprocess.run("cls", shell=True)
'''
NETWORK = {
    "7":  {"name":"Harbour Express", "stops":["Central Bus Stand","Fort","Harbour","Navy Nagar","Colaba"],            "base_fare":20.0,"is_ac":True, "capacity":60,"operator":"BEST"},
    "12": {"name":"Airport Shuttle", "stops":["Majestic","MG Road","Hebbal","Airport T1","Airport T2"],             "base_fare":35.0,"is_ac":True, "capacity":45,"operator":"KSRTC"},
    "31": {"name":"City Loop",       "stops":["KR Market","Shivajinagar","MG Road","Richmond","Jayanagar"],          "base_fare":12.0,"is_ac":False,"capacity":80,"operator":"BMTC"},
    "42": {"name":"North Connector", "stops":["Yeshwanthpur","Peenya","Tumkur Road","Nelamangala","Dobbaspet"],      "base_fare":18.0,"is_ac":False,"capacity":80,"operator":"BMTC"},
    "55": {"name":"South Express",   "stops":["Majestic","Jayanagar","JP Nagar","Bannerghatta Rd","Electronic City"],"base_fare":15.0,"is_ac":True, "capacity":60,"operator":"BMTC"},
    "88": {"name":"Tech Corridor",   "stops":["Silk Board","HSR Layout","Koramangala","Indiranagar","MG Road"],      "base_fare":22.0,"is_ac":True, "capacity":50,"operator":"KSRTC"},
}
# ============================================================
#--- 1. FileNotFoundError ---
# ============================================================
try:
    with open("no_such_file.csv", "r") as f:
        data = f.read()
except Exception as e:
    print(f'Caught exception: {e}')
    print(f' Filename was {e.filename}')
# ============================================================
#--- 2. ValueError during type casting ---
# ============================================================
print("\n=== 2. ValueError in CSV casting ===")
bad_row = {"route_id":"7", "passengers":"forty", "fare_collected":"18.50"}

try:
    passengers = int(bad_row["passengers"])
except ValueError as e:
    print(f'Caught value error: {e}')
    print(f'Bad value was {bad_row["passengers"]}')

# ============================================================
#--- 3. KeyError on missing route ---
# ============================================================
print("\n=== 3. KeyError on missing route ===")
try:
    info = NETWORK["99"]    # route 99 doesn't exist
except KeyError as e:
    print(f"  Caught KeyError: {e}")

# WIP
# https://colab.research.google.com/drive/1cBfNUD9dnl6HkyQhw94k99TadwQJOSbl#scrollTo=p1-ex-pre
# https://colab.research.google.com/drive/11yrmqLwKL_9ReOSZGrSdFo4HxhnkkRjG#scrollTo=p2dc-3.-keyerror-on-mis
'''
class_list = [
    ("  arjun  ", "82"), ("PRIYA", "95"), ("ravi kumar", "67"),
    ("Sneha", "88"),     ("  dev", "45"), ("Meena", "72"),
]
# Each tuple: (raw_name, score_as_string)

# ✏️ YOUR TURN

# 1. Clean names using a comprehension
#    Unpack each tuple: name, _ = ("  arjun  ", "82")
names_clean  = [name.strip().title() for name, age in class_list]

# 2. Convert scores to int using a comprehension
scores_clean = [int(score) for name, score in class_list]

# 3. Names of students who scored >= 80
top_students = [name for name, score in zip(names_clean, scores_clean) if score >= 80]

# 4. Average score — sum all and divide by count
avg = round(sum(scores_clean) / len(scores_clean), 1)

print("Clean names:  ", names_clean)
print("scores_clean:  ", scores_clean)
print("Top students: ", top_students)
print("Class average:", avg)