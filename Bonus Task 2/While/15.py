a = int(input())
b = 0
b1 = 1
b2 = 1
while b1 < a or b2 < a:
    b1 = b1 + b2
    b2 = b1 + b2
    b += 2
if b1 == a:
    b = b + 1
if a + b1 == b2 or a + b2 == b1 or b1 == a:
    print(b)
else:
    print(-1)