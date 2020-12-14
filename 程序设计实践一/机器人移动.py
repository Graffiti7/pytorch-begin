def move(str):
    x,y = 0,0
    for i in range(len(str)):
        if(str[i]=='W'):
            y+=1
        elif(str[i]=='S'):
            y-=1
        elif(str[i]=='D'):
            x+=1
        elif(str[i]=='A'):
            x-=1
    print(x,y)

n = input()        
for i in range(int(n)):
    step = input()
    move(step)

