'''
from datetime import date
today=date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.weekday())
print(today.isoweekday())
print(date(2025,12,30))


from datetime import time,date
print(date(2025,12,30))
print(time(23,16,23))

from datetime import time,date,datetime
now=datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.month)
print(now.second)

from datetime import time,date,datetime
now=datetime.now()
print(now.strftime('%y/%m/%d'))
print(now.strftime('%d/%m/%y'))
print(now.strftime('%d/%m/%y %H:%M:%S'))
print(now.strftime('%d/%m/%y %I:%M:%S'))
print(now.strftime('%A %d/%m/%y %I:%M:%S %p'))
print(now.strftime('%a %d/%m/%y %I:%M:%S %p'))
print(now.strftime('%a ,%d %B %y %I:%M:%S %p'))
print(now.strftime('%a , %d %b %y %I:%M:%S %p'))


from datetime import time,date,datetime,timedelta
today=date.today()
now=datetime.now()
after7=today+timedelta(days=7)
after7m=now+timedelta(minutes=7)
after7h=now-timedelta(hours=7)
print(after7,after7m,after7h)


import platform
print(platform.system())
print(platform.release())
print(platform.processor())
'''
import random
print(random.random())
print(random.randint(1,10))
print(random.uniform(1,10))

names=['vinaya','divya','akshitha','bindhu']
print(random.choice(names))
print(random.choices(names,k=3))
print("Before:",names)
random.shuffle(names)
print("After:",names)




