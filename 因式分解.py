n = int(input('任意數,求其因數分解'))
ans=[]
for i in range(2,n+1):
    while n%i == 0:
        n=n//i
        ans.append(str(i))
        if n%i ==1:
            break
        
a="*".join(ans)
print(a)