# _*_ coding:utf-8 _*_

import datetime

imyear = input("请输入您的出生年月：")
nowyear = datetime.datetime.now().year
age = nowyear-int(imyear)
print("现在的年龄为： ",age)

if age < 18:
    print("您现在是少年")
if age >=18:
    print("您现在是成年人")
if age>=60:
    print("您现在是老年人")
if age >= 120:
    print("您是妖精")
