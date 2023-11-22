def NameConvert (x):
    if x == "WARRIOR":
        x = "Guard"
    elif x == "TANK":
        x = "Defender"
    elif x == "PIONEER":
        x = "Vanguard"
    elif x == "Crowd-Control":
        x = "Crowd Control"
    elif x == "Special":
        x = "Specialist"
    elif x == "Support":
        x = "Supporter"
    return x