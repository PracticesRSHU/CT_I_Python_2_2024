# Наслідування (Успадкування) + Полімоврфізм
"""
class підклас (суперклас):
    методи_класу
"""
#==========defination class Person===========
class Person:
    count_person=0 #static field
    def __init__(self,firstname):
        """Коснтруктор
        :param firstname: Імя людини
        """
        self.__firstname=firstname
        Person.count_person+=1

    def __del__(self):
        Person.count_person-=1
        
    def __str__(self):
        return f"Person {self.firstname}"

    @property
    def firstname(self):
        return self.__firstname
    
    @firstname.setter
    def firstname(self,value):
        if value:
            self.__firstname

    @staticmethod
    def getCountPerson():
        """Статичний метод
        :return: значення статичного поля сount_person
        """
        return Person.count_person
    
    def display_info(self):
        print(f"Person firstname: {self.__firstname}")

# ==============одиничне наслідування===========
class Employee(Person):
    """
    опис класу працівника 
    """  
    def __init__(self, firstname, salary=0):
        super().__init__(firstname) #виклик конструктура базового класу (суперкласу)
        self.__salary=salary
   # ....
   # GETTERS, SETTERS
   # ....
    def work(self):
        # print(f"{self.__firstname} works") # error
        print(f"{self.firstname} works and has salary {self.__salary}") # повинні використовуати gettter для доступу до приватинх полів суперкласу
    
class Student(Person):
    def __init__(self, firstname,university="RSHU"):
        super().__init__(firstname)
        self.__university=university
   
    @property
    def university(self):
        return self.__university
    
    @university.setter
    def university(self,value):
        self.__university=value

    def study(self):
        print(f"{self.firstname} is student of {self.__university}, which studies...")
#===============множинну наслідування===========

class WorkingStudent(Employee, Student):
    def __init__(self, firstname, salary=0,university="RSHU"):
        super().__init__(firstname, salary)
        self.university=university # використано сеттер класу Student

    def print_info(self):
        print("===============Info about person in class WorkingSttudent=====")
        self.study()
        self.work()
        print("=============================The End==========================")


# ========= using class Person=====================
person_obj=Person("Natalya")
print(person_obj)
print("Count persons=",person_obj.getCountPerson())
print("Count persons=",Person.getCountPerson())
person_obj.display_info()


# конекретний працівник
employee1=Employee("Andriy",10500) # obj.__init__
employee1.display_info()
print("Count persons=",employee1.getCountPerson())
employee1.work()
print(employee1)

#конкретний студент
student1=Student("Dmitro")
student1.study()
print(student1)

#конкретний працюючий студент
working_student1=WorkingStudent("Olga",14900)
working_student1.work()
working_student1.study()

print(WorkingStudent.__mro__)  #ієрархію послідовності виклику класів
working_student1.print_info()

# list bases class 
print(Employee.__base__)
# dict attr of class
print(Employee.__dict__)
print(Employee.__doc__)
print(Employee.__module__)

print(Employee.__annotations__)

