import pandas  as pd 
from datetime import datetime
import backtrader as bt
import tushare as ts


def get_data():
    pro=ts.pro_api('79c8ef91769f1ffe520edbb0c8d303c34fa7cc9588bfe32f8c564931')
    data=pro.daily(ts_code='000001.SZ',start_date='20220401',end_date='20220410')
    #data.index=pd.to_datetime(data.trade_date)
    #data=ts.get_k_data(code='000001',start='2022-04-01',end='2022-04-10')
    print(data)
    data.columns=['code','date','open','high','low','close','pre_close','change','pct_chg','volome','amount']
    data.index=pd.to_datetime(data.date)
    data['openinterest']=0
    data=data[['open','high','low','close','volome','amount','openinterest']]
    return data


def get_indicator():
    pro=ts.pro_api('79c8ef91769f1ffe520edbb0c8d303c34fa7cc9588bfe32f8c564931')
    #df = pro.query('fina_indicator', ts_code='300750.SZ', start_date='20150101', fields='end_date,roa,roe')
    df = pro.query('fina_indicator', ts_code='600000.SH', start_date='20170101', end_date='20180801')
    print(df)


stock_df=get_data()
#indicator_df=get_indicator

#fromdate=datetime(2022,4,1)
#todate=datetime(2022,4,10)
#btdata=bt.feeds.PandasData(dataname=stock_df,fromdate=fromdate,todate=todate)

#print(indicator_df)

from progress.bar import Bar

bar=Bar("Processing ",max=20)
for i in range(20):
    bar.next()
bar.finish()