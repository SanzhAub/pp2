sum=0
m=0
s=0
a = int(input())
while a != 0:
    m += 1
    s += a
    sum += a ** 2
    a = int(input())
print(((sum - s ** 2 / m)/(m - 1))**0.5)