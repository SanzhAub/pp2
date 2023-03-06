import re
file = open ('C:/Users/Acer/OneDrive/Рабочий стол/Week 5/regex.md/text.txt', 'r', encoding='UTF8')
words = file.read().split("_")
up_words = [words[0]] + [w.capitalize() for w in words[1:]]
camel = "".join(up_words)
print(camel)