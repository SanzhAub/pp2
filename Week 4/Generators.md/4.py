a = int(input())
b = int(input())
def squrares(a,b):
    while a**2<b**2:
        yield a**2
        a+=1
for i in squrares(a,b):
    print(i)
