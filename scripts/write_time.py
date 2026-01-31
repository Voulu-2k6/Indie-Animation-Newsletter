from datetime import datetime
from zoneinfo import ZoneInfo

now = datetime.now(ZoneInfo("America/Chicago"))

baseTime = now.isoformat()[11:16]
hour = int(baseTime[0:2])
am = 1
if(hour >= 12):
    hour -= 12
    am = 0

if(hour == 0):
    hour += 12

clockTime = f"{hour}:" + baseTime[3:]

with open("time.txt", "a") as f:
    f.write(f"{clockTime}")
    if(am == 1): f.write("am\n")
    else: f.write("pm\n")