from sklearn.cluster import KMeans
from sklearn import preprocessing as pre
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from kneed import DataGenerator, KneeLocator
from scipy.cluster.hierarchy import dendrogram, ward
from sklearn.cluster import AgglomerativeClustering
from pylab import *

#图表中文显示
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

#数据预处理，0-1规范化
def pre_process(source_data):
    train_x=source_data[['人均GDP','城镇人口比重','交通工具消费价格指数','百户拥有汽车量']]
    # 规范化到 [0,1] 空间
    min_max_scaler=pre.MinMaxScaler()
    train_x=min_max_scaler.fit_transform(train_x)
    return train_x

# K-Means 手肘法：统计不同K取值的误差平方和,获取分组数量
def SSE(train_x):
    sse = []
    for k in range(1, 20):
    	# kmeans算法
    	kmeans = KMeans(n_clusters=k)
    	kmeans.fit(train_x)
    	# 计算inertia簇内误差平方和
    	sse.append(kmeans.inertia_)
    x = range(1, 20)
    kneedle = KneeLocator(x, sse, S=1.0, curve='convex', direction='decreasing') #自动获取拐点，
                                                                                    #S：float型，默认为1，敏感度参数，越小对应拐点被检测出得越快
                                                                                    #curve：str型，指明曲线之上区域是凸集还是凹集，concave代表凹，convex代表凸
                                                                                    #direction：str型，指明曲线初始趋势是增还是减，increasing表示增，decreasing表示减
    plt.xlabel('K')
    plt.ylabel('SSE')
    plt.plot(x, sse, 'o-')
    plt.show()
    return kneedle.knee

#使用K_MEANS聚类
def k_means(train_x,cluster_num,source_data):
    kmeans = KMeans(n_clusters=cluster_num)
    kmeans.fit(train_x)
    predict_y = kmeans.predict(train_x)
    # 合并聚类结果，插入到原数据中
    result_KMEANS = pd.concat((source_data,pd.DataFrame(predict_y)),axis=1)#将聚类结果加入原始表
    result_KMEANS.rename({0:u'聚类结果'},axis=1,inplace=True)
    result_KMEANS=result_KMEANS.sort_values('聚类结果') #对聚类结果进行排序
    print('-'*30,'KMEANS聚类结果','-'*30)
    print(result_KMEANS)

#层次聚类
def Hierarchical(train_x,cluster_num,source_data):
    model = AgglomerativeClustering(linkage='ward', n_clusters=cluster_num)
    y = model.fit_predict(train_x)
    result_hierarchical=pd.concat((source_data,pd.DataFrame(y)),axis=1)#将聚类结果加入原始表
    result_hierarchical.rename({0:u'层次聚类结果'},axis=1,inplace=True)
    linkage_matrix = ward(train_x)
    dendrogram(linkage_matrix,labels=list(result_hierarchical["地区"]))
    result_hierarchical=result_hierarchical.sort_values('层次聚类结果')#对聚类结果进行排序
    print('-'*30,'层级聚类结果','-'*30)
    print(result_hierarchical)
    plt.show() #层次聚类可视化

source_data=pd.read_csv('car_data.csv',encoding='gbk')
train_x=pre_process(source_data) #调用数据0-1规范化
cluster_num=SSE(train_x) #调用手肘法，输出拐点
predict_y=k_means(train_x,cluster_num,source_data) #调用KMEAN算法，输出分类后数据集
Hierarchical(train_x,cluster_num,source_data) #调用层次聚类，输出数据集和可视化
