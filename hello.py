import torch

x = torch.rand(5, 3)

print(x)

a,b,c = 1,2.0,"abc" 

print(a,b,c)

print(type(a),type(b),type(c))

a,b,c = 1,2,3

print(a+b//c)

print(type(a),type(b),type(c))

print(isinstance(a,int));

str = "Friend" 

skt = "My best"

print(str)

print(str[0:-2])

print(2*str)

print(skt + str)

a = set('ababababab')

print(a)

list = ["Hello","my","friend"]

b=list[:]

print(type(b))

print(list[:] is list)

def reversestring(input):           #字符串反转
    
    intputWords = input.split(" ")

    intputWords = intputWords[-1::-1]

    output = ' '.join(intputWords)
    
    return output

input = "I love you"

print(reversestring(input))

num1= 2010

num2= 2020

if(num1>num2):
    print(num1)
else:
    print(num2)

if(num1 is num2):
    print(num1 is num2)
else:
    print(num1 is num2)