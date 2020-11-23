import torch

x = torch.empty(5,3)

y = torch.rand(5,3)

z = torch.tensor([5.5,3])

x = x.new_ones(5,3,dtype = torch.float64)

x = torch.rand_like(x,dtype = torch.float64)

print(x.size()[0:]) #torch.size()是一个tuple,支持tuple操作，获取tensor形状也可使用print(x.shape)

'''
#算术操作
#test1:
print(x+y)

#test2:
print(torch.add(x,y))

test3:
result = torch.empty(5,3)
torch.add(x, y, out = result)
print(result)

#test4:
y.add_(x)
print(y)
'''
#索引(索引结果与原数据共用共享内存 即改变其中一个，另一个也随之变化)
'''
y = x[0,:]
y+=1
print(y)
print(x[0,:])
'''

#改变形状
'''
y = x.view(15)

z = x.view(-1,5)

print(x.size(),y.size(),z.size())
'''

#创建副本
'''
x_cp = x.clone().view(-1,5)
print(x)
print(x_cp)
'''

#转换tensor为python
'''
x = torch.rand(1)
print(x)
print(x.item())
'''

#广播机制
'''
x = torch.arange(1,4).view(1,3)

y = torch.arange(1,4).view(3,1)

print(x)

print(y)

print(x+y)
'''
#Tensor与Numpy的相互转换
'''
y = x.numpy()
print(x)
print(y)
'''

#从numpy转回Tensor
'''
import numpy
a = numpy.ones(5)
b = torch.from_numpy(a)
print(b)
'''

#requires_grad用于追踪函数求导
'''
x = torch.ones(2,2,requires_grad=True)
y = x + 1
print(y)
print(x.grad_fn) # x直接创建为叶子节点
print(y.grad_fn)# 创建加法操作<AddBackward0 object at 0x0000028C262D6970> 
print(x.is_leaf,y.is_leaf)
'''

#复杂的操作
'''
z = y*y*3
out = z.mean()# mean函数用于取均值
print(z,out)
'''
#梯度
'''
x = torch.ones(3,3).requires_grad_(True)
t = x*2
t.backward(torch.ones_like(t))
print(x.grad)
'''