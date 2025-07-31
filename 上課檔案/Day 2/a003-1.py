M, D = input().split() #'3 5' -> ['3','5']
M, D = int(M), int(D)
S = (M*2+D)%3
luck = ['普通','吉','大吉']
print(luck[S])
