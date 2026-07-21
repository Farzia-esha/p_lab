#1. bank
class BankAccount:
    def __init__(self, name, balance):
        self.name = name          # public variable
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
account = BankAccount("Rahim", 5000)

# Accessing methods
account.deposit(2000)
account.withdraw(1000)

# Accessing balance using method
print("Current Balance:", account.get_balance())  

#ex:2 file handling
try:
    file = open("geek.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError as e:
    print("Error:", e)
finally:
    file.close()


#Ex:3 Exception handling
try:
    data = open("file.txt", "r").read()
    result = 10 / int(data)
except FileNotFoundError:
    print("The file is missing.")
except ValueError:
    print("The file contains non-numeric data.")
except ZeroDivisionError:
    print("You cannot divide by zero.")

#Exception handling with multi exceptions
try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ValueError:
    print("You must enter a number.")
except ZeroDivisionError:
    print("You cannot divide by zero.")

# another ex
try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ValueError:
    print("You must enter a number.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
def check_age(age):
    if age < 18:
        raise ValueError("You must be 18 or older.")
    print("Access granted.")

try:
    check_age(16)
except ValueError as e:
    print(e)

#another ex
file_path = 'numbers.txt'
total_sum = 0

with open(file_path, 'r') as file:
    lines = file.readlines()

for line in lines:
    number = int(line.strip())  # Convert each line to an integer
    total_sum += number         # Add the integer to total_sum

# task
print("The sum of the numbers is:", total_sum)
import pandas as pd
s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(s)
print(s.sort_values())  # Sort by values
print(s.sort_index())

#task
import pandas as pd

# create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 32, 18, 47, 33],
    'City': ['New York', 'Paris', 'London', 'Tokyo', 'Sydney']
}
df = pd.DataFrame(data)

# access the Name column
names = df['Name']

print(names)
df[['Name','Age']]

#task

row_list = df.loc[[0, 3, 4]]
row_list
column_list = df.loc[:,['Name', 'Age']]
column_list
single_row = df.iloc[2]
single_row
boolean_index = df.loc[df['Age'] > 30]
boolean_index

#task 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Generate random data for the histogram
data = np.random.randn(1000)

# Creating a customized histogram with a density plot
sns.histplot(data, bins=30, kde=True, color='lightgreen', edgecolor='red')

# Adding labels and title
plt.xlabel('Values')
plt.ylabel('Density')
plt.title('Customized Histogram with Density Plot')

# Display the plot
plt.show()

#task
from random import randint
import numpy as np

# Generate two lists of 16 random integers
list1 = [randint(1, 20) for i in range(16)]
list2 = [randint(1, 20) for i in range(16)]

# Convert lists to NumPy arrays
array1 = np.array(list1)
array2 = np.array(list2)

# Reshape into 4×4 matrices
array1 = array1.reshape(4, 4)
array2 = array2.reshape(4, 4)

# Element-wise operations
addition = array1 + array2
subtraction = array1 - array2
multiplication = array1 * array2

# Display results
print("Array 1:")
print(array1)

print("\nArray 2:")
print(array2)

print("\nAddition:")
print(addition)

print("\nSubtraction:")
print(subtraction)

print("\nMultiplication:")
print(multiplication)

#task
import pandas as pd

# Create DataFrame
data = {
    "Employee Name": ["Alice", "Bob", "Charlie", "David"],
    "Department": ["HR", "IT", "Finance", "Marketing"],
    "Salary": [50000, 65000, 60000, 70000],
    "Years of Experience": [3, 5, 4, 6]
}

df = pd.DataFrame(data)

# Display DataFrame
print("Employee Data:")
print(df)

# Average salary
average_salary = df["Salary"].mean()
print("\nAverage Salary:", average_salary)

# Employee with highest salary
highest_salary = df.loc[df["Salary"].idxmax()]

print("\nEmployee with Highest Salary:")
print(highest_salary)

#task
import matplotlib.pyplot as plt

# Subjects
subjects = ["Math", "Physics", "Chemistry", "Biology", "English", "ICT"]

# Marks of two students
student1 = [85, 90, 78, 88, 92, 95]
student2 = [80, 85, 82, 86, 89, 91]

# Plot line graph
plt.plot(subjects, student1, marker="o", linestyle="-", label="Student 1")
plt.plot(subjects, student2, marker="s", linestyle="--", label="Student 2")

# Title and labels
plt.title("Performance Comparison of Two Students")
plt.xlabel("Subjects")
plt.ylabel("Marks")

# Legend
plt.legend()

# Grid
plt.grid(True)

# Show graph
plt.show()

#task
# Ask user for filename
filename = input("Enter the filename: ")

try:
    file = open(filename, "r")
    content = file.read()

    print("\nFile Contents:")
    print(content)

    file.close()

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied to access the file.")

except Exception as e:
    print("An error occurred:", e)


#task
temps=[30,32,29,35,34,36,33,31,40,39]
count = 0
highest = temps[0]

for i in range(len(temps)):
    if(highest < temps[i] and temps[i]>temps[i-1]):
        print("Peak found at index", i, "with value", temps[i])
        count = count + 1

print("Total number of peaks", count)

#task
# Base class
class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.issued = False

    def issue_item(self):
        self.issued = True

    def display(self):
        print("Title:", self.title)
        print("ID:", self.item_id)
        print("Status:", "Issued" if self.issued else "Available")


# Derived class Book
class Book(LibraryItem):
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author

    # Method overriding
    def display(self):
        super().display()
        print("Type: Book")
        print("Author:", self.author)


# Derived class CD
class CD(LibraryItem):
    def __init__(self, title, item_id, duration):
        super().__init__(title, item_id)
        self.duration = duration

    # Method overriding
    def display(self):
        super().display()
        print("Type: CD")
        print("Duration:", self.duration, "minutes")
# Create objects
book1 = Book("Python Programming", 101, "James")
book2 = Book("Database System", 102, "Robert")
cd1 = CD("Python Tutorial", 201, 120)

# Issue items
book1.issue_item()
cd1.issue_item()

# Store all items
library = [book1, book2, cd1]


# Display issued items
def display_issued_items(items):
    print("Issued Items:")
    
    for item in items:
        if item.issued:
            item.display()
            print()


# Function call
display_issued_items(library)  


# task
def fahrenheit_to_celsius(fahrenheit_list):
    celsius_list = []

    for temp in fahrenheit_list:
        if isinstance(temp, (int, float)):
            c = (temp - 32) * 5 / 9
            celsius_list.append(round(c, 2))

    return celsius_list


fahrenheit = [32, 75, "missing", 100, 212]

celsius = fahrenheit_to_celsius(fahrenheit)

print("Fahrenheit:", fahrenheit)
print("Celsius:", celsius)

#task
student = {
    "Name": "Rahim",
    "Age": 20,
    "Department": "CSE"
}

for key, value in student.items():
    print(key, ":", value)

    #task
# Student records dataset
students = [
    {"id": 1, "name": "A", "marks": 78},
    {"id": 2, "name": "B", "marks": 91},
    {"id": 3, "name": "C", "marks": 67}
]

# Dictionary to store classified results
classified_students = {
    "A": [],
    "B": [],
    "C": [],
    "Fail": []
}

# Classify students based on marks
for student in students:
    marks = student["marks"]

    if marks >= 80:
        grade = "A"
    
    elif marks >= 70:
        grade = "B"
    
    elif marks >= 60:
        grade = "C"
    
    else:
        grade = "Fail"

    # Add student information to corresponding grade
    classified_students[grade].append(student)


# Display student grades
print("Student Grade Classification:")
for grade, students_list in classified_students.items():
    print("\nGrade", grade)
    
    for student in students_list:
        print(
            "ID:", student["id"],
            "Name:", student["name"],
            "Marks:", student["marks"]
        )
