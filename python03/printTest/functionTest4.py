import datetime
import time

now = datetime.datetime.now()
print(now)
print("-----------------")

time.sleep(5)
print(now.year)
print(now.month)
print(now.day)
print(now.weekday())
print('월화수목금토일'[now.weekday()])
print(now.hour)
print(now.minute)
print(now.second)