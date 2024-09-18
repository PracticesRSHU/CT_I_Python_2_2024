# # if value:
# #     commands
# # else:
# #     commands

# # if value1:
# #     commands
# #elif value2:
# #     commands
# # else:
# #     commands

# #> < >= <= != is  and or not
# # predicate , logic value


# if "Python": #true
#     print("Commands for true")
# else:
#     print("Commands for false")


# if not None: #  23, "str" =>  true
#     print("Commands for true")
# else:
#     print("Commands for false")


# a=6
# b=67

# if a>b:
#     max=a
# else:
#     max=b

# print(f'max={max}')

# # operand1 if value else operand2
# max=a if a>b else b #ternarniy
# print(f'max={max}')

# day_of_week=int(input("Input number day of week: "))
# if day_of_week>=1 and day_of_week<=5:  #[1;5]
#     print("working day")
# elif day_of_week==6 or day_of_week==7:
#     print("weekend")
# else:
#     print("Error")

# # match
# match day_of_week:
#     # pattern1
#     case 1|2|3|4|5:
#         print("working day")
#     # pattern2
#     case 6|7:
#         print("weekend")
#     # default pattern
#     case _: #alternativ varaiable
#         print("Error")

# """
# for змінна in послідовність:
#     команди
# """

# """
# for змінна in послідовність:
#     команди
# else:                     
#     команди
# """

# # range(10) => [0,1,2,...,9]
# suma=0
# for i in range(10):
#     suma+=i
#     print(i,end="\t")

# print("\n",suma)

# print(list(range(4,10,2))) #4 6 8

"""
while умова(предикат):
    команди (ітерації)
else:
    команди (успішний цикл без break)
"""

"""
1. Вмочив пензлик у фарбу 
2. Пофарбував штахету #i
3. Крок вправо на одну штахету
... допоки не закінчаться штахети в паркані
паркан складається з 20 штахет
"""

for item in range(20):
    if item==10: 
        print("Break.....")
        break
    working="1. Вмочив пензлик у фарбу.\n2. Пофарбував штахету #{} \n3. Крок вправо на одну штахету\n\n".format(item+1)
    print(working)
else:
    print("Work done!!!") #not break cicle

# Том Соєр вирішив фарбувати кожну другу штахету
for item in range(20): #0,1,2,3..,19
    if item%2==1: 
        print("Continue item #",item+1)
        continue
    if item==10: 
        print("Break.....")
        break
    working="1. Вмочив пензлик у фарбу.\n2. Пофарбував штахету #{} \n3. Крок вправо на одну штахету\n\n".format(item+1)
    print(working)
else:
    print("Work done!!!") #not break cicle

for item in range(1,21): #1,2,3..,20
    if item%2==1: 
        print("Continue item #",item)
        continue
    if item==10: 
        print("Break.....")
        break
    working="1. Вмочив пензлик у фарбу.\n2. Пофарбував штахету #{} \n3. Крок вправо на одну штахету\n\n".format(item)
    print(working)
else:
    print("Work done!!!") #not break cicle


# break continue
# while
print("Working with while...")
cout_shtaheta=20
all_shtahet=20
while cout_shtaheta<all_shtahet:
    cout_shtaheta+=1 
    # cout_shtaheta=cout_shtaheta+1
    working="1. Вмочив пензлик у фарбу.\n2. Пофарбував штахету #{} \n3. Крок вправо на одну штахету\n\n".format(cout_shtaheta+1)
    print(working)
else:
    print("Work done!!!") #not break cicle
