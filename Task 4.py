# Exercise 1 part 1
print("Hello, World!")


# Exercise 1 part 2
name = "Zoobia"
age = 22
favorite_color = "green"

print(f"My name is {name}, I am {age} years old, and my favorite color is {favorite_color}.")


# Exercise 2 part 1
number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# Exercise 2 part 2
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_ = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2

print(f"Sum: {sum_}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Quotient: {quotient}")


# Exercise 2 part 3
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
