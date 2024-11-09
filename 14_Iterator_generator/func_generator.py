# ГЕНЕРАТОРИ-ФУНКЦІЇ
def fibonach_generator(n):
    prev=1 #first element of siquence
    next=1 #second element of siquence
    for i in range(n):
        result=prev
        prev, next=next, prev+next
        # return result
        yield result

generator_FIB=fibonach_generator(4)
print(next(generator_FIB))
print(next(generator_FIB))
print(next(generator_FIB))
print(next(generator_FIB))
# print(next(generator_FIB)) #exception

for i in fibonach_generator(10):
    print(i,end="; ")
print()

def fibonach_generator2(n):
    prev=1 #first element of siquence
    next=1 #second element of siquence
    for i in range(n):
        result=prev
        temp_prev=prev
        temp_next=next
        prev=next
        next=temp_prev+temp_next
        # prev, next=next, prev+next
        yield result

print(list(fibonach_generator2(10)))



def colors():
    yield "green"
    yield "yellow"
    yield "red"

colors_list=list(colors())
print(colors_list)
for color in colors():
    print(color)