import re

txt = "The rain in Spain"

x = re.search("ai", txt)
print(x) #this will print an object

x = re.search(r"\bS\w+", txt)
print(x.span())

x = re.search(r"\bS\w+", txt)
print(x.string)

x = re.search(r"\bS\w+", txt)
print(x.group())

