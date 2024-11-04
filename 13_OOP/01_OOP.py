# Object => 
#          характеристики: property (field, attributes) => variables
#          дії: methods  =>  functions  def

class Student:
    """
    Class about entity Student of University

    """
    # змінна класу static
    count_students=0
    # def __init__(self):
    #     self.first_name="Ganna"
    #     self.second_name="Kozachok"
    # конструктор класу
    def __init__(self,first_name="NoName", second_name="NoSeconName"):
        #властивості (атрибути) екземплря класу
        self.first_name=first_name  #attr class
        self.second_name=second_name #attr class
        Student.count_students+=1
        print("Created object number #",Student.count_students)

    def __del__(self):
        Student.count_students-=1
        print(f"Deleted  info about {self.second_name} {self.first_name}.\n Залишилося студентів {Student.count_students}")

    #представлення обєкта в рядковому форматі
    def __str__(self):
        return f"Student: {self.second_name} {self.first_name}"

    def learning(self,count_lessons):
        print(f"Зараз {self.second_name} {self.first_name} має {count_lessons} уроків")

    def eating(self,*foods):
        print(f"Зараз {self.second_name} {self.first_name} їсть {foods}")
    
    # method of class => static
    def print_count_students():
        print(f"count of students =  {Student.count_students}")


if __name__=="__main__":
    # екземпляр (обєкт) клас Student 
    student1=Student("Ganna","Kozachok") 
    print(student1)
    print(student1.count_students)
    print(Student.count_students)
    student1.eating("каву","гамбургер")

    student1.marks=[5,4,5]
    print(student1.marks)
    # print(type(student1))
    # print("Info student=> ",student1.second_name, student1.first_name)

    student2=Student("Mikola","Tkachuk") #екземпляр класу Student
    print(student2)
    print(student2.count_students)
    student2.learning(4)
    # print(student2.marks) # Exception

    #явний виклик спеціальних  методів класу
    student3=Student("Viktoria", "Dzjubuk")
    print(student3.__str__())
    student3.second_name="Schedra"
    print(student3)
    student4=Student()
    print(student4)

    # student4.print_count_students()
    Student.print_count_students()



    # number=int("23") #10111
    # number=8 #1000
    # print(number.bit_count())
    # print(number.bit_length())

    print("Finished program...")