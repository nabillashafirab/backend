def ClassNameConvert (x):
    if x == "WARRIOR":
        x = "Guard"
    elif x == "TANK":
        x = "Defender"
    elif x == "PIONEER":
        x = "Vanguard"
    elif x == "SPECIAL":
        x = "Specialist"
    elif x == "SUPPORT":
        x = "Supporter"
    else :
        x = x.capitalize()
    return x

def TagConvert (x):
    if x == "Crowd-Control":
        x = "Crowd Control"
    return x