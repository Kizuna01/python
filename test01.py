for a in range(2,11):
    prime=0
    for b in range(2,a):
        if a%b==0:
            prime=1
            break
    if prime ==0:
        print(a)    