import random
a=random.randint(1,9)
b=random.randint(1,9)
c=random.randint(1,9)
d=random.randint(1,9)

while a==b or a==c or a==d or b==c or b==d or c==d:
    a=random.randint(1,9)
    b=random.randint(1,9)
    c=random.randint(1,9)
    d=random.randint(1,9)
    
ans=a*1000+b*100+c*10+d
#print(ans)
guess=0
while ans != guess:
    a=0
    b=0
    guess=int(input('輸入4位數，1放棄公布答案'))
    ans1=ans//1000
    ans2=ans//100-ans//1000*10
    ans3=ans//10-ans//100*10
    ans4=ans//1-ans//10*10
    
    guess1=guess//1000
    guess2=guess//100-guess//1000*10
    guess3=guess//10-guess//100*10
    guess4=guess//1-guess//10*10
    
    if guess==1:
        print('殘念')
        print('答案為',ans)
        break
    elif guess1==guess2 or guess1==guess3 or guess1==guess4 or guess2==guess1 or guess2==guess3 or guess2==guess4 or guess3==guess1 or guess3==guess2 or guess3==guess4 :
        print('禁止輸入重複數字，ex:1111、1233')
        continue
    
    else:
     if guess1==ans1:
        a+=1
     if guess2 == ans2:
        a+=1
     if guess3 == ans3:
        a+=1
     if guess4 == ans4:
        a+=1
    
     if guess1==ans2 or guess1==ans3 or guess1==ans4:
        b+=1 
    
     if guess2 == ans1 or guess2==ans3 or guess2==ans4:
        b+=1
     if guess3 == ans1 or guess3 ==ans2 or guess3 ==ans4:
        b+=1
     if guess4 == ans1 or guess4 ==ans2 or guess4 ==ans3:
        b+=1
    
    if a==4 :
        print('賓果，答案為',ans)
    else:
        print(a,'a',b,'b')