'''
l = []
i = [int(i) for i in input().split()]

for j in i:
    if j > 1:
        l.append(j)

if l:
    print(*l)
else:
    print('none')
'''
l = [i for i in range(1, 11)]
print(l[::2]) #from start to end-1