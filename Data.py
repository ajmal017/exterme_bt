import backtrader as bt
import os
import pandas as pd
from datetime import datetime
class CSV_Data():

    def __init__(self):

        modpath = os.path.dirname('C:\\TickDownloader\\tickdata\\')
        datapath = os.path.join(modpath, 'EURUSD_M5_UTC-5_00_noweekends.csv')

        # Create a Data Feed
        self.feed = bt.feeds.GenericCSVData(
            dataname=datapath, dtformat='%Y.%m.%d',
            tmformat='%H:%M',
            datetime=0,
            time=1,
            open=2,
            high=3,
            low=4,
            close=5,
            todate=datetime(2017,1,1),
            reverse=False,csv=False)

    def get_feed(self):
        return self.feed


class Pandas_Data():

    def __init__(self,holdout=False):

        modpath = os.path.dirname('C:\\TickDownloader\\tickdata\\')
        datapath = os.path.join(modpath, 'EURUSD_M5_UTC-5_00_noweekends.csv')


        dataframe = pd.read_csv(datapath,
                                parse_dates=False,
                                header=None)

        dataframe.columns = ['date','time','open','high','low','close','volume']

        dataframe['date'] = pd.to_datetime(dataframe['date']+' '+dataframe['time'])

        if not holdout:
            dataframe = dataframe[dataframe.date<datetime(2017,1,1)]

        self.dataframe = dataframe.set_index(['date'], drop=True)


    def get_feed(self,index=None):

        if index is None:
            index = range(self.dataframe.shape[0])
        # Create a Data Feed
        feed = bt.feeds.PandasData(
            dataname=self.dataframe.iloc[index],
            open=1,
            high=2,
            low=3,
            close=4,
        volume=5)

        feed.csv = False

        return feed



data = Pandas_Data()


