import tushare as ts


class TsData():
## 获取股票列表
   def __init__(self):
      self.pro = ts.pro_api("5426ad82176097db40ef42f021474c04bc6b7ab57c520d8dcc4213b3")

   def get_basic_info(self):
      return self.pro.stock_basic()

   def get_daily(self,date):
      return self.pro.daily(trade_date=date)
