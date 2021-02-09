# Action3: 对汽车质量数据进行统计
import pandas as pd

# 数据加载
df = pd.read_csv('./car_complain.csv')

# 数据预处理，拆分problem类型至多个字段，0代表无，1代表有，拆分problem列的问题，按逗号分隔
df = df.drop('problem',axis=1).join(df.problem.str.get_dummies(','))
# 数据清洗，别名合并
def f(x):
    x = x.replace('一汽-大众','一汽大众')
    return x
df['brand'] = df['brand'].apply(f)
tags = df.columns[7:]

# 计算每个车型投诉数量
result1 = df.groupby(['brand','car_model'])[tags].agg(['sum'])
# 按行求和
result1 = result1.sum(1)
print('每个车型投诉数量：','\n',result1)

# 计算各品牌平均车型投诉量并排序
result4 = pd.merge(result2,result3,left_index=True,right_index=True,how='outer')
result4 = result4['sum']/result4['car_model']
result4 = result4.sort_values(0, ascending=False).round(2)
print('各品牌平均车型投诉量：','\n',result4)
