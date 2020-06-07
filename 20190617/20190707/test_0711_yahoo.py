#-*-coding:utf-8-*-
from pandas_datareader import data as pdr

#import fix_yahoo_finance as yf

#yf.pdr_override()  # 需要调用这个函数

# 获取数据
data = pdr.get_data_yahoo( "SPY", start="2017-01-01", end="2017-04-30" )
data = pdr.get_data_yahoo( ["SPY", "IWM"], start="2017-01-01", end="2017-04-30" )

print(data)
