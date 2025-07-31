a, b, c = [int(i) for i in input().split()]

def sol(a, b, c):
    D = b**2 - 4 * a * c
    if D < 0: #no real root
        return None
    else:
        # (1)
        a1 = (-b + D**.5)/(2*a)
        a2 = (-b - D**.5)/(2*a)
        return [a1, a2]
    
r = sol(a,b,c)        
if not(r):
    print('No real root')
# (2)    
elif r[0]==r[1]:
    print(f'Two same roots x={int(r[0])}')
else:
    print(f'Two different roots x1={int(r[0])} , x2={int(r[1])}')