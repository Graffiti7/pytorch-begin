n = input()
for i in range(int(n)):
    x,y = map(int,input().split())
    ans = input()
    list1 = [int(i) for i in ans.split()]
    ans2 = input()
    list2 = [int(i) for i in ans2.split()]
    list1.extend(list2)
    list1.sort()
    print(list1)
