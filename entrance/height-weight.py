# _*_ coding:utf-8 _*_

height = float(input("请输入您的身高： "))
weight = float(input("请输入您的体重： "))
bmi = weight/(height*height)

print("您的BMI指数为： "+str(bmi))

if bmi < 18.5:
    print("您的体重过轻！")
if bmi < 25 and bmi>=18.5:
    print("正常范围，请注意保持")
if bmi < 30 and bmi>=25:
    print("体重过重")
if bmi >=30:
    print("您很肥胖")

print("我一直认为我是一致🐌，我一直在爬，也许还没有爬到金字塔的塔尖"
"但是只要你在爬，就足以爬到顶端")