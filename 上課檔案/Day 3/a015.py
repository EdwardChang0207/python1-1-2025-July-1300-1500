'''
r, c = input().split()
r, c = int(r), int(c)
A = []
for i in range(r):
    row = input().split() #['1','2','3']
    A.append(row)

2 3
1 2 3
2 3 4
'''
import sys
for i in sys.stdin:
    r, c = i.split()
    r, c = int(r), int(c)
    A = []
    for i in range(r):
        row = input().split()
        A.append(row)

    AT = []
    for j in range(c):
        nr = []
        for i in range(r):
            nr.append(A[i][j])
        AT.append(nr)

    for i in range(c):
        print(*AT[i])