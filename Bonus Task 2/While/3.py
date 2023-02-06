import math
a=int(input())
n=1
while 2**n<=a:
    n+=1
if 2**n>a:
    n=n-1
print(n,2**n)