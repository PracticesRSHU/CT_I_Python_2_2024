# from my_classes import Student
# student1=Student("Irina","Sagaidachna")
# print(student1)
# Інкапсуляція, Поліморвфізм, Наслідування (Успадкування)

class Student:
    """
    Class about entity Student of University

    """
    # змінна класу static
    count_students=0
    # конструктор класу
    def __init__(self,first_name="NoName", second_name="NoSeconName",age=17):
        #властивості (атрибути) екземплря класу
        # private => приватний доступ
        self.__first_name=first_name  #attr class
        self.__second_name=second_name #attr class
        self.__age=age #attr class
        Student.count_students+=1
        print("Created object number #",Student.count_students)

    def __del__(self):
        Student.count_students-=1
        print(f"Deleted  info about {self.__second_name} {self.__first_name}.\n Залишилося студентів {Student.count_students}")

    #представлення обєкта в рядковому форматі
    def __str__(self):
        return f"Student: {self.__second_name} {self.__first_name} {self.__age} yeas old"

    #getter, setter
    def get_first_name(self):
        return self.__age
    
    def set_first_name(self,first_name):
        if first_name:
            self.__first_name=first_name
        else:
            print("Firstname must be not empty!!!")
        
    def get_second_name(self):
        return self.__second_name
    
    def set_second_name(self,second_name):
        if second_name:
            self.__second_name=second_name
        else:
            print("Firstname must be not empty!!!")

    def get_age(self):
        return self.__age
    
    def set_age(self,age):
        if age>=14:
            self.__age=age
        else:
            print("Age must be > 14")

    def learning(self,count_lessons):
        print(f"Зараз {self.__second_name} {self.__first_name} має {count_lessons} уроків")

    def eating(self,*foods):
        print(f"Зараз {self.__second_name} {self.__first_name} їсть {foods}")
    
    # # method of class => static
    # def print_count_students():
    #     print(f"count of students =  {Student.count_students}")


class Student2:
    """
    Class about entity Student of University

    """
    # змінна класу static
    count_students=0
    # конструктор класу
    def __init__(self,first_name="NoName", second_name="NoSeconName",age=17):
        #властивості (атрибути) екземплря класу
        # private => приватний доступ
        self.__first_name=first_name  #attr class
        self.__second_name=second_name #attr class
        self.__age=age #attr class
        Student2.count_students+=1
        print("Created object number #",Student2.count_students)

    def __del__(self):
        Student.count_students-=1
        print(f"Deleted  info about {self.__second_name} {self.__first_name}.\n Залишилося студентів {Student2.count_students}")

    #представлення обєкта в рядковому форматі
    def __str__(self):
        return f"Student: {self.__second_name} {self.__first_name} {self.__age} yeas old"

    #getter, setter  by property using decorator
    @property
    def first_name(self):
        return self.__age
    
    @first_name.setter
    def first_name(self,first_name):
        if first_name:
            self.__first_name=first_name
        else:
            print("Firstname must be not empty!!!")
        
    @property
    def second_name(self):
        return self.__second_name
    
    @second_name.setter
    def second_name(self,second_name):
        if second_name:
            self.__second_name=second_name
        else:
            print("Firstname must be not empty!!!")

    @property
    def age(self)->int:
        return self.__age
    
    @age.setter
    def age(self,age):
        if age>=14:
            self.__age=age
        else:
            print("Age must be > 14")

    def learning(self,count_lessons):
        print(f"Зараз {self.__second_name} {self.__first_name} має {count_lessons} уроків")

    def eating(self,*foods):
        print(f"Зараз {self.first_name} {self.second_name} їсть {foods}")
    



student1=Student("Olga","Svistun",20)
print(student1)
# student1.__age=9
# print(student1.__age)
# student1.age=2
# print(student1.age)
student1.learning(3)
student1.set_age(21)
print("Changed age 1:",student1)
student1.set_age(10)
print("Changed age 2:",student1)
print(student1.get_age())
# =============using Student2
student2=Student2("Ganna","Chorniy",19)
print(student2)
student2.age=student2.age+2
print("Changed age 1:",student2.age)
student2.second_name="Korovay"
print("Changed second name2:",student2.second_name)

print("Finish!!!")