profit=int(input('利潤?'))
if profit <=100000:
    bonus=profit*0.1
if profit >100000 and profit<=200000:
    bonus=((profit-100000)*0.075)+100000*0.1
if profit >200000 and profit<300000:
    bonus=(profit-200000)*0.03+(100000*0.075)+100000*0.1
    
print('獎金',bonus)

