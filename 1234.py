count=0
for i in range(4):
    n=[1,2,3,4]
    n.pop(i)
    for i in range(len(n)):
        for i in range(len(n)-1):
            temp=n[i]
            n[i]=n[i+1]
            n[i+1]=temp
            count+=1
            print(n)
print(count)