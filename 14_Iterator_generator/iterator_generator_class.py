# collection=[3,4,6,7]
# for item in collection:
#     print(item)
# # print(collection[4]) # IndexError
# collection=(3,4,6,7)
# for item in collection:
#     print(item)

# class iterator =>
# 1) передати екземпляру класу посилання на колекцію, 
#  для якої цей обєкт буде ітератором. 
# 2) описати спец. метод __next__(), в якому визначити спосіб 
# послідовного перебору (оюходу) елементів колекції
# StopIteration -  end iteration


class Iterator:
    def __init__(self, collection) -> None:
        self.__collection=collection
        self.__cursor=0 #  поточна позиція ітератора
    
    # def __next__(self):
    #     if self.__cursor==len(self.__collection):
    #         raise StopIteration
    #     item=self.__collection[self.__cursor] #значення колекції
    #     self.__cursor+=1
    #     return item

    def __next__(self):
        try:
            item=self.__collection[self.__cursor] #значення колекції
            self.__cursor+=1
            return item
        except IndexError:
            raise StopIteration

# Для перетворення класу-колекцію в ітерований обєкт 
# використовується спец метод __iter__()
collection1=[33,44,66,77]
#стандартна функція, що задана в стандарнтій біблотеці

iterator1= iter(collection1) 
print(iterator1)
#явний виклик ітератора
print(iterator1.__next__())
# print(iterator1.__next__())
print(next(iterator1))
print(iterator1.__next__())
print(iterator1.__next__())
# print(iterator1.__next__()) #stop iterator

# collection2=(33,44,66,77)
# iterator2= iter(collection2)
# print(iterator2)

collection3=(333,444,555,777)
#for елемент in щось => iter(щось) =>  next(щось)
for item in collection3:
    print(item)

set()
iterator3={'a','b','c'}.__iter__()
print(iterator3.__next__())

# клас користувача НАШ ІТЕРАТОР
iterator3= Iterator(collection3)
print(iterator3.__next__()) # or print(next(iterator3))
print(iterator3.__next__())
print(iterator3.__next__())
print(iterator3.__next__())
# print(iterator3.__next__()) #exeption


# Створити ітератор піднесення 2 до степеня:
# pow(2,n), 2^0,  2^1, 2^2, 2^3
# n=3
#КЛАС ГЕНЕРАТОР (це ІТЕРАТОР з функцією _iter_)
class PowToTwo:
    def __init__(self,n=0):
        self.__n=n
        
    def __iter__(self):
        self.__start=0
        return self
    
    def __next__(self):
        if self.__start<=self.__n:
            result=2**self.__start
            self.__start+=1
            return result
        else:
            raise StopIteration
        
print("Using our class PowToTwo:")        
numbers=PowToTwo(5)
iterator_pow=iter(numbers) # 1, 2, 4,  8, 16, 32
print(next(iterator_pow))
print(next(iterator_pow))
print(next(iterator_pow))
print(next(iterator_pow))
print(next(iterator_pow))
print(next(iterator_pow))
# print(next(iterator_pow)) #exception

print("Object PowToTwo(5)=>",PowToTwo(5))

for i in PowToTwo(5):
    print(i)

list_two_in_step=list(PowToTwo(10))
print(list_two_in_step)


# range(3,10,1)  3<10

class MyRange:
    def __init__(self,start=0, end=0, step=1) -> None:
        self.__start=start
        self.__end=end
        self.__step=step

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__start<=self.__end:
            result=self.__start
            self.__start+=self.__step
            return result
        else:
            raise StopIteration
        
    @property
    def start(self):
        return self.__start
    
    @property
    def end(self):
        return self.__end
    
    @start.setter
    def start(self,value):
        if isinstance(value,int):
            self.__start=value
        else:
            raise AttributeError
        
    @end.setter
    def end(self,value):
        self.__end=value

myrange=MyRange(1,10)
print(list(myrange)) # 1,2,3,4,5,6,7,8,9,10

#=>  self.__start=11
for item in myrange: #not worked
    print("I am working!")
    print(item)
else:
    print("end for")

myrange1=MyRange(1,10)
for item in myrange1:
    # print("I am working! Спроба2")
    print(item)
else:
    print("end for")

myrange1.start=1
myrange1.end=10
for item in myrange1:
    # print("I am working! Спроба2")
    print(item)
else:
    print("end for")


