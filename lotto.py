import random
lotto=[]

while len(lotto)<7:
    for i in range(7-len(lotto)):
        x=random.randint(1,49)
        lotto.append(x)
        lotto=list(set(lotto))
print(lotto)

        