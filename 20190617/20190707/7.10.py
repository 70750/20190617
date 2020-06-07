#-*-coding:utf-8-*-

import mpl_finance as finance
import datetime
import matplotlib.mlab as mlab

ticker = 'IBM'
d1=datetime.date(2019,1,1)
d2=datetime.date(2019,5,1)
price=finance.fetch_historical_yahoo_ochl(ticker,d1,d2)
r=mlab.csv2rec(price)
price.close()
r.sort()




#date1=(2018,1,1)
#date2=(2018,12,31)
#price=fetch_historical_yahoo_ochl('IBM',date1,date2)
#print(price)