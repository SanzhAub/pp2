import re
file = open ('C:/Users/Acer/OneDrive/Рабочий стол/Week 5/regex.md/text.txt', 'r', encoding='UTF8')
a = re.sub("\s" , ":", file.read())
b = re.sub("\.",":",a)
c = re.sub("\,",":",b)
print(c)