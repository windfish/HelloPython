#!/usr/bin/env python3
# -*- coding: utf-8 -*-


print('>>> datetime  -----------------')
from datetime import  datetime

now = datetime.now()
print(now, type(now))

# 指定日期和时间
dt = datetime(2020, 5, 22, 16, 00)
print(dt)

print('---------datetime 转换为 timestamp----------')
# 1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0，当前时间就是相对于epoch time的秒数，称为timestamp
# timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
# timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00 北京时间
# 可见timestamp 与时区无关
print(dt.timestamp())  # 将时间转为timestamp，浮点数，小数位表示毫秒数

print('---------timestamp 转换为 datetime----------')
print(datetime.fromtimestamp(1590134402.0))  # 转换为本地时间
print(datetime.utcfromtimestamp(1590134402.0))  # 转换为UTC 时间

print('---------str 转换为datetime----------')
print(datetime.strptime('2020-5-22 16:16:44', '%Y-%m-%d %H:%M:%S'))

print('---------datetime 转换为str----------')
print(now.strftime('%a, %Y-%m-%d %H:%M:%S'))

print('---------datetime 加减----------')
from datetime import timedelta

print(now)
print(now + timedelta(hours=5))
print(now + timedelta(minutes=10))
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=1))

print('---------时区转换----------')
# datetime 类型有一个时区属性tzinfo，默认是None
from datetime import timezone

tz_utc_8 = timezone(timedelta(hours=8))  # 创建时区
# 强制设置为UTC+8:00，如果系统时区不是UTC+8:00，不能强制设置
dt = now.replace(tzinfo=tz_utc_8)
print(dt)

# utcnow() 获得当前的UTC 时间，再转换为任意时区的时间
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# 转换时区为北京时间
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
# 转换时区为东京时间
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
# 北京时间转换为东京时间
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)


print('>>> collections  -----------------')





