# import datetime

# print(datetime.datetime.now())
# print(datetime.date.today())
# print(datetime.datetime.now().time())

from datetime import datetime
from datetime import date

print(datetime.now())
print(date.today())
print(date.today().year)
print(date.today().month)
print(datetime.now().day)
print(datetime.now().time())

now = datetime.now()
print(now)
print(now.strftime("%d/%m/%Y %H:%M:%S"))
# formatted the time to the Euro Standard

print(now.strftime("%B %d, %Y %H:%M:%S"))

