n = int(input())
a = []
#start to end-1, increase interval
for i in range(2, n+1):
    while n % i == 0:
        a.append(i)
        n //= i

'''
<sol1>
i = 0
while i <= len(a)-1:
    c = a.count(a[i])
    if c != 1:
        print(f'{a[i]}^{c}',end='')
    else:
        print(f'{a[i]}',end='')

    i += (c-1) #i = i+1
    if i != len(a)-1:
        print(' * ',end='')
    i += 1
'''

# <sol2>
# [2,2,2,3] -> {2,3} -> [2,3]
s = set(a)
s = list(s)
s.sort()
for i in range(len(s)):
    c = a.count(s[i])
    if c == 1:
        print(f'{s[i]}',end='')
    else:
        print(f'{s[i]}^{c}',end='')
    if i != len(s)-1: 
        print(' * ',end='')