#统计成绩
from pandas import Series, DataFrame
data = {'语文': [68, 95, 98, 90,80], '数学': [65, 76, 86, 88, 90], '英语': [30, 98, 88, 77, 90]}
df1 = DataFrame(data)
df2 = DataFrame(data, index=['张飞', '关羽', '刘备', '典韦', '许褚'], columns=['语文', '数学', '英语'])
print('平均成绩：',df2.mean())
print('最小成绩：',df2.min())
print('最大成绩：',df2.max())
print('方差：',df2.var())
print('标准差：',df2.std())
zongfen=df2.sum(1)
zongfen2= zongfen.sort_values(0, ascending=False)
print(zongfen2)