import pandas as pd
import jqdatasdk as jq
from   jqdatasdk.technical_analysis import RSI
from jqfactor_analyzer.utils import get_forward_returns_columns
import tushare as ts
import backtrader as bt
import datetime

current_date = datetime.datetime.now().date().strftime('%Y%m%d')
#current_date=current_date.replace("-","")
print("当前日期：", current_date)




pro=ts.pro_api('79c8ef91769f1ffe520edbb0c8d303c34fa7cc9588bfe32f8c564931')

data=pro.daily(ts_code='000001.SZ',start_date='20220401',end_date='20220401')
#print(df)





class TushareData(bt.feeds.PandasData):
    params = (
        ('datetime', ),
        ('open', 1),
        ('high', 2),
        ('low', 3),
        ('close', 4),
        ('volume', 5),
        ('openinterest', None)
        )

data = TushareData(dataname=data)


class MovingAverageStrategy(bt.Strategy):
    params = (('pfast', 30), ('pslow', 100),)

    def __init__(self):
        sma1 = bt.ind.SMA(period=self.params.pfast)
        sma2 = bt.ind.SMA(period=self.params.pslow)
        self.crossover = bt.ind.CrossOver(sma1, sma2)

    def next(self):
        if not self.position:
            if self.crossover > 0:
                self.buy()
        elif self.crossover < 0 :
            self.close()


cerebro = bt.Cerebro()
cerebro.addstrategy(MovingAverageStrategy)


data_feed = bt.feeds.PandasData(dataname=data)
cerebro.adddata(data_feed)


cerebro.run()



