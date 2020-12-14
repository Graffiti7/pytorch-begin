from 判断闰年  import runnian

Day = [31,28,31,30,31,30,31,31,30,31,30,31]

def days(time):
    total = 0
    for i in range(int(time[1])-1):
        total += Day[i]
    total += int(time[2])
    if(runnian(int(time[0]))==0):
        return total
    else:
        if(int(time[1])>2):
            return total + 1
        else:
            return total

x = input()
for i in range(int(x)):
    time = input().split()
    print(days(time))
