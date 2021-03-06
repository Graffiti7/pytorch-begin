import torch
import torch.nn as nn
import torch.nn.functional as F 
import matplotlib.pyplot as plt 
from IPython import display

x = torch.unsqueeze(torch.linspace(-1,1,100),dim = 1)

y = x.pow(2) + 0.2 * torch.rand(x.size()) 

class Net(nn.Module):
    def __init__(self,features_,hidden_,output_):
        super().__init__()
        self.hidden = nn.Linear(features_,hidden_)
        self.predict = nn.Linear(hidden_,output_)

    def forward(self,x):
        x = torch.relu(self.hidden(x))
        x = self.predict(x)
        return x 

net = Net(1,10,1)

plt.ion()

plt.show()

# 优化神经网络
optimizer = torch.optim.SGD(net.parameters(),lr = 0.5) #(参数，学习效率)
# 损失函数 MSLoss
criterion = nn.MSELoss()

for i in range(100):
    criterion  = net(x)
    loss = F.mse_loss(criterion,y)

    net.zero_grad() #梯度清零
    loss.backward() #反向传播
    optimizer.step()#更新参数

    if i % 5 ==0:
        plt.cla()
        plt.scatter(x,y)
        plt.plot(x,criterion.data.numpy(),"r-",lw = 5)
        plt.text(0.5,0,"Loss = %.4f"%loss)
        plt.pause(0.1)#每次显示图片的暂停时间
        display.clear_output(wait=True)#每次显示完图以后删除，达到显示动图的效果

plt.ioff()
plt.show()
