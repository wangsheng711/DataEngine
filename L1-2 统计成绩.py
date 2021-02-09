# Action2: 统计全班的成绩，班里有5名同学，现在需要你用Python来统计下这些人在语文、英语、数学中的平均成绩、最小成绩、最大成绩、方差、标准差。然后把这些人的总成绩排序，得出名次进行成绩输出（可以用numpy或pandas）
import pandas as pd
data = {'语文': [68,95,98,90,80], '数学': [65,76,86,88,90], '英语': [30,98,88,77,90]}
df = pd.DataFrame(data, index=['张飞', '关羽', '刘备', '典韦', '许褚'], columns=['语文', '数学', '英语'])
print(df)
print('平均成绩：','\n',df.mean())
print('最小成绩：','\n',df.min())
print('最大成绩：','\n',df.max())
print('方差：','\n',df.var())
print('标准差：','\n',df.std())
df = df.sum(1)
# sum(0)按列求和，sum(1)按行求和
# 或按行求和df = df.apply(lambda x: x.sum(), axis=1)
print(df.sort_values(0, ascending=False))
