from math import sqrt
from matplotlib import pyplot
import numpy as np
from pandas import DataFrame
from pandas import Series
from pandas import concat
from pandas import read_csv
from pandas import datetime
from sklearn.metrics import mean_squared_error
r=[]
m=[]
n=[]
e=[]
count=1
count1=1
dataset_name="CLOSING"
dataset_name1="closing"
for i in range(30):
    origin = read_csv('./LSTMSNPCell/'+dataset_name+'/origin/' + str(i+1) + '_'+dataset_name1+'.csv', delimiter=',',header=None).values
    predictions=read_csv('./LSTMSNPCell/'+dataset_name+'/prediction/' + str(i+1) + '_'+dataset_name1+'.csv', delimiter=',',header=None).values
    rmse = sqrt(mean_squared_error(origin, predictions))
    mse = mean_squared_error(origin, predictions)
    meanV = np.mean(origin)  # 对整个origin求取均值返回一个数
    dominator = np.linalg.norm(predictions - meanV, 2)
    nmse = mse / np.power(dominator, 2)
    error = abs(origin - predictions)
    r.append(rmse)
    m.append(mse)
    n.append(nmse)
    e.append(error)

    fig4 = pyplot.figure()
    ax41 = fig4.add_subplot(111)
    pyplot.xticks(fontsize=12)
    pyplot.yticks(fontsize=12)
    ax41.set_xlabel("Time", fontsize=12)
    ax41.set_ylabel("Magnitude", fontsize=12)
    pyplot.plot(origin, 'k-o', label='the original data')
    pyplot.plot(predictions, 'k+-', label='the predicted data')
    pyplot.legend()
    pyplot.title(dataset_name + "-use 60 datas as test")
    tt_name = "/home/dell/文档/liuqian/lasttest/Test2/LSTMSNPCell/" + dataset_name + '\\' + dataset_name + '{}.png'
    pyplot.savefig(tt_name.format(count))
    count = count + 1
    pyplot.show()
    # # 作图展示2
    fig1 = pyplot.figure()
    ax42 = fig1.add_subplot(111)
    pyplot.xticks(fontsize=15)
    pyplot.yticks(fontsize=15)
    ax42.set_xlabel("Time", fontsize=15)
    ax42.set_ylabel("Magnitude", fontsize=15)
    pyplot.plot(error, 'k-o', label='the original data-the predicted data')
    pyplot.legend()
    pyplot.title(dataset_name + "-use 60 datas error as test")
    tt_name = "/home/dell/文档/liuqian/lasttest/Test2/LSTMSNPCell/ERROR/" + dataset_name + '\\' + dataset_name + '{}.png'
    pyplot.savefig(tt_name.format(count1))
    count1 = count1 + 1
    pyplot.show()
R=np.var(r)
M=np.var(m)
N=np.var(n)

b1 = len(r)
b2 = len(m)
b3 = len(n)
sum1 = 0
sum2 = 0
sum3 = 0
for i in r:
    sum1 = sum1 +i
AVGR=(sum1/b1)
for i in m:
    sum2 = sum2 +i
AVGM=(sum2/b2)
for i in n:
    sum3 = sum3 +i
AVGN=(sum3/b3)


A=r.index(min(r))+1
print(r)
print (dataset_name+' Test RMSE: %.15f ,RMSE: %.15f ,RMSE: %.15f ' %(r[r.index(min(r))],m[r.index(min(r))],n[r.index(min(r))]))
print(A)
print(dataset_name+' Test RMSE: %.10f ± %.15f,RMSE: %.10f ± %.15f,RMSE: %.10f ± %.15f' %(AVGR,R,AVGM,M,AVGN,N))









