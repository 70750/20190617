#-*-coding:utf-8-*-

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

year=[2009,2010,2011,2012,2013]

ret_A=np.array([0.102,-0.02,0.213,0.12,0.13])
ret_B=np.array([0.1062,0.23,0.045,0.234,0.113])
port_EW=(ret_A+ret_B)/2
result=round(np.mean(ret_A),3),round(np.mean(ret_B),3),round(np.mean(port_EW),3)
print(result)
result1=round(np.std(ret_A),3),round(np.std(ret_B),3),round(np.std(port_EW),3)
print(result1)

plt.figtext(0.2,0.65,"Stock Ahhh")
plt.figtext(0.15,0.45,"Stock Bjjjj")
plt.xlabel("Year")
plt.ylabel("Returns")
plt.plot(year,ret_A,lw=2)
plt.plot(year,ret_B,lw=2)
plt.plot(year,port_EW,lw=2)
plt.title("Individal stocks vs. an equal-weighted 2-stock portflio")
plt.annotate('Equal-weighted Portfolio',xy=(2013,0.1),
             xytext=(2009.,0),arrowprops=dict(facecolor='red',shrink=0.05),)
plt.ylim(-0.1,0.3)
plt.show()

result3=sp.corrcoef(ret_A,ret_B)
print(result3)