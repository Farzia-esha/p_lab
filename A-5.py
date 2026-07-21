#PART 1: Encapsulation Real Life Problem
#Problem 1: Bank Account System
class BankAccount:
    def __init__(self, name, balance):
        self.name = name  # public variable
        self.__balance = balance  # private variable
    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
    # Withdraw method
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient Balance!")
# Getter method
    def get_balance(self):
        return self.__balance
# Creating object
account = BankAccount("xyz", 9000)
# Accessing methods
account.deposit(1000)
account.withdraw(500)
# Accessing balance
print("Current Balance:", account.get_balance())



#Problem 2: ATM Machine
class ATM:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        # Private attribute
        self.__balance = initial_balance

    # Controlled interaction through explicit options
    def check_balance(self):
        return f"Your current balance is: ${self.__balance}" 
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Successfully withdrew ${amount}.")
        else:
            print("Insufficient Amount!")
# Usage
my_atm = ATM("xyz", 1000)
# print(my_atm.__balance) # Error! Cannot access directly. print(my_atm.check_balance())
my_atm.withdraw(200)


#Problem 3: Student Result System
class StudentResult:
    def __init__(self, name):
        self.name = name
        self.__gpa = 0.0
    def update_gpa(self, gpa):
        if 0 <= gpa <= 4.0:
            self.__gpa = gpa
        else:
            print("Invalid GPA!")
    def get_gpa(self):
        return self.__gpa
# Create object
s1 = StudentResult("Suborna Akter")
# Update GPA
s1.update_gpa(3.82)
# Display result
print("Student:", s1.name)
print("GPA:", s1.get_gpa())



#Problem 4: Online Shopping Cart
class ShoppingCart:
    def __init__(self):
        self.__total_price = 0

    def add_product(self, price):
        self.__total_price += price

    def get_total(self):
        return self.__total_price
cart = ShoppingCart()
cart.add_product(500)
cart.add_product(1000)
print("Total Price:", cart.get_total())



#Problem 5: Hospital Management System
class Patient:
    def __init__(self, name, disease):
        self.name = name
        self.__disease = disease

    def view_record(self):
        return f"{self.name} - {self.__disease}"

    def update_disease(self, disease):
        self.__disease = disease

p1 = Patient("Rahim", "Fever")
print(p1.view_record())
p1.update_disease("Diabetes")
print(p1.view_record())



#PART 2: Inheritance Real Life Problem
#Problem 1: Single Inheritance - Person and Student
# Parent Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Child Class
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age) # Inherit attributes from Person
        self.student_id = student_id

    def show_student(self):
        self.show_person()
        print("Student ID:", self.student_id)

# Object Creation
s1 = Student("Suborna Akter", 22, "B210305047")
s1.show_student()


#Problem 2: Multiple Inheritance
# First parent class
class Teacher:
    def teach(self):
        print("Teaching students")


# Second parent class
class Researcher:
    def research(self):
        print("Conducting research")


# Child class inheriting from both parents
class Professor(Teacher, Researcher):
    def manage(self):
        print("Managing academic activities")


# Creating object
p1 = Professor()

# Accessing methods from both parent classes
p1.teach()
p1.research()
p1.manage()



#Problem 3: Multilevel Inheritance
# Grandparent Class
class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)


# Parent Class
class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

    def show_employee(self):
        print("Employee ID:", self.emp_id)


# Child Class
class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department

    def show_details(self):
        self.show_name()
        self.show_employee()
        print("Department:", self.department)


# Object Creation
m1 = Manager("Suborna", "EMP101", "IT")
m1.show_details()



#Problem 4: Hierarchical inheritan
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)
class Student(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id

    def display_student(self):
        self.display_person()
        print("ID:", self.id)
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    def display_teacher(self):
        self.display_person()
        print("Subject:", self.subject)
# Objects
s = Student("Suborna Akter", 22, "B210305047")
t = Teacher("Manowar Sir", 40, "Python")
print("Student Information:")
s.display_student()
print("\nTeacher Information:")
t.display_teacher()



#Problem 5: Hybrid Inheritance
# Base class
class Person:
    def show_person(self):
        print("I am a person")


# First child class
class Teacher(Person):
    def teach(self):
        print("Teaching students")


# Second child class
class Researcher(Person):
    def research(self):
        print("Conducting research")


# Child class inheriting from both classes
class Professor(Teacher, Researcher):
    def manage(self):
        print("Managing university activities")


# Creating object
p1 = Professor()

# Accessing methods
p1.show_person()
p1.teach()
p1.research()
p1.manage()



#PART 3: Polymorphism Real Life Problem
#Problem 1: Transportation System
class Car:
    def move(self):
        print("Car is driving")
class Boat:
    def move(self):
        print("Boat is sailing")
class Plane:
    def move(self):
        print("Plane is flying")

vehicles = [Car(), Boat(), Plane()]
for vehicle in vehicles:
    vehicle.move()



#Problem 2: Method Overriding
from math import pi
class Shape:
    def __init__(self, name):
        self.name = name
    def area(self):
        pass
    def fact(self):
        return "I am a two-dimensional shape."
    def __str__(self):
        return self.name
class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length ** 2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2
# Creating objects
a = Square(4)
b = Circle(7)
print(b)
print(b.fact())
print(a.fact())
print(b.area())



#Problem 3: Operator Overloading
class Student:
    def __init__(self, marks):
        self.marks = marks
    def __add__(self, other):
        return self.marks + other.marks
s1 = Student(80)
s2 = Student(90)
print(s1 + s2)



#PART 4: Data Abstraction Real Life Problem
#Problem 1: The Payment System
from abc import ABC, abstractmethod
# Abstract Class
class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
# Child Class 1
class CreditCard(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing Credit Card payment of ${amount}")
# Child Class 2
class PayPal(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")
# Objects
card = CreditCard()
btc = PayPal()
card.process_payment(500)
btc.process_payment(400)