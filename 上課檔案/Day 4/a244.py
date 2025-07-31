N = int(input())
#重複N次
for i in range(N):
    #處理一組的code
    a, b, c = [int(i) for i in input().split()]
    if a == 1:
        print(b+c)
    elif a == 2:
        print(b-c)
    elif a == 3:
        print(b*c)
    else:#a==4
        print(int(b/c))