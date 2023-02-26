def even(x):
  i=0
  while i<=x:
        if i%2==0:
            yield i
        i+=1
for i in even(int(input())):
    print(i,end=', ')