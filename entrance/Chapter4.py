import keyword
print(keyword.kwlist)
我的名字 = "科学"
print(type(我的名字))
我的名字 = 505
print(type(我的名字))
no = 505

print(id(no))
print(id(我的名字))
h16 = 0x10
h8 = 0o100
print(h16)
print(h8)
print(0.1+0.2)
print((3+8j)-(2+9j))
print('''可以换行么？
是的，可以换''')
print("n' 也是字符串")
print('''
                  >学习编程，你不是一个人在战斗~~
                  |
                  |
        __\--________
II=====00[/*101______]
       __\_____\/-----.
    /___microsoft.com__\

      \oooooooooooooo/
      ~~~~~~~~~~~~~~~~




''')

print("失望之酒\n机会之杯")

print(r"失望之酒\n机会之杯")

x = 345+40

print(str(x))
print(repr(x))
print(eval(str(x)))
print(chr(x))
print(hex(x))

money_all = 45.6+34.7+87.90
money_all_str = str(money_all)
print("总价为： ",money_all_str)
money_real = int(money_all)
money_real_str = str(money_real)
print("实际金额为： ",money_real_str)

