# Exercise 1 part 1
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits)

# Exercise 1 part 2
fruits.append("fig")
print(fruits)

# Exercise 1 part 3
fruits.remove("banana")
print(fruits)

# Exercise 1 part 4
fruits.sort()
print(fruits)



# Exercise 2 part 1
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple)

# Exercise 2 part 2
print(my_tuple[2])  # Output: 30

# Exercise 2 part 3
try:
    my_tuple[1] = 25
except TypeError as e:
    print(e)  # Output: 'tuple' object does not support item assignment


# Exercise 3 part 1
numbers = {1, 2, 3, 4, 4, 5}
print(numbers)  # Output: {1, 2, 3, 4, 5}

# Exercise 3 part 2
numbers.add(6)
print(numbers)

# Exercise 3 part 3
numbers.remove(3)
print(numbers)

# Exercise 3 part 4
print(2 in numbers)  # Output: True
print(7 in numbers)  # Output: False


# Exercise 4 part 1
student = {"name": "Ali", "age": 22, "courses": ["Math", "CompSci"]}
print(student)

# Exercise 4 part 2
student["grade"] = "A"
print(student)

# Exercise 4 part 3
student["age"] = 23
print(student)

# Exercise 4 part 4
del student["courses"]
print(student)
