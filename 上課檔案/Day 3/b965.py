def filp(matrix:list):
    matrix.reverse()
    return matrix
def rotate(matrix:list):
    #AT
    AT = []
    for j in range(len(matrix[0])):
        nr = []
        for i in range(len(matrix)):
            nr.append(matrix[i][j])
        AT.append(nr)
    #Filp
    AT = filp(AT)
    return AT

R,C,M = input().split()
#sol1
B = []
for i in range(int(R)):
    B.append(input().split()) 
#sol2
'B = [input().split() for i in range(int(R))]'
k = input().split()
k.reverse()
for i in k:
    if i == '1': B = filp(B)
    else: B = rotate(B)
print(len(B), len(B[0]))
for row in B:
    print(*row)