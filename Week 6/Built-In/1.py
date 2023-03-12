import math 
list = []
n = int(input())
for i in range(n):
    list.append(int(input()))
def func(list):
    return math.prod(list)
print (func(list))