from stockproject.config_settings import *
import tushare as ts
from stockproject.getDataFromTushare import TsData


def stockBasic():

    pass


data = TsData()
print(data.get_basic_info())