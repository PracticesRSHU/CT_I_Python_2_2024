
from abc import ABCMeta, abstractmethod
class Pet(metaclass=ABCMeta):
    def __init__(self,name) -> None:
        self.__name=name 

    @abstractmethod
    def eat(self):
        pass #порожня реалізація
    
    @abstractmethod
    def voice(self):
        pass #порожня реалізація
    

class Cat(Pet):
    def __init__(self, name):
        """Конструктор
        :param name: Кличка тварини
        """
        self.__name=name

    def eat(self):
        print(f"Cat {self.__name} like milk and fish.")

    def voice(self):
        print("May-may")

class Dog(Pet):
    def __init__(self, name):
        """Конструктор
        :param name: Кличка тварини
        """
        self.__name=name

    def eat(self):
        print(f"Dog {self.__name} like eat and fish.")

    def voice(self):
        print("Gav-gav")

# pet=Pet("Ituch") # TypeError: Can't instantiate abstract class Pet without an implementation for abstract methods 'eat', 'voice'
mycat = Cat("Tom")
mycat.eat()
mycat.voice()

mydog=Dog("Chupu")
mydog.eat()
mydog.voice