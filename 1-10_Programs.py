
"""
#Program 1
#Print Hello World
print("Hello, World!")


#Program 2
#Sum of two numbers
a= 23
b= 43
c= a + b

print("Sum of 2 numbers is:", c)


#Program 3
#Perform arithmetic operations on two numbers
d= 45
e= 97

total_sum=d+e
product= d*e
difference=d-e
quotient=d/e

print("Sum of two numbers is:", total_sum)
print("Product of two numbers is:", product)
print("Difference of two numbers is:", difference)
print("Quotient of two numbers is:", quotient)


#Program 4
#Calculate area and circumference of a circle
radius = float(input("Enter radius of a circle: "))

pi= 3.14

area = pi*radius*radius
circumference=2 * pi * radius

print("The area of circle is:", area, "square units")
print("The circumference of circle is:", circumference, "units")


# Program 5
# Calculate area of a rectangle
length = int(input("Enter the length of rectangle: "))
breadth = int(input("Enter the breadth of rectangle: "))

area = length * breadth

print("Area of rectangle is:", area)


# Program 6
# Swap two variables using a third variable
a = int(input("Enter a value for variable A: "))
b = int(input("Enter a value for variable B: "))

print("Stored value in A is:", a)
print("Stored value in B is:", b)

c = a
a = b
b = c

print("After swapping:")
print("Stored value in A is:", a)
print("Stored value in B is:", b)


# Program 7
# Swap two variables without using a third variable
num1 = int(input("Enter number to store in num1: "))
num2 = int(input("Enter number to store in num2: "))

num1, num2 = num2, num1

print("After swapping:", num1, num2)


# Program 8
# Convert Celsius into Kelvin
temp1 = float(input("Enter temperature in Celsius: "))

temp2 = temp1 + 273.15

print("Temperature in Kelvin is:", temp2, "K")


# Program 9
# Calculate total marks, average and percentage
marks1 = int(input("Enter marks of subject 1: "))
marks2 = int(input("Enter marks of subject 2: "))
marks3 = int(input("Enter marks of subject 3: "))
marks4 = int(input("Enter marks of subject 4: "))
marks5 = int(input("Enter marks of subject 5: "))

total = marks1 + marks2 + marks3 + marks4 + marks5

average = total / 5
percentage = total * 100 / 500

print("Your total marks are:", total)
print("Your percentage is:", percentage, "%")
print("The average is:", average)


# Program 10
# Convert seconds into minutes and hours
seconds = int(input("Enter seconds: "))

print("Your entered seconds are:", seconds)

minutes = seconds / 60
print("Seconds converted into minutes are:", minutes)

hours = minutes / 60
print("Seconds converted into hours are:", hours)
"""