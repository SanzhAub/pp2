sum=0
i=0
while True:
    a=int(input())
    sum+=a
    if a==0:
        break
    i+=1
print(sum/i)