# -*- coding: utf-8 -*-
"""Assignment1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15AGHtLDxv0z_HvfZZjP7RnVxMDMs-ky7

Nisarga H R

Assignment 1

1. Understanding Variables
a) Define a variable in Python. Provide an example of how to create a variable that stores your name.
b) What is the difference between a variable and a constant? Can we have constants in Python?

1a) Python variables are containers that store values.
"""

name = "Nisarga H R"
print(name)

"""1b) Python variables stores values that can change during program execution whereas constants are representations of fixed values in a program.
Python does not contain any constants.Any variable written in the upper case is considered as a constant in python.

2a)Working with Different Data Types
 Create variables of the following types in Python:
1. Integer
2. Float
3. String
4. Boolean
"""

age = 25
print(age)

print(type(age))

pi = 3.14
print(pi)

print(type(pi))

name = 'Nisarga H R'
print(name)

print(type(name))

x = 5
y = 10
is_greater = x > y
print(is_greater)

print(type(is_greater))

"""2b) Write a Python script to display the type of each variable you created."""

age = 25
print(age)

pi = 3.14
print(pi)

name = 'Nisarga H R'
print(name)

x = 5
y = 10
is_greater = x > y
print(is_greater)

"""3. Arithmetic Operators

a) Explain the following arithmetic operators with examples:
1. Addition (`+`)
2. Subtraction (`-`)
3. Multiplication (``)
4. Division (`/`)
5. Floor Division (`//`)
6. Modulus (`%`)
7. Exponentiation (``)

1.Addition
"""

a = 5
b = 2
result = a + b
print(result)

"""2. Subtraction"""

a = 7
b = 2
result = a - b
print(result)

"""3. Multiplication"""

a = 3
b = 2
result = 3 * 2
print(result)

"""4. Division"""

a = 10
b = 2
result = a/b
print(result)

"""5. Floor Division"""

a = 10
b = 3
result= a//b
print(result)

"""6. Modulus"""

a = 10
b = 3
result = a % b
print(result)

"""7. Exponentiation"""

a = 2
b = 3
result = a ** b
print(result)

"""3b)  Write a Python script to calculate the area of a rectangle using variables `length` and `width` with
values 5 and 10, respectively. Use the multiplication operator.
"""

length = 5
width = 10
area = length * width
print("The area of the rectangle is:",area)

"""4.  Comparison and Logical Operators

a) Explain the following comparison operators with examples:
1. Equal to (`==`)
2. Not equal to (`!=`)
3. Greater than (`>`)
4. Less than (`<`)
5. Greater than or equal to (`>=`)
6. Less than or equal to (`<=`)

1. Equal to
"""

a = 5
b = 5
result = a == b
print(result)

"""2. Not equal to"""

a = 5
b = 3
result = a != b
print(result)

"""3. Greater than"""

a = 7
b = 3
result = a > b
print(result)

"""4. Less than"""

a = 2
b = 4
result = a < b
print(result)

"""5. Greater than or equal to"""

a = 5
b = 3
result = a >= b
print(result)

a = 3
b = 3
result = a >= b
print(result)

"""Less than or equal to"""

a = 6
b = 8
result = a <= b
print(result)

a = 8
b = 8
result = a <= b
print(result)

"""4b)  Using logical operators (`and`, `or`, `not`), write a Python script that checks if a number is positive
and even.

"""

num = int(input("Enter a number:"))
if num > 0 and num % 2 == 0:
 print(f"{num} is a positive and even number.")
else:
   print(f"{num} is neither a positive nor a even number.")

"""5.  Type Casting in Python

a) What is type casting? Explain the difference between implicit and explicit type casting with examples.

Type casting, also known as type conversion, refers to the process of converting a variable from one data type to another.

Implicit type casting, also known as automatic type casting or type promotion, occurs automatically by the interpreter or compiler when a data type is required to be converted to another type without the programmer’s intervention.
"""

a = 5
b = 2.0
result = a + b
print(result)

"""Explicit type casting is where the programmer manually converts one data type to another using built-in functions or methods."""

a = 5
b = 2.0
b_as_int = int(b)
result = a + b_as_int
print(result)

"""5b) Write a Python script that:
1. Converts a float to an integer.
2. Converts an integer to a string.
3. Converts a string to a float.

1. Converts a float to an integer
"""

float_num = 123.45
int_num = int(float_num)
print(f"Float {float_num} converted to integer: {int_num}")

"""2. Converts an integer to a string.

"""

int_num = 123
str_num = str(int_num)
print(f"Integer {int_num} converted to string: {str_num}")

"""3. Converts a string to a float."""

str_num = "123"
float_num = float(str_num)
print(f"String {str_num} converted to float: {float_num}")

"""6. Practical Exercise: Mini Calculator

Write a Python script that asks the user to input two numbers and then:
1. Adds the two numbers and prints the result.
2. Subtracts the second number from the first and prints the result.
3. Multiplies the two numbers and prints the result.
4. Divides the first number by the second and prints the result (handle division by zero).
5. Converts the sum of the numbers to a string and prints the type of the result.

"""

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
sum_result = num1 + num2
print(f"The sum of {num1} and {num2} is {sum_result}")
subtraction_result = num1 - num2
print(f"The result of subtracting {num2} from {num1} is {subtraction_result}")
multiplication_result = num1 * num2
print(f"The result of multiplying {num1} and {num2} is {multiplication_result}")
division_result = num1 / num2
print(f"The result of dividing {num1} by {num2} is {division_result}")
print("Error: Division by zero is not allowed.")
sum_as_str = str(sum_result)
print(f"The sum converted to a string is '{sum_as_str}' and its type is {type(sum_as_str)}")