x = input()
rvs = "".join(reversed(x))
def pal(x):
    if  rvs == x:
        return ("Palindrome")
    else:
        return ("Not palindrome")
print(pal(x))