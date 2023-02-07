a = int(input())
b = int(input())
i = 1
while b - a > 0:
    a = a + (a * 0.1)
    i += 1
print(i)
