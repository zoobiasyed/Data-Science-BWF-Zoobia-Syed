# Exercise 1-CLASSES AND OBJECTS
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

car1 = Car("Toyota", "Corolla", 2020)
print(f"Car Make: {car1.make}, Model: {car1.model}, Year: {car1.year}")

# Exercise 2-INHERITENCE
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

student1 = Student("Zoobia", 22, "B12345")
print(f"Name: {student1.name}, Age: {student1.age}, Student ID: {student1.student_id}")

# Exercise 3-Encapsulation
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

account1 = BankAccount("1234567890", 1000)
account1.deposit(500)
print(f"Balance after deposit: {account1.get_balance()}")
account1.withdraw(300)
print(f"Balance after withdrawal: {account1.get_balance()}")
