f = open("C:/Users/Acer/OneDrive/Рабочий стол/Week 6/Python Read Files/demofile.txt", "r")
print(f.read())

f = open("C:/Users/Acer/OneDrive/Рабочий стол/Week 6/Python Read Files/demofile.txt", "r")
print(f.read(5))

f = open("C:/Users/Acer/OneDrive/Рабочий стол/Week 6/Python Read Files/demofile.txt", "r")
print(f.readline())

f = open("C:/Users/Acer/OneDrive/Рабочий стол/Week 6/Python Read Files/demofile.txt", "r")
print(f.readline())
print(f.readline())

f = open("C:/Users/Acer/OneDrive/Рабочий стол/Week 6/Python Read Files/demofile.txt", "r")
for x in f:
  print(x)