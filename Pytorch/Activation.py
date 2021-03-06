import  matplotlib.pyplot as plt
import torch
import torch.nn.functional as F

data = torch.linspace(-100,100,100)

y_relu = torch.relu(data)

y_tanh = torch.tanh(data)

y_sigmoid = torch.sigmoid(data)

y_softmax = F.softplus(data)

figure,axes = plt.subplots(nrows=2,ncols=2,figsize=(20,8),dpi = 80)


axes[0][0].plot(data,y_relu,linestyle="-",color = "red",label = "relu")

axes[0][0].legend()

axes[0][1].plot(data,y_tanh,linestyle="-",color = "blue",label = "tanh")

axes[0][1].legend()

axes[1][0].plot(data,y_sigmoid,linestyle="-",color = "black",label = "sigmoid")

axes[1][0].legend()

axes[1][1].plot(data,y_softmax,linestyle="-",color = "green",label = "softmax")

axes[1][1].legend()


plt.show()