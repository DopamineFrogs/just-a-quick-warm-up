import time
from win10toast import ToastNotifier
import datetime
notif = ToastNotifier()
setTime = input("Enter the time (0 - 23): ")
message = input("What's this for?: ")
x = setTime.split(":")
def run():
    notif.show_toast("Time's up!", message, duration=7) 
def timer(hour, minute):
    while True:
        now = datetime.datetime.now()
        targetTime = datetime.datetime(now.year, now.month, now.day, hour, minute)
        if now >= targetTime:
            run()
            break
        else:
            timeWait = (targetTime - now).total_seconds()
            time.sleep(timeWait)
timer(int(x[0]),int(x[1]))
