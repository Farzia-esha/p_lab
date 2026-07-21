#task:count num
count=0
num=7876
while num!=0:
    num=num//10
    
    print("hi",num)
    count=count+1
print("Number of digit:",count)

#factorial calculator
def factcalculator(value):
    fac=1
    for i in range(1,value+1):
        fac=fac*i
        print(fac)
factcalculator(4) 

# 4. Check Leap Year
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")


#Check if a number is prime or not        
# 5.Prime Number Check
num = int(input("Enter a number: "))
if num <= 1:
    print("Not Prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")

# 5. Function to check prime
def is_prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1

    if count == 2:
        return True
    else:
        return False

num = int(input("Enter a number: "))

if is_prime(num):
    print("Prime")
else:
    print("Not Prime")

# 2. Sum of digits of a number
n = int(input("Enter a number: "))
total = 0

while n > 0:
    digit = n % 10
    total += digit
    n = n // 10

print("Sum of digits =", total)

#task
x = int(input("Enter a numebr :"))

if x==1:
    print("One")
elif x==2:
    print("Two")
elif x==3:
    print("Three")
elif x==4:
    print("Four")
else:
    print("Otherwise")

# 4.Count Vowels
text = input("Enter a string: ")
count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print("Total vowels:", count)

#positive or negative.
Number = int(input("Enter a number to check:"))

if Number>=0:
    print("This is posative number")
else:
    print("This is negative number")


# 5.Fibonacci Series(first N terms)
n = int(input("Enter number of terms: "))

a = 0
b = 1
count = 0

while count < n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    count += 1


#find the greatest number from them. 
number1 = int(input("Enter the first number:"))
number2 = int(input("Enter the second number:"))
number3 =int(input("Enter the third number:"))

if number1>number2 and number1>number3:
    print(number1," is greater number.")
elif number2>number1 and number2>number3:
    print(number2," is greater number.")
else:
    print(number3," is greater number.")
x = int(input("Enter a number to check:"))

if x%2 == 0:
    print("This is even number")
    if x >= 10:
        print("This is also greater than 10")
    else:
        print("This is less than 10")
else:
    print("This is not even number")
    if x >= 10:
        print("This is also greater than 10")
    else:
        print("This is less than 10")

#Print the number between 1 to 100 but skip the number that are divisible by 3 or 5.
# Same thing using for loop .
for x in range(1,101):
    if x % 3 != 0 and x % 5 != 0:
        print(x,",",end="")
i = 0
while i < 5:
    print("Inside the loop ",i)
    if i == 3:
        break
    i += 1
print("Out of the loop")
i=0;
while i<5:
    if i==3:
        break
    print("Inside the loop, value of i",i)
    i+=1
#Ex: Print the number from 1 to 100. Skip the number which are divisible by 3 and 5.
x = 1
while x <= 100:
    if x %3 == 0 or x % 5 == 0:
        x += 1 
        continue
    print(x,",",end="")
    x = x+1

 #BMI calculator
height = float(input("Enter your height : "))
weight = int(input("Enter your weight :"))

bmi = weight / (height**2)
print("Your BMI is: ",int(bmi),end="")
if bmi < 18.5:
    print(" Underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print(" Normal Weight")
elif bmi >= 25 and bmi <= 19.9:
    print(" Overweight")
else:
    print(" Obese")

# numpy
import numpy as np
l=np.arange(1,6)
print(l)
np.ones(3)
np.random.rand(5,5)


#palindrome check
def is_palindrome(s):
    return s == s[::-1]

word = input("Enter text: ")

if is_palindrome(word):
    print("Palindrome")
else:
    print("Not Palindrome")

#palindrome ignore case & space
text = input("Enter text: ")

clean = text.lower().replace(" ", "")

if clean == clean[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")