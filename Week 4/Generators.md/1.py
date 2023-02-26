def squares(x):
  i=0
  while i**2<=x:
        yield i**2
        i+=1
for i in squares(int(input())):
    print(i)