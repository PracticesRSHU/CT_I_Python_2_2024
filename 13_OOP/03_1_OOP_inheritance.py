# Наслідування (Успадкування) 
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
    def work(self):
        # print(f"{self.__firstname} works") # error
        print(f"{self.firstname} works") # повинні використовуати gettter для доступу до приватинх полів суперкласу
    
class Student(Person):
    def study(self):
        print(f"{self.firstname} is student, which studies...")
#===============множинну наслідування===========

class WorkingStudent(Employee, Student):
    pass


# ========= using class Person=====================
person_obj=Person("Natalya")
print(person_obj)
print("Count persons=",person_obj.getCountPerson())
print("Count persons=",Person.getCountPerson())
person_obj.display_info()


# конекретний працівник
employee1=Employee("Andriy") # obj.__init__
employee1.display_info()
print("Count persons=",employee1.getCountPerson())
employee1.work()
print(employee1)

#конкретний студент
student1=Student("Dmitro")
student1.study()
print(student1)

#конкретний працюючий студент
working_student1=WorkingStudent("Olga")
working_student1.work()
working_student1.study()
