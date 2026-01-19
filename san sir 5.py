#Task 1: Identify if the inputted character is alphabet, number, or special character

char = input("Enter a character: ")

if char.isalpha():
    print("It is an alphabet.")
elif char.isdigit():
    print("It is a number.")
else:
    print("It is a special character.")

#Task 2: Identify if the inputted character is vowel or consonant

char = input("Enter an alphabet: ").lower()

if char.isalpha():
    if char in 'aeiou':
        print("It is a vowel.")
    else:
        print("It is a consonant.")
else:
    print("Invalid input. Please enter an alphabet.")

#Task 3: Demonstrate a function passing argument and showing calculation with 
# passed parameters

def calculate_total(price, quantity):
    total = price * quantity
    return total

price = float(input("Enter price of item: "))
quantity = int(input("Enter quantity: "))
result = calculate_total(price, quantity)
print("Total amount is:", result)

def calculate_total(price, quantity):
    total = price * quantity
    return total

price = float(input("Enter price of item: "))
quantity = int(input("Enter quantity: "))
result = calculate_total(price, quantity)
print("Total amount is:", result)

#Task 4: Count the number of blank spaces within a string

text = input("Enter a string: ")
count = 0

for ch in text:
    if ch == " ":
        count += 1

print("Number of blank spaces:", count)

#Task 5:  Easy student info program

name = input("Enter student name: ")
roll = input("Enter student roll/ID: ")
course = input("Enter course name: ")

print("\n--- Student Information ---")
print("Name   :", name)
print("Roll/ID:", roll)
print("Course :", course)
