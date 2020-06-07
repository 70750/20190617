#-*-coding:utf-8-*-

from yahoo_finance import Share
yahoo = Share('YHOO')
print yahoo.get_open()