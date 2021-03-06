import random
a=random.randint(1,9)
b=random.randint(1,9)
c=random.randint(1,9)
d=random.randint(1,9)

ans=[a,b,c,d]
guess=[]
print(ans)
while ans != guess:
    ans=[a,b,c,d]
    number=int(input('輸入四位數'))
    number1=number//1000
    number2=number//100-number//1000*10
    number3=number//10-number//100*10
    number4=number//1-number//10*10
    
    guess=[number1,number2,number3,number4]
    A=0
    B=0
    C=[]#蒐集A的值，然後一次清除掉
    print(ans)
    print(guess)
    for i in range(0,4):
        if ans[i]== guess[i]:
            A+=1
            C.append(ans[i])
    for i in C:
        ans.remove(i)
        guess.remove(i)        
    guess=list(set(guess))#去除猜數中的重複項目，避免重複計算B
    
    for i in range(len(guess)):    
        if ans.count(guess[i]) ==1:
                B+=1
    print(A,'A',B,'B')
print('right')

