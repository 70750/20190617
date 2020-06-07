#-*-coding:utf-8-*-
# 20200607
import scipy as sp
from matplotlib.pyplot import *
cashflows=[-200,80,90,100]
rate=[]
npv=[]
x=(0,0.7)
y=(0,0)

for i in range(1,70):
    rate.append(0.01*i)
    npv.append(sp.npv(0.01*i,cashflows))

    plot(rate,npv)
    plot(x,y)
    show()