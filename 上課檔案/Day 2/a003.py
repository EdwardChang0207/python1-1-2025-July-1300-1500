M, D = input().split() #'3 5' -> ['3','5']
M, D = int(M), int(D)
S = (M*2+D)%3
if S == 0: print('普通')
elif S == 1: print('吉')
else: print('大吉')
