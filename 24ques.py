# Task 1: Function that takes a list of integers and returns True if all numbers are unique
def all_unique(numbers):
    return len(numbers) == len(set(numbers))
print(all_unique([1, 2, 3]))
print(all_unique([1, 2, 2]))

# Task 2: Prompt user to enter lap time and check if below 50.5 seconds
time = float(input("Enter lap time: "))
if time < 50.5:
    print("Below standard time")
else:
    print("Not below standard time")

# Task 3: Prompt user to enter strings until empty input, then display in reverse order
strings = []
while True:
    s = input()
    if s == "":
        break
    strings.append(s)
for s in reversed(strings):
    print(s)

# Task 4: Prompt user to enter integer and display if positive, negative, or zero
num = int(input())
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Task 5: Function that checks if one of the strings is "coconut"
def contains_coconut(words):
    return "coconut" in words
print(contains_coconut(["apple", "banana"]))
print(contains_coconut(["coconut", "mango"]))

# Task 6: Prompt user to enter integers until empty input, display how many are even
count_even = 0
while True:
    s = input()
    if s == "":
        break
    if int(s) % 2 == 0:
        count_even += 1
print(count_even)

# Task 7: Prompt user to enter a string and check if it is a palindrome
s = input()
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")

# Task 8: Function that returns maximum value in a list of integers
def max_value(numbers):
    return max(numbers)
print(max_value([1, 5, 3]))

# Task 9: Prompt user to enter integer and check if divisible by both 3 and 7
num = int(input())
if num % 3 == 0 and num % 7 == 0:
    print("Divisible by both 3 and 7")
else:
    print("Not divisible by both")

# Task 10: Prompt user to enter strings until empty input, count unique strings
strings = set()
while True:
    s = input()
    if s == "":
        break
    strings.add(s)
print(len(strings))

# Task 11: Prompt user to enter integer and display if odd or even
num = int(input())
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Task 12: Function that checks if list is sorted in ascending order
def is_sorted(numbers):
    return numbers == sorted(numbers)
print(is_sorted([1, 2, 3]))
print(is_sorted([3, 2, 1]))

# Task 13: Prompt user to enter strings until empty input, display longest string
strings = []
while True:
    s = input()
    if s == "":
        break
    strings.append(s)
print(max(strings, key=len))

# Task 14: Prompt user to enter integer and check if multiple of 5
num = int(input())
if num % 5 == 0:
    print("Multiple of 5")
else:
    print("Not a multiple of 5")

# Task 15: Function that checks if all strings start with capital letter
def all_capital(words):
    return all(w[0].isupper() for w in words)
print(all_capital(["Apple", "Banana"]))
print(all_capital(["apple", "Banana"]))

# Task 16: Prompt user to enter strings until empty input, display lowercase alphabetical order
strings = []
while True:
    s = input()
    if s == "":
        break
    strings.append(s.lower())
for s in sorted(strings):
    print(s)

# Task 17: Prompt user to enter string and display number of vowels
s = input()
vowels = "aeiouAEIOU"
count = sum(1 for ch in s if ch in vowels)
print(count)

# Task 18: Function that checks if all integers are between 0 and 100 inclusive
def all_in_range(numbers):
    return all(0 <= n <= 100 for n in numbers)
print(all_in_range([10, 50, 100]))
print(all_in_range([10, 150]))

# Task 19: Prompt user to enter exam mark and check if pass (>=40)
mark = int(input())
if mark >= 40:
    print("Pass")
else:
    print("Fail")

# Task 20: Function that checks if list contains no empty strings
def no_empty_strings(words):
    return all(w != "" for w in words)
print(no_empty_strings(["apple", "banana"]))
print(no_empty_strings(["apple", ""]))

# Task 21: Prompt user to enter integers until empty input, display sum
total = 0
while True:
    s = input()
    if s == "":
        break
    total += int(s)
print(total)

# Task 22: Prompt user to enter string and check if palindrome
s = input()
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")

# Task 23: Function that returns average of integers in list
def average(numbers):
    return sum(numbers) / len(numbers)
print(average([1, 2, 3, 4]))

# Task 24: Prompt user to enter strings until empty input, display average length
strings = []
while True:
    s = input()
    if s == "":
        break
    strings.append(s)
avg_length = sum(len(s) for s in strings) / len(strings)
print(avg_length)

# Task 25: Prompt user to enter integer and display if positive, negative, or zero
num = int(input())
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
