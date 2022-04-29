
import pandas as pd
import plotly.io as pio
import plotly
import plotly.express as px
import plotly.graph_objects as go
from collections import Counter
import plotly.graph_objects as go


file_name = r'C:\Users\Administrator\Desktop\豆瓣数据.xlsx'
df = pd.read_excel(file_name)

df.rename(columns={'年代':'year'},inplace=True)


#统计每个年代上榜影片数量,并用plotly绘制柱状图
# n=df.groupby('year').count()
# x=list(n.index)
# y=list(n['评分'])
# fig = go.Figure()
# fig.add_trace(go.Bar(
#     x=x,
#     y=y,
# ))
# pio.write_image(fig, r'C:\Users\Administrator\Desktop\1.png')

# 这里需要标准化数据，使他们落在一个区间
# x=df.groupby('year')['评价人数','评分'].mean()
# s=(x-x.mean())/x.std()
# fig = px.line(s)
# fig.show()

#统计所有上榜电影类型
# types=df['电影类型'].str.split('/')
# l=[]
# tl=[]
# for i in range(500):
#     l.extend(types[i])
# for i in l:
#     tl.append(i.strip())
# c = Counter(tl)
# k=list(c.keys())
# v=list(c.values())
# count=pd.DataFrame({'type':k,'c':v})
# count.sort_values(by='c')
# total=count
# fig = px.pie(total, values='c', names='type')
# fig.show()

#每个年代电影类型占比的统计
