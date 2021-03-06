import time
import numpy as np

class My_Class():
    def __init__(self,name,age) -> None:
        self._name = name
        self._age = age 
    @property
    def name(self):
        return self._name 
    @name.setter
    def name(self,name):
        self._name = name 
class Doge(My_Class):
    def wink(self):
        print('see you')
'''
def log_fuc_time(func):
    def wrapper():
        start_time = time.perf_counter()
        func()
        end_time = time.perf_counter()
        print('方法{}执行了{}ms'.format(func.__name__,(end_time - start_time)*1000))
    return wrapper

@log_fuc_time
def calculate_fun1():
    list1 = [i for i in range(20)]
    for i in list1:
        print(i)


@log_fuc_time
def calculate_fun2():
    list2 = (i for i in range(20))
    for i in list2:
        print(i)

calculate_fun1()

calculate_fun2()
'''

def test(sum,a,b):
    sum = a + b
    return sum

if __name__ == '__main__':
    t = My_Class('GMZ',18)
    t.name = 'TY'
    print(t._name)

