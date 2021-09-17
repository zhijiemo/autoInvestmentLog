# coding: utf-8
import akshare as ak
import os
import datetime
import time
import pytz
import pandas as pd
import configparser

localtime = datetime.datetime.now(tz=pytz.timezone('Asia/Shanghai')).strftime("%Y-%m-%d")
Outfilename="Data-"+str(localtime)+".txt"
config = configparser.ConfigParser()
filename = 'config.ini'
config.read(filename, encoding='utf-8')
report = str()
report +="个股：\r\n"
stocks_codes_str = config.get('stocks', 'codes')
stocks_codes_list = stocks_codes_str.replace(' ', '').split(',')
if not os.path.exists(localtime):
    os.mkdir(localtime)
try:
    df_Stock = ak.stock_zh_a_spot()
    df_Stock.to_excel(localtime + '/A_data.xlsx')
    for stock_code in stocks_codes_list:
    if stock_code == '':
        continue
    try:
        df_temp = df_stocks[df_stocks['代码'] .str.contains(stock_code)].reset_index(drop=True)
        name = df_temp['名称'][0]
        current_price = df_temp['最新价'][0]
        price_change = df_temp['涨跌额'][0]
        price_change_percent = df_temp['涨跌幅'][0]
        last_price = df_temp['昨收'][0]
        max_price = df_temp['最高'][0]
        min_price = df_temp['最低'][0]
        trade_volume = df_temp['成交量'][0]
        trade_amount = df_temp['成交额'][0]
        report += "{代码} {名称}  最新价 {current_price:.2f}, {vhdp}{price_change_percent:.2f}%\r\n"\
            .format(代码=stock_code, 名称=name, current_price=float(current_price)
                    , vhdp='上涨' if float(price_change_percent) >= 0 else '下跌', price_change_percent=abs(float(price_change_percent)))
    except:
        continue
# with open(Outfilename, 'w', encoding='utf-8') as f:
with open('todayData.txt', 'w', encoding='utf-8') as f:
    f.write(report)
except:
    pass

time.sleep(10)
