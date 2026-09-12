import subprocess as sb
sb.run("cls", shell=True)
print("Welcome to the OOP Assignment 04")
class Person:
    # Class variable
    era = "21st Century."
    def __init__(self, name, age):
        print("Initializing Person class")
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Era: {self.era}")

    @classmethod
    def change_era(cls, new_era):
        cls.era = new_era

    @staticmethod
    def greet(i=0):
        print("\n########################")
        print(f"Person {i+1}:")

# Example usage:
person1 = Person("Alice", 30)
# person1.display_info()
# Example of inheritance
class Student(Person):
    def __init__(self, name, age, student_id):
        print("Initializing Student class")
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")

# Example usage:
student1 = Student("Bob", 20, "S12345")
# student1.display_info()

# Example of polymorphism
class Teacher(Person):
    def __init__(self, name, age, subject):
        print("Initializing Teacher class")
        super().__init__(name, age)
        self.subject = subject

    def display_info(self):
        super().display_info()
        print(f"Subject Expertize: {self.subject}")

# Example usage:
teacher1 = Teacher("Charlie", 40, "Mathematics")
#teacher1.display_info()

persons = [person1, student1, teacher1]
i = 0
for person in persons:
    Person.greet(i)
    if i == 1:
        Person.change_era("22nd Century.")
    person.display_info()
    i += 1