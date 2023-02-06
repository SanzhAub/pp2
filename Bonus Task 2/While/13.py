max =0
cnt = 0
while True:
    a = int(input())
    if a==0: break
    if max < a:
        max = a
        cnt = 1
    elif max == a:
        cnt += 1
print(cnt)