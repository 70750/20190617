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