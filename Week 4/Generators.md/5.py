n = int(input())
def f(n):
    while n>0:
        yield n
        n-=1
for i in f(n):
    print(i)