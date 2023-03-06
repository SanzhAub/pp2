import re
file = open ('C:/Users/Acer/OneDrive/Рабочий стол/Week 5/regex.md/text.txt', 'r', encoding='UTF8')
spl = re.sub('([A-Z][a-z]+)',r' \1',file.read()).split()
snk = '_'.join([s.lower() for s in spl])
print(snk)