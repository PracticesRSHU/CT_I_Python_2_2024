'''
print("Hello")
print("Hello")
print("Hello")
'''

# a=5
# b=6
# suma=a+b
# print(suma)

# int, float, complex, str, list, tuple, set, dict
# print("Input a:")
a=input("Input a:")
a=float(a)
print("Input b:",end="")
b=float(input())
print(type(a))
suma=a+b #concat str
print("Suma=",suma,sep="")
result_div=a/b
print(a,"/",b,"=",result_div)
result=f'{a:.2f} / {b:^10.2f} = {(a/b):.2f}'
print(result)
# %, format

# using type str in Python
str1="We"
str2="""are learning"""
str3='Python'
newstr=str1+"\n"+str2+"\t"+str3
print(newstr)
newstr2="Вірш \"Сон\""
print(newstr2)
poem="""У всякого своя доля
І свій шлях широкий,
Той мурує, той руйнує,
Той неситим оком
За край світа зазирає,
Чи нема країни,
Щоб загарбать і з собою
Взять у домовину.
"""

print(poem)

import math
x=float(input("Input x="))
y=float(input("Input y="))
# rez=(math.sin(x+y)**3)/math.log(x) # ln(x) 
rez=(math.pow(math.sin(x+y),3))/math.log(x) # ln(x) 
print(f'Rez={rez}')

