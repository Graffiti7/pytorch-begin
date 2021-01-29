import numpy as np
import matplotlib.pyplot as plt
#生成01数组
z = np.zeros(shape = (3,4),dtype ="float32")
o = np.ones(shape = (3,4),dtype ="int32")
#深拷贝(copy,arragy)
nz = np.copy(z)
#浅拷贝
no = np.asarray(o)
#生成固定范围数组
np.linspace(0,10,100) #左闭右闭(begin,end,num)
np.arange(0,10,100) #左闭右开（begin,end,step)与range类似
#生成随机数组
np.random.randint(0,10,10)
#均匀分布
x = range(10)
y = np.random.uniform(-1,1,100000)
plt.figure()
plt.hist(y,1000,density=True)
plt.show()