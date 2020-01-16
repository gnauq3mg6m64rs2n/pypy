from datetime import datetime

ts = int(input())

print(datetime.utcfromtimestamp(ts).strftime("%H:%M:%S"))
