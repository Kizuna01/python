for i in range(1,5):
    print(' '*(4-i)+'*'*(2*i-1))
for i in range(3,0,-1):
    print(' '*(4-i)+'*'*(2*i-1))
    
#利用center的功能，來印出菱形
s='*'
for i in range(1,8,2):
    print((s*i).center(7))
for i in range(5,0,-2):
    print((s*i).center(7))
    

#暴力迴圈解
for i in range(1,8,2):
    for v in range(i,7,2):
        print(' ',end='')
    for s in range(i):
        print('*',end='')
    print()
for i in range(5,-1,-2):
    for v in range(i,6,2):
        print(' ',end='')
    for s in range(i):
        print('*',end='')
    
    print()