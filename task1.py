import seaborn as sns #用于画图
from bs4 import BeautifulSoup #用于爬取arxiv的数据
import retest #用于正则表达式，匹配字符串的模式
import requests #用于网络连接，发送网络请求，使用域名获取对应信息
import json #读取数据，我们的数据为json格式的
import pandas as pd #数据处理，数据分析
import matplotlib.pyplot as plt #画图工具

# 读入数据
data = []

# 使用with语句优势：1.自动关闭文件句柄；2.自动显示（处理）文件读取数据异常
with open("arxiv-metadata-oai-2019.json", 'r') as f:
    for idx, line in enumerate(f):
        # 读取前100行，如果读取所有数据需要8G内存
        if idx >= 100:
            break
        data.append(json.loads(line))
data = pd.DataFrame(data)  # 将list变为dataframe格式，方便使用pandas进行分析
print(data.shape)  # 显示数据大小
data.head() #显示数据的前五行
plt.figure(figsize=(15,12))