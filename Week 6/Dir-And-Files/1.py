import os
import string
# ex1
path="C:\\Users\\Acer\\OneDrive\\Рабочий стол\\Week 6\\Dir-And-Files\\"
print("Only directories:")
print([d for d in os.listdir(path) if  os.path.isdir(os.path.join(path,d))])
print("Only files:")
print([f for f in os.listdir(path) if not os.path.isdir(os.path.join(path,f))])
print("Files and directories together:")
print([fd for fd in os.listdir(path)])

#ex2
if os.path.exists(path):
    print("Yes")
else:
    print("No")

print(os.access(path,os.R_OK))
print(os.access(path,os.W_OK))
print(os.access(path,os.X_OK))

#ex3
path3="c:\\Users\\nuriks\\Documents\\GitHub\\pp2_22B050864\\TSIS-6\\dirandfiles\\23794274934.txt"
path2="C:\\Users\\Acer\\OneDrive\\Рабочий стол\\Week 6\\Dir-And-Files\\D.txt"
if os.path.exists(path2):
    print(os.path.dirname(path2))
    print(os.path.basename(path2))
else:
    print('No')
if os.path.exists(path3):
    print(os.path.basename(path3))
else:
    print("No")

#ex4
b = open("C:\\Users\\Acer\\OneDrive\\Рабочий стол\\Week 6\\Dir-And-Files\\B.txt", "r" )
cnt = 0
for line in b:
    cnt += 1
print(cnt)

#ex5
c = open("C:\\Users\\Acer\\OneDrive\\Рабочий стол\\Week 6\\Dir-And-Files\\1.txt","w")
ls = [s for s in input().split()]
for s in ls:
    c.write(s + " ")

#ex6
if not os.path.exists("letters"):
   os.makedirs("letters")
for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)

#ex7
copy = open("C:\\Users\\Acer\\OneDrive\\Рабочий стол\\Week 6\\Dir-And-Files\\cop.txt","r")
read = open("C:\\Users\\Acer\\OneDrive\\Рабочий стол\\Week 6\\Dir-And-Files\\read.txt","a")

for lines in copy:
    read.write(lines)


#ex8
if os.path.exists("C:\\Users\\Acer\\OneDrive\\Рабочий стол\\Week 6\\Dir-And-Files\\delete.txt"):
    os.remove("C:\\Users\\Acer\\OneDrive\\Рабочий стол\\Week 6\\Dir-And-Files\\delete.txt")
else:
    print("File does not exits!")