itemA=[100,80,90,70,100]
itemB=itemA
itemC=list()
for a in itemA:
    itemC.append(a)  
itemA[1]=88 #itemC串列不會被改變
print(itemA)
print(itemC)
