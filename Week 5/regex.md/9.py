import re
file = open ('C:/Users/Acer/OneDrive/Рабочий стол/Week 5/regex.md/text.txt', 'r', encoding='UTF8')
res =re.sub(r"([A-Z]+)", r" \1", file.read())
print(res)