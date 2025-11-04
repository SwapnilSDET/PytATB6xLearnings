import time

print(time.time()) # 1762276438.6111355 Epoch & Unix time

print(time.sleep(5)) # None - halt the program execution for 5 sec

print(time.localtime()) # time.struct_time(tm_year=2025, tm_mon=11, tm_mday=4, tm_hour=23, tm_min=6, tm_sec=20, tm_wday=1, tm_yday=308, tm_isdst=0)
print(time.localtime().tm_hour) #23
print(time.localtime().tm_min) #6
print(time.localtime().tm_sec) #20


