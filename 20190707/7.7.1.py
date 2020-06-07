#-*-coding:utf-8-*-
#7.7.1
import matplotlib.pyplot as plt
import numpy as np

A_EPS = (15.02,4.54,4.18,3.73)
B_EPS = (1.35,1.88,1.35,0.73)
ind = np.arange(len(A_EPS))
width = 0.2

fig,ax = plt.subplots()
A_std = B_std = (2,2,2,2)
rects1 = ax.bar(ind,A_EPS,width,color='yellow',yerr=A_std)
rects2 = ax.bar(ind+width,B_EPS,width,color='black',yerr=B_std)
ax.set_ylabel('EPS')
ax.set_xlabel('Year')
ax.set_title('Diluted EPS Excluding Extraordinary Items')
ax.set_xticks(ind+width)
ax.set_xticklabels(('2012','2011','2010','2009'))
ax.legend((rects1[0],rects2[0]),('W-Mart','Dell'))

def autolable(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2.,1.05*height,
                '%d'%int(height),ha='center',va='bottom')

autolable(rects1)
autolable(rects2)
plt.show()

