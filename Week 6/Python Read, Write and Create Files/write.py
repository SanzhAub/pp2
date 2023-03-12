f = open("C:/Users/Acer/OneDrive/Рабочий стол/Week 6/Python Read Files/demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("C:/Users/Acer/OneDrive/Рабочий стол/Week 6/Python Read Files/demofile2.txt", "r")
print(f.read())


f = open("C:/Users/Acer/OneDrive/Рабочий стол/Week 6/Python Read Files/demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("C:/Users/Acer/OneDrive/Рабочий стол/Week 6/Python Read Files/demofile3.txt", "r")
print(f.read())