import re 
file = open ('C:/Users/Acer/OneDrive/Рабочий стол/Week 5/regex.md/text.txt', 'r', encoding='UTF8')
res = re.findall('[A-Z][^A-Z]*', file.read())
print(res)
