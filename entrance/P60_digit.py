'''
while True:
    number = input("输入数字： ")
    print(int(number,))
'''
'''
number = int(input("请输入一个十进制数字： "))
two = bin(number)[2:]
eight = oct(number)[2:]
sixteene = hex(number)[2:]
print(number,"的二进制是： ",two,",八进制是： ",eight,",十六进制是： ",sixteene)
'''
'''
gongji = input("请输入攻击值： ")
fangyu = input("请输入防御值： ")
wuli = input("请输入武力值： ")
tongshuai = input("请输入统帅值： ")
sudu = input("请输入速度值： ")
zhili = input("请输入智力值： ")

print("攻击：",gongji,"      ","*"*int((int(gongji)/10)))
print("防御：",fangyu,"      ","*"*int((int(fangyu)/10)))
print("武力：",wuli,"      ","*"*int((int(wuli)/10)))
print("统帅：",tongshuai,"      ","*"*int((int(tongshuai)/10)))
print("速度：",sudu,"      ","*"*int((int(sudu)/10)))
print("智力：",zhili,"      ","*"*int((int(zhili)/10)))
'''
'''
stone = 1
siccer = 2
bu = 3

one = int(input("第一个玩家输入："))
two = int(input("第二个玩家输入："))
print("第一个玩家输入：",one,"第二个玩家输入： ",two,)

if one>3 or two>3:
    print("输入不合法，请重新输入，每个玩家只能输入1-3")

if one == 1:
    if two ==  1:
        print("两个玩家打平")
    if two == 2:
        print("玩家1获胜")
    if two == 3:
        print("玩家2获胜")
if one == 2:
    if two == 2:
        print("两个玩家打平")
    if two == 3:
        print("玩家1获胜")
    if two == 1:
        print("玩家2获胜")
if one == 3:
    if two == 3:
        print("两个玩家打平")
    if two == 1:
        print("玩家1获胜")
    if two == 2:
        print("玩家2获胜")
'''

'''
sum = 0.0
input=input("请输入摇一摇：")
for x in input:
    ran=float(int(ord(x))/100)
    sum=float(sum)+ran

if sum>0.2:
    print("用户奖励：",sum,"元")
if sum<=0.2 and sum>0:
    print("用户奖励：全免费")
'''
print('''
                尤文图斯          曼联
    53%          ***** 控球率    ****        47%
    17              ** 任意球    **          15
    3                * 射正      *           3
    11              ** 射偏      *           2




''')

