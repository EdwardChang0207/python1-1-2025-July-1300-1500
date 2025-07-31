a, b, c = [bool(int(i)) for i in input().split()]
r = []
#AND
if (a and b) == c:
    r.append('AND')
#OR
if (a or b) == c:
    r.append('OR')
#XOR
# if ((a or b) and not(a and b)) == c:
#     r.append('XOR')
if (a ^ b) == c:
    r.append('XOR')

#IMPOSSIBLE
if not r: print('IMPOSSIBLE')
else: print(*r, sep='\n')