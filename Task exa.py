# Task 1

**Course:** Programming Fundamentals  
**Student ID/Email:** the@example.com  

I am submitting Exam Paper 2.

# Task 2
# How I Work Best in Programming

## Preferred Tools
I usually work with **VS Code**, Git, and Python. These tools make me feel *productive* and organized.

## Environment
I prefer a quiet environment with minimal distractions. Having a comfortable chair and good lighting helps me stay focused.

### Key Factors
- **Consistency**: I like to follow a routine.  
- *Breaks*: Short breaks keep my mind fresh.  
- Collaboration: Discussing ideas with peers improves my understanding.  

## Summary
In short, I work best when I have the right tools, a calm environment, and a structured workflow.

# Task 3: Prompt user for exam mark and check pass/fail
mark = int(input("Enter your exam mark: "))

if mark >= 40:
    print("Pass")
else:
    print("Fail")

# Task 4: Function to check if 'coconut' is in the list
def contains_coconut(strings):
    return "coconut" in strings

# Demonstration
test_list1 = ["apple", "banana", "coconut"]
test_list2 = ["apple", "banana", "orange"]

print(contains_coconut(test_list1))  # True
print(contains_coconut(test_list2))  # False

# Task 5: Collect strings until empty input, then display sorted lowercase list
strings = []

while True:
    s = input("Enter a string (press Enter to stop): ")
    if s == "":
        break
    strings.append(s.lower())

strings.sort()

print("Strings in alphabetical order:")
for word in strings:
    print(word)

