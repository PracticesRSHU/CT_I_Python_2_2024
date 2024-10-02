tuple1=()
tuple2=tuple()
tuple3=(3,)
print(f"tuple1={tuple1} type: {type(tuple1)}")
print(f"tuple2={tuple2} type: {type(tuple2)}")
print(f"tuple3={tuple3} type: {type(tuple3)}")

x,y,z=23,"Python",67
print(x)
print(y)
print(z)

books=('Shevchenko', 'Franko')
print(books)
#books[0]='Stusa'  #error runtime
library=list(enumerate(books))
print(library)
# methods count; index
# function: len, min, max