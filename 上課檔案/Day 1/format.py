'''
格式符號
d -> int
f -> float
s -> str
e -> 科學記號
(1)%
    name, score = '王大明',100
    print('姓名:%s,成績:%d'%(name, score))
(2).format()
    name, score = '王大明',100
    print('姓名:{},成績:{}'.format(name, score))
(3)f-string [function]
    print(f'1+1={1+1}')
    name, score = '王大明',100
    print(f'姓名:{name},成績:{score}')
'''

print('kevin', 100)
print('alan', 80)
print('andy', 5)

print('姓名:%5s,成績:%3d'%('kevin', 100))
print('姓名:%5s,成績:%3d'%('alan', 80))
print('姓名:%5s,成績:%3d'%('andy', 5))

print('姓名:{:5s},成績:{:3d}'.format('kevin', 100))
print('姓名:{:5s},成績:{:3d}'.format('alan', 80))
print('姓名:{:5s},成績:{:3d}'.format('andy', 5))

name = ['kevin', 'alan', 'andy']
print(f'姓名:{name[0]:5s},成績:{100:3d}')
print(f'姓名:{name[1]:5s},成績:{80:3d}')
print(f'姓名:{name[2]:5s},成績:{5:3d}')
