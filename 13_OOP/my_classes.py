class Student:
    """
    Class about entity Student of University

    """
    # змінна класу static
    count_students=0
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
    # print(sys.path)
