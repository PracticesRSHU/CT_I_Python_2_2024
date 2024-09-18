import random
import string
#           0          1        2 
students=["Andriy","Anton","Victoriya"]
#            -3       -2        -1

print(students)
print(students[0])
groups=[]
print(groups)
# groups.append("CT21")
# groups.append("I-11")
groups.extend(["CT-21","I-21"])
print(groups)
print(type(groups))
# print(type(int("56")))
marks_of_students1=list() #[]
print(marks_of_students1)
marks_of_students2=list((4,5,5,4)) #[]
print(marks_of_students2)
print(id(marks_of_students2))
marks_of_students1=list(marks_of_students2)
print(id(marks_of_students1))

marks_of_students3=marks_of_students1
print(f"marks1:{id(marks_of_students1)}={marks_of_students1}")
print(f"marks3:{id(marks_of_students3)}={marks_of_students3}")
marks_of_students3[3]=5
print(f"No modefied=> marks1:{id(marks_of_students1)}={marks_of_students1}")
print(f"Modefied=> marks3:{id(marks_of_students3)}={marks_of_students3}")

marks_of_students4=marks_of_students1[:] #  or marks_of_students1.copy()  - (shallow copy) неглибоке копіювання
marks_of_students5=list(marks_of_students1) #

print(f"marks1:{id(marks_of_students1)}={marks_of_students1}")
print(f"marks4:{id(marks_of_students4)}={marks_of_students4}")
print(f"marks5:{id(marks_of_students5)}={marks_of_students5}")

marks_of_students5[3]=2
print(f"No modefied=> marks1:{id(marks_of_students1)}={marks_of_students1}")
print(f"Modefied=> marks5:{id(marks_of_students5)}={marks_of_students5}")

# row="Python"
# row[0]="p" #error
# print(row)

lang=["C#","JavaScript","Ruby","Python"]
print(f'id={id(lang)}={lang}')
lang[1]="Java"
print(f'id={id(lang)}={lang}')
lang[2:3]=["C","C++","Dart"]
print(f'id={id(lang)}={lang}')
del lang[2:5] # index 2,3,4
print(f'id={id(lang)}={lang}')
lang[3:]=["C","C++","Dart"]
print(f'id={id(lang)}={lang}')
lang[1::2]=["C++11","C++12","C++13"]
print(f'id={id(lang)}={lang}')
lang[1]="C++"
print(f'id={id(lang)}={lang}')
lang.insert(1,"C")
print(f'id={id(lang)}={lang}')
# del element by index => default => -1
del_element=lang.pop()
print(f'"{del_element}" deleted from list "lang"=>{lang}')
# remove by element
lang.remove('C++12')
print(f'id={id(lang)}={lang}')
# reverse
lang.reverse()
print(f'id={id(lang)}={lang}')

list_symbol=list(string.ascii_lowercase)
print(list_symbol)

# print(random.randint(1,20))
# for item in lang:
#     print(f"We are learning {item}")
#Приклад 1. Сформувати список цілих чисел з діапазону  [1,50], кратні 7
listNumbers1=list()
for number in range(1,51): # [1,2,3,...,50]
    if number % 7==0:
        listNumbers1.append(number)

print(listNumbers1)
#скорочення синтаксису => метод включення
listNumbers2=[number for number in range(1,51) if  number%7==0]
print(listNumbers2)

# variant 1 генерування списку випадкових чисел
listNumbers3=[random.randint(1,20) for _ in range(20)]
print(listNumbers3)
#variant 2 генерування списку випадкових чисел
listNumbers4=[]
for _ in range(20):
    number=random.randint(1,20)
    if not (number in listNumbers4):
        listNumbers4.append(number)
print(listNumbers4)

#variant 3 унікальні значення у списку
listNumbers5=[]
index_element=0
while index_element<20:
    number=random.randint(1,20)
    if not (number in listNumbers4):
        listNumbers5.append(number)
        index_element=index_element+1
print(listNumbers5)

#Глибоке копіювання
list2D=[11,22,[33,44,55]]
print(list2D)
print(list2D[0])  #11
print(list2D[1])  #22
print(list2D[2][1]) #44
print(list2D[2][2]) #55

list2D_copy=list2D.copy()
print("list2D=",list2D)
print("list2D_copy=",list2D_copy)
list2D_copy[0]=1111
print("list2D=",list2D)
print("list2D_copy=",list2D_copy)
list2D_copy[2][1]=4444
print("list2D=",list2D)
print("list2D_copy=",list2D_copy)
import copy
list2D_deepcopy=copy.deepcopy(list2D)
print("list2D=",list2D)
print("list2D_deepcopy=",list2D_deepcopy)
list2D_deepcopy[2][1]=8888
print("list2D=",list2D)
print("list2D_deepcopy=",list2D_deepcopy)