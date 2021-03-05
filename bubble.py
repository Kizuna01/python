number=list()
while len(number)<=5:
    num=int(input('請輸入數字'))
    number.append(num)
print('串列內容',number)
print('氣泡排序法')

for v in range(len(number)):
    for i in range(len(number)-1):
        if number[i]>number[i+1]:
            temp=number[i+1]
            number[i+1]=number[i]
            number[i]=temp
print(number)