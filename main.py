# Python Calculator
# Project 2 - Learning Python
import sys

print("Welcome to my Python Calculator!")
print()
print("===== CALCULATOR MENU =====")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("===============================")
print()

choice = input("Choose an operation (1-4): ")
if choice not in ["1", "2", "3", "4"]:
    print("Invalid choice. Please select 1-4")
    sys.exit()
name = input("What is your name? ")
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Error: Please enter valid numbers.")
    sys.exit()

if choice == "1":
    print("You selected Addition.")
    result = num1 + num2
    print(f"Result: {result}")
elif choice == "2":
    print("You selected Subtraction.")
    result = num1 - num2
    print(f"Result: {result}")
elif choice == "3":
    print("You selected Multiplication.")
    result = num1 * num2
    print(f"Result: {result}")
elif choice == "4":
    print("You selected Division.")
    if num2 == 0:
        print("Error: Cannot divide by zero!")
    else:
        result = num1 / num2
        print(f"Result: {result}")
else:
    print("Invalid choice. Please select 1-4")

print(f"You selected option {choice}")
print(name, ", you selected option", choice)

