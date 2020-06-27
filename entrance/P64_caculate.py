'''
print(3+5)
print(3-5)
print(3*5)
print(3/5)
print(3%5)
print(5%4)
print(3//5)
print(7//3)
print(2**3)
print(4**3)

a = 17
b = 15
c = 3
print("-------------")
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(b%c)
print(a//c)
print(b//c)
print(b**c)

print("%%%%%%%%%%%%%")
print("M"*10)
print("@"*10)
print(" "*10,"M"*5)
'''
'''
python = 92
english = 92
c = 89

sub = python - english
avg = (python+english+c)/3

print("python 和 english 和分数只差为：",sub,"分")
print("平均分为： ",avg,"分")

a = a+b
print(a)
a+=b
print("a+=b ",a)

a-=b
print("a-=b",a)
a*=b
print("a*=b",a)
print("a ",a,"c",c)
a//=c
print("a//c",a)

print("python = "+str(python)+" english="+str(english)+" c ="+str(c)+"\n")
print("python <english的结果是：",str(python<english))
print("python > english 的结果是： ",str(python > english))
print("english > c 的结果是： ",str(python>=c))
print("python<=english的结果是： ",str(python<=english))
'''
'''
print("\n手机店正在打折，活动进行中......")
strweek = input("请输入中文星期（如星期一）：")
intime = int(input("请输入小时（范围：0-23）："))

if(strweek=="星期二" and (intime>=10 and intime<=11)or\
    (strweek=="星期五" and (intime>=14 and intime<=16))):
    print("恭喜你，获得了折扣参与资格")
else:
    print("来晚了一步，期待下次活动")
'''
'''
print("12&8 is ",str(12&8))
print("4|8 is ",4|8)
print("31^22 is ",31^22)
print("~31 is ",~31)

print("48<<1 is ",48<<2)
print("48>>1 is ",48>>3)
print("-80>>1 is ",-80>>2)
'''
'''
print(int(0o244567))
print(int(0b101101001))
print(int(0xe3a5))
'''
'''
di = float(input("请输入底："))
zhishu = float(input("请输入指数："))
sum= di**zhishu
print(di,"的",zhishu,'次幂是：',sum)
'''
'''
huashi = float(input("请输入华氏温度： "))
sheshi = (huashi-32)*5/9
print("摄氏温度是： ",sheshi)
'''
qianshu = float(input("请输入加油的钱数： "))
gongli = float(input("请输入运行的公里数： "))
youhao = 8.1
print("您车辆的油耗为：",youhao,"每公里花费为： ",qianshu/gongli)
zonggongli=float(input("请输入车辆1年运行的总的公里数： "))
print("您的车辆一年的油费为： ",qianshu/gongli*zonggongli)






