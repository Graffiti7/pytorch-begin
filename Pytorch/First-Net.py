import torch
import torch.nn as nn
import torch.nn.functional as F
 
#构建一个小的CNN
 
class Net(nn.Module):
 
    #此初始化函数定义了神经网络的基本架构
    def __init__(self):
        #使用Net的父类的初始化方法，即先运行nn.Module的初始化函数
        super(Net,self).__init__()
        #1 个输入通道，6个输出通道，5*5的卷积核
        #定义class torch.nn.Conv2d(in_channels, out_channels, kernel_size, stride=1, padding=0, dilation=1, groups=1, bias=True)
        self.conv1=nn.Conv2d(1,6,5)
        self.conv2=nn.Conv2d(6,16,5)
        #定义一个线性操作 y=wx+b
        #Linear的创建需要两个参数，inputSize 和 outputSize
        #inputSize：输入节点数
        #outputSize：输出节点数
 
        #全连接函数，将16*5*5个节点连接到120个节点上
        self.fc1=nn.Linear(16*5*5,120)#全连接层
        # 全连接函数，将120个节点连接到84个节点上
        self.fc2=nn.Linear(120,84)
        # 全连接函数，将84个节点连接到10个节点上
        self.fc3=nn.Linear(84,10)
 
 
    #定义神经网络的前向传播，一旦定义成功，那么后向传播也会自动生成（autograd）
    def forward(self, x):
        #定义最大池化的输入图像为F.relu,定义的卷积核为（2,2）
        #conv2d(input,filter,strides,padding,use_cudnn_on_gpu=None,data_format=None,name=None)
 
        #输入的x经过卷积conv1之后，经过relu激活函数，再通过2*2的窗口进行最大池化
        x=F.max_pool2d(F.relu(self.conv1()),(2,2))
        # 输入的x经过卷积conv2之后，经过relu激活函数，再通过2*2的窗口进行最大池化，然后更新到x
        x=F.max_pool2d(F.relu(self.conv2(x)),2)
        #view函数将张量x变形为一维向量的形式，总特征数不变，为接下来的全连接做准备
        x=x.view(-1,self.num_flat_features(x))
 
        #输入x,经过全连接1层再经过relu函数,然后更新x
        x=F.relu(self.fc1(x))
        x=F.relu(self.fc2(x))
        #输入x，经过全连接fc3，然后再更新x
        x=self.fc3(x)
        return x
 
net=Net()
#执行该网络
net
 
#以下代码是为了看一眼参数的数量
print (net)
params=list(net.parameters())
 
k=0
for i in params:
    l=1
    print ("该层的结构："+str(list(i.size())))
    for j in i.size():
        l*=j
    print ("参数和："+str(l))
    k=k+1
print ("总参数和："+str(k))
 