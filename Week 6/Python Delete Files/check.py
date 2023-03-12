import os
if os.path.exists("C:/Users/Acer/OneDrive/Рабочий стол/Week 6/Python Read Files/demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
