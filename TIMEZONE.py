



# from django.utils import timezone
# print(timezone.now())


from datetime import datetime,date

# 处理时区
import pytz


print(type(pytz.timezone("Asia/Shanghai")))

today = date.today() # 2019-5-26



d = datetime(year=today.year, month=today.month, day=today.day,
             hour=0, minute=0, second=0,
             tzinfo=pytz.timezone("Asia/Shanghai"))


print(d)

