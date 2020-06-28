import random
verse = ["圣安东尼奥马刺","洛杉矶湖人","休斯顿火箭","金州勇士"]

print(verse[2])
print(verse[-1])

ba = [1,2,3,4,5,6,7,8,9,10]
ca = [11,12,13,14,15,16,17,18,19,20]
print(ba[1:5])
print(ba[0:5:2])      

print(ba+ca)
print(ba+verse)
print(ba*3)

emptylist = [None]*5
print(emptylist)

print("北京国安" not in verse)
print("序列的长度为： ",len(verse))
print("序列的长度为： ",len(ba))
print("序列 ：",ba,"中的最大值为：",max(ba) )
print("序列 ：",ca,"中的最小值为：",min(ca))
print(list(range(10,20,2)))
print(ca[3])
print(verse[1])
for index,item in enumerate(ba):
    print("ba[",index,"]", "is ",item)

ba.append(100)
print(ba+[200,300])

ba.extend(ca)
print(ba)
ba[2]=90
print(ba)
ba[3] = 456
print(ba)
del ba[3]
print(ba)
if ba.count(20)>0:
    ba.remove(20)
print(ba)
num = ba.count(11)
print(num)
print(ba.index(11))
total = sum(ba[2:5])
print(total)

grade = [94,56,87,90,34,86,45]
print("grade is ",grade)
grade.sort()
print("grade now is ",grade)

char =["asd","defk","sfr","jfpoew","DD"]
print("char is ",char)
print(id(char))
char.sort(key=str.lower)
print("char now is ",char)
print(id(char))

char1 =["asd","defk","sfr","jfpoew","DD"]
print("char1 is ",char1)
print(id(char1))
char2=sorted(char1,reverse= True)
print("char2 is ",char2)
print(id(char2))

randomnumber = [random.randint(10,100) for i in range(10)]
print(randomnumber)
newnum = [x*0.5 for x in randomnumber if x>50]
print(newnum)
print(25*44)

num1 = (34,45,43,23,21,56,76,45)
print(num1)
team=("马刺","湖人","公牛","网队")
untitle=("湖人",("ac米兰","尤文"),"罗马")
print(untitle)
str1 =("罗马")
print(str1)
tuple1 = ("罗马",)
print(tuple1)
print(type(tuple1))
emptytuple=()
print(emptytuple)

tuple2=tuple(range(10,20,2))
print(tuple2)
list2 = list(range(10,20,2))
print(list2)
print(tuple2[:3])
print(tuple2+tuple(list2))
tuple2= tuple(range(100,200,20))
print(tuple2)
tuple3 = (x for x in range(0,10))
print("tuple3.__next is ",tuple3.__next__())
print("tuple3.__next is ",tuple3.__next__())
print(tuple3)
print(tuple(tuple3))
list3=[x for x in range(0,10)]
print(list3)

num5=(i for i in range(23,34))
for i in num5:
    print(i,end=" ")
print(tuple(num5))













