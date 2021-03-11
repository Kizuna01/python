s=['A','B','C']
for i in range(len(s)):
    for i in range(len(s)-1):
        temp=s[i]
        s[i]=s[i+1]
        s[i+1]=temp
        print(s)
