import datetime

'''
input = input("请输入一个字符串")
for x in input:
    print(ord(x),end = " ")
print("\n")
'''
'''
input = input("请输入消费金额：")
#print(int(input))
print("付款金额为：",input)
print("支付成功，对方已经收款！")
'''
'''
print(datetime.date.today())
print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.now().strftime('%Y-%m-%d'))
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %A'))
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %A %B'))
'''
'''
day20 = datetime.datetime.strptime('2020-7-1 0:0:0','%Y-%m-%d %H:%M:%S')
#print(day20)
now = datetime.datetime.now()
delta = day20-now
day = delta.days
hour = int(delta.seconds/60/60)
minute = int((delta.seconds-hour*60*60)/60)
second = int(delta.seconds-hour*60*60-minute*60)

print('到2020年7月1日还有： '+str(day)+'天'+str(hour)+'小时'+str(minute)+'分'+str(second)+'秒')

print(now+datetime.timedelta(days=10))
print(now-datetime.timedelta(days=10))
print((now-datetime.timedelta(hours=100)))
print((now-datetime.timedelta(hours=100)).strftime('%Y-%m-%d '))
'''
'''
print(" 两全 美")
print("    乐 ")
print("    无 ")
print("    穷 ")
input = input("请输入所缺词语：")
print(" 两全\033[1;31m",input,"\033[0m 美")
print("    乐 ")
print("    无 ")
print("    穷 ")
'''
