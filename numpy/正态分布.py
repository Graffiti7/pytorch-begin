import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(loc = 1.75,scale = 0.1,size = 10000000)

stock_change = np.random.normal(loc = 0,scale = 1,size = (8,10))

#数据切片索引
print(stock_change[0,0:3])

#形状修改(reshape,resize)
print(stock_change.shape)
stock_change.reshape(10,8) #原始数据没有变 返回新的ndarray
print(stock_change.shape)
stock_change.resize((10,8)) #原始数据没变 原ndarray形状改变
print(stock_change.shape)
stock_change.T     #转置 行变列 列变行 返回新的ndarray
print(stock_change.T.shape)
'''
plt.figure()
plt.hist(stock_change,1000)
plt.show()
'''