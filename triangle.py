number=int(input('想要幾層的?'))
a=[0,1]
for i in range(number):
    b=[]
    for i in range(len(a)-1):
        x=a[i]+a[i+1]
        b.append(x)
    #print(b)
    print(' '*(number-i),end='')
    for s in b:
        print(s,end=' ')
    print()
    a=b
    a.insert(0,0)
    a.append(0)
    

