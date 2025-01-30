# 1. Print "Hello, World!"
print("Hello, World!")

# 2. Calculate the sum of two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum:", num1 + num2)

# 3. Find the square of a number
num = int(input("Enter a number: "))
print("Square:", num ** 2)

# 4. Accept the user's name and greet them
name = input("Enter your name: ")
print("Hello,", name + "!")

# 5. Check whether a number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 6. Return a new list with unique elements of the first list
def unique_list(lst):
    return list(set(lst))

lst = list(map(int, input("Enter list elements separated by space: ").split()))
print("Unique List:", unique_list(lst))

# 7. Convert Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

# 8. Calculate the area of a circle
import math
radius = float(input("Enter radius: "))
print("Area of Circle:", math.pi * radius ** 2)

# 9. Reverse a given string
string = input("Enter a string: ")
print("Reversed String:", string[::-1])

# 10. Check if a number is a prime number
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print("Prime")
else:
    print("Not Prime")

# 11. Calculate the factorial of a number
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

num = int(input("Enter a number: "))
print("Factorial:", factorial(num))

# 12. Find the largest item from a given list
lst = list(map(int, input("Enter list elements separated by space: ").split()))
print("Largest number:", max(lst))

# 13. Check whether a number is in a given range
num = int(input("Enter a number: "))
low, high = map(int, input("Enter range (low high): ").split())
if low <= num <= high:
    print(f"{num} is in the range [{low}, {high}]")
else:
    print(f"{num} is not in the range [{low}, {high}]")

# 14. Calculate the number of uppercase and lowercase letters in a string
string = input("Enter a string: ")
upper = sum(1 for c in string if c.isupper())
lower = sum(1 for c in string if c.islower())
print(f"Uppercase letters: {upper}, Lowercase letters: {lower}")