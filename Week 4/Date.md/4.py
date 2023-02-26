import datetime
now = datetime.datetime.now()
then = datetime.datetime(2017, 2, 26, 14, 23, 43)
delta = now - then
print(delta.seconds)
