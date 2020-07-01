

list8 =[]
input=input("请输入两位数字年份")
print(input)
list8=list(input.split(","))

list8 = list(map(int, list8))

j=0

for i in list8:
    if (i>=30 and i<=99):
        list8[j] = list8[j]+1900
        j=j+1
    if (i<30 and i>=0):
        list8[j] = list8[j]+2000
        j=j+1
    if(i<0 or i>=100):
        print(list8[j],"不对，请输入两位数")
        j=j+1

list8.sort()
print(list8)

#print("list is ",list8)

    