a=[1,2]
ans=0
for i in range(20):
    b=a[i]+a[i+1]
    a.append(b)
    c=a[i+1]/a[i]
    ans+=c
print(ans)