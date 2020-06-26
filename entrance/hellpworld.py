'''/*
 * @Author: LiuJun 
 * @Date: 2020-06-25 21:18:02 
 * @Last Modified by: LiuJun
 * @Last Modified time: 2020-06-25 21:21:16
 */
 '''
import datetime

print("hello world")
print("Go big or go home")
print("10.24(程序员之日)寓意：\n")
print("  低调，踏实，核心\n")
print(" 1024M=1G,谐音一级棒")

print("    丽江市新闻采编系统\n")
print("用户名：_______\n")
print("密码：_________\n")
print("验证码：_______ 3+5=?")

print("###################")
print("笑        飞")
print("书        雪\n")

print("_______________")
print("|  Python团队  |")
print("|  人人人人人  |")
print("_______________")

a = 100
b = 5

print("a =",a)

print(chr(65))
print(chr(56))
print(chr(91))
print("\u751f\u5316\u5371\u673a")
print("\u4e2d\u56fd")

fp = open(r'/Users/wangnan/PycharmProjects/entrance/mr.txt','a+')
print("要么出众，要么出局",file=fp)
fp.close()

print("当前年份： "+str(datetime.datetime.now().year))
print("当前日期时间： "+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

tip = input("输入文字")
print("tip is ",tip)
for x in tip:
    ors = ord(x)
    print(int(ors))
