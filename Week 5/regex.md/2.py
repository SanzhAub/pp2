import re

file = open ('C:/Users/Acer/OneDrive/Рабочий стол/Week 5/regex.md/text.txt', 'r', encoding='UTF8')
result = re.findall("ab{2,3}",file.read())
print(result)