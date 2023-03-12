import string 
import re
x = input()
small = 0
big = 0 
for i in range(len(x)):
    if x[i].islower():
        small+=1
    elif x[i].isupper():
        big+=1
print("Number of upper case letters:" ,big)
print("Number of small case letters:" ,small)