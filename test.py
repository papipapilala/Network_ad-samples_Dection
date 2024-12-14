import pandas as pd
import re
# def finalldata(data_orginal, data_show):
#     for i in range(len(data_orginal)):
#         for j in range(len(data_show)):
#
#             if data_orginal['data'][i][2:-1] == data_show['data'][j][2:-1]:
#                 print("yes",i)
#                 data_orginal['label'][i] = data_show['label'][j]
#                 data_orginal['classes'][i] = data_show['classes'][j]
#
#     return data_orginal

data_orginal = pd.read_csv(r"save.csv", encoding='gbk', parse_dates=True)
data_show = pd.read_csv(r"./data/shown.csv", encoding='gbk', parse_dates=True)
# 假设 'data' 列包含字符串，需要去掉其中的反斜杠
data_show['data'] = data_show['data'].str.replace("\\", "", regex=False)
data_orginal['label'] = 0
data_orginal['classes']=0
# data_orginal=finalldata(data_orginal,data_show)

for i in range(20):
    for j in range(20):
        # data_show['data'][i][:]=data_show['data'][i][:].replace("\\","")
        print(data_orginal['data'][i][2:-1])
        print(data_show['data'][j][2:-1])
        print("-----------------------------")