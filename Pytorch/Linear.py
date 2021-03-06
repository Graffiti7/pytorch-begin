import torch 
import torch.nn as nn 
import matplotlib.pyplot as plt 
from torch.optim import SGD 
from IPython import display
import numpy as np

x = np.random.rand(256)

noise = np.random.randn(256) / 4

y = x * 5 + 7 + noise

y_ticks = np.linspace(0,15,10)

plt.ion()

plt.show()

model=nn.Linear(1, 1)
# 损失函数
criterion = nn.MSELoss()
# 随机梯度下降
optim = SGD(model.parameters(),lr = 0.01)
x_train = x.reshape(-1, 1).astype('float32')
y_train = y.reshape(-1, 1).astype('float32')

for i in range(30000000):
    input = torch.from_numpy(x_train)
    labels = torch.from_numpy(y_train)
    output = model(input)
    optim.zero_grad() #梯度清零
    loss = criterion(output, labels)
    loss.backward() #反向传播
    optim.step()#更新参数
    if (i%100==0):
        plt.clf()
        #每 100次打印一下损失函数，看看效果
        plt.scatter(x,y)
        plt.plot(x,output.data.numpy())
        plt.pause(0.1)
        print('epoch {}, loss {:1.4f}'.format(i,loss.data.item()))  

plt.ioff()
plt.show()