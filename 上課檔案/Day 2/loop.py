#while
'''
while <cond>:
    ...
'''
i = 1 #索引值 index
while i <= 10:
    print(i)
    i += 1

#for 
# for i in <range>
for i in ['鮭魚','鮪魚','玉子燒']:
    print(i)

for i in 'hello':
    print(i)

'''
range(start[init:0], end, interval[init:1])
from start to end-1, increase interval
for i in range(1, 10, 1):
    print(i)
for i in range(1, 10):
    print(i)
for i in range(10):
    print(i)
#10 -> 1

#while
i = 10
while i >= 1:
    print(i)
    i -= 1
#for
for i in range(10, 0, -1):
    print(i)
'''

#continue(skip), break(stop)
for i in range(10):
    if i % 3 == 0: continue
    if i == 8: break
    print(i)