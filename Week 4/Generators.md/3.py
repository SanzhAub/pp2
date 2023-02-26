def iter(x):
  i=0
  while i<=x:
        if i%3==0 and i%4==0:
            yield i
        i+=1
for i in iter(int(input())):
    print(i)