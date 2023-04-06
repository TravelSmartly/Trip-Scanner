import androidhelper as android
import time
droid = android.Android()
def foo():
    start_time = time.time()
    droid.startLocating(minDistance=1000,minUpdateDistance=1)
    droid.eventWaitFor('location', int(9000))
    location = droid.readLocation().result
    data = bytes(str(location),'ascii')
    print(location)
    end_time = time.time()
    total_time = end_time - start_time
    print("Total time taken:", total_time, "seconds")

foo()

droid.stopLocating()