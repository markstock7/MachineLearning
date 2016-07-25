# encoding: utf-8
from numpy import *
import kNN
import matplotlib
import matplotlib.pyplot as plt

fig = plt.figure()

ax = fig.add_subplot(111)
datingDataMat, datingLabels = kNN.file2matrix('datingTestSet.txt')

## 由于每个指标的范围不一致, 我们这里需要进行归一化特征值
normMat, ranges, minVals = kNN.autoNorm(datingDataMat)

ax.scatter(normMat[:, 1], normMat[:,2])

# 添加坐标轴的labels
plt.xlabel('Percentage of Time Spent Playing Video Games')
plt.ylabel('Liters of Ice Cream Consumed Per Week')

plt.show()

