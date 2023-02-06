max=0
i=-1
while True:
    a=int(input())
    
    if a==0:
        break
    if a>max:
        i+=1
        max=a
print(i)