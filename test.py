
from datetime import datetime, time
import time
import ts as ts

now = datetime.now()

timestamp = datetime.timestamp(now)
print("timestamp =", timestamp)

ts = time.gmtime()
print(time.strftime("%Y-%m-%d", ts))