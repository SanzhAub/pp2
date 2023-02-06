max1=0
max2=0
while True:
    a=int(input())
    if a==0: break
    if a>max1:
        max2=max1
        max1=a
    elif a>max2 :
        max2=a
print(max2)