def decode_hero_profile(raw_profile):
    def convert(val):
        # boolean? ("1", "0", "true", "false")
        if val.lower() in ("1", "true"):
            return True
        if val.lower() in ("0", "false"):
            return False
        # int?
        if val.isdigit():
            return int(val)
        # float? (e.g., "78.2")
        try:
            return float(val)
        except ValueError:
            pass
        # fallback: keep original
        return val
    return {key: convert(val) for key, val in raw_profile.items()}

def calibrate_stone(raw_power, stability, guardian_bonus):
    effective_power = round((raw_power * stability) + guardian_bonus,2)
    if(effective_power >= 80):
        status = "OPTIMAL"
    elif(effective_power >= 50):
        status = "STABLE"
    else:
      status = "VULNERABLE"
    return((effective_power,status))

def decrypt_caesar(encrypted_message, shift):
    char_list = list(encrypted_message)
    d_list = [chr(ord(c)-shift) for c in char_list]
    return "".join(d_list)

def parse_stone_signature(signature):
    name, power, tag = signature.split("-")
    return (name, int(power), tag.title())

def classify_hero(name, health, power, is_compromised):
    if is_compromised:
        return "BENCHED"
    elif health > 50 and power > 60:
        return "DEPLOY"
    elif health > 30 and power > 40:
        return "BACKUP"
    else:
        return "BENCHED"

def analyze_waves(waves):
    #{"wave": 1, "sector": "A", "ships": 200,  "power_each": 5}
    total_threat = 0
    wave_count = 0
    max_threat = 0
    deadliest_wave = 0
    for wave in waves:
        if(int(wave['ships']) != 0):
            threat = int(wave['ships']) * int(wave['power_each'])
            total_threat += threat
            wave_count += 1
            if(max_threat < threat):
                max_threat = threat
                deadliest_wave = int(wave['wave'])
            else:
                pass
        else:
            pass
    return({"total_threat":total_threat, "wave_count": wave_count, "deadliest_wave":deadliest_wave})

def simulate_gauntlet(heroes_data, thanos_base_power):
    l_heroes_data = list(heroes_data.items())
    s_heroes_data = sorted(l_heroes_data, key=lambda x:x[1]['power'])
    thanos_power = thanos_base_power
    outcome = ""
    rounds = 0
    stones_taken = []
    blocked_by = "None"
    battle_log = []
    for gurdian in s_heroes_data:
        rounds += 1
        if(thanos_power <= gurdian[1]['power']):
            outcome = 'BLOCKED'
            blocked_by = gurdian[0]
            battle_log.append(blocked_by + 'blocked the Thanos')
            break
        else:
            thanos_power *= 2
            stones_taken.append(gurdian[1]["stone"])
            battle_log.append('Thanos captures the stone of ' + gurdian[0])
    if(rounds == len(heroes_data)):
        outcome = "SNAP"
    return({'outcome': outcome, 'rounds':rounds, 'stones_taken':stones_taken, 'blocked_by':blocked_by, 'battle_log':battle_log})
