import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

x = re.findall("Portugal", txt)
print(x)