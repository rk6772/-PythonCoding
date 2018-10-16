import time
t=time.localtime()
print("local time is",t)
print("the ctime is",time.ctime())
later=time.time()+15
print("15 secs from now",time.ctime())
