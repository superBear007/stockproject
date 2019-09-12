import tushare as ts

pro = ts.pro_api("5426ad82176097db40ef42f021474c04bc6b7ab57c520d8dcc4213b3")

## 获取股票列表
def get_basic_info():
   return ts.get_stock_basics()
