'''import datetime, time
while True:
    print(datetime.datetime.now())
    time.sleep(1)'''
'''import time
while True:
# seconds passed since epoch
    seconds = time.time()

# convert the time in seconds since the epoch to a readable format
    local_time = time.ctime(seconds)

    print("Local time:", local_time)
    time.sleep(1)'''
import time


def struct():
    global STime
    STime = time.localtime()


while True:
    struct()
    clock = time.strftime("%H:%M:%S", STime)
    print(clock, end='\r')
