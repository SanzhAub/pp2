max = 0
a = -1
i = -1
i_max = 0
while a != 0:
    a = int(input())
    i += 1
    if a > max:
        max = a
        i_max = i        
print(i_max) 