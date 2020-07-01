
thisweek = [4235,10111,8447,9677,2345,3456,9873]
lastweek = [2345,4567,8745,3456,2365,10111,3455]
week = ["星期日","星期一","星期二","星期三","星期四","星期五","星期六"]
index3 =0

for index1,value1 in enumerate(thisweek):
    print(index1,value1)
    thisweek[index1]+=lastweek[index1]
            

print(thisweek)
thisweek.sort()
print(thisweek)

weekmax=0
weekmin=10000000

print("lstweek is ",lastweek)
for index2,value2 in enumerate(lastweek):
    if lastweek[index2]>weekmax:
        weekmax=lastweek[index2]
        indexmax=index2
    if lastweek[index2]<weekmin:
        weekmin=lastweek[index2]
        indexmin=index2

print("max index is ",week[indexmax],"max is ",lastweek[indexmax])

print("min index is ",week[indexmin],"min is ",lastweek[indexmin])