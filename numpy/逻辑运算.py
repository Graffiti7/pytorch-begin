import numpy as np

stock_change = np.random.normal(0,1,(8,10))

#条件判断
stock_change > 0.5

#布尔索引
stock_change[stock_change > 0.5]

#通用判断函数
np.all((stock_change[0:2,0:5] > 0.5) | (stock_change[0:2,0:5] < 0.5))  #只有stock_change[0:2,0:5] > 0.5 全为True 返回值为True; 只要有一个False 返回值为False

np.any(stock_change[0:2,0:5] > 0.5)  #只有stock_change[0:2,0:5] > 0.5  全为False 返回值为False; 只要有一个True 返回值为True

#三元运算符(判断，True赋值，Fasle赋值)
np.where(np.logical_and(stock_change > 0.5,stock_change < 1),1,0)

#逻辑运算

np.logical_and(stock_change > 0.5,stock_change < 1)
np.logical_or(stock_change > 0.5 , stock_change < -0.5)


#统计运算
stock_change.max(axis = 0) #按列取最大值
np.max(stock_change,axis = 1)#按行取最大值
np.argmax(stock_change,axis = 1)   #最大值位置