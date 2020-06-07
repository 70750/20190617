#-*-coding:utf-8-*-
#print(ts.__version__)

import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import tushare as ts


sz=ts.get_hist_data('sz')
print(sz)

ts.get_profit_data(2014,3)

df =ts.get_hist_data('000938')
print(df)
print("&&&&&&&&&&&&&&&&&&7")

df1 =ts.get_hist_data('000938',ktype='W')
print(df1)
print("&&&&&&&&&&&&&&&&&&7")

sh=ts.get_hist_data('sh',ktype='M')
print(sh)

cl=ts.get_industry_classified()
print(cl)

sz=ts.get_sz50s()
print(sz)