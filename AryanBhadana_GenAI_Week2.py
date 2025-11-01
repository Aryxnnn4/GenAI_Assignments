# GENAI Assignment - Week 2



# Task 1: Python Basics & Operators

# Accept two numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform basic arithmetic operations
print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")
print(f"Division: {num1 / num2}")
print(f"Modulus: {num1 % num2}")
print(f"Power: {num1 ** num2}")

# Comparison and Logical operators
print(f"{num1} > {num2}: {num1 > num2}")
print(f"{num1} < {num2}: {num1 < num2}")
print(f"{num1} == {num2}: {num1 == num2}")
print(f"{num1} != {num2}: {num1 != num2}")
print(f"Logical AND: {(num1 > 0) and (num2 > 0)}")
print(f"Logical OR: {(num1 > 0) or (num2 > 0)}")
print(f"Logical NOT on num1 positive: {not(num1 > 0)}")






# Task 2: Lists and Arrays

import numpy as np
import random

# Create a list of 10 random integers
numbers = [random.randint(1, 100) for _ in range(10)]
print("\nOriginal list:", numbers)

# Add and remove elements
numbers.append(200)
numbers.remove(numbers[0])
print("After adding 200 and removing first element:", numbers)

# Find maximum, minimum, and sort list
print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers))
numbers.sort()
print("Sorted list:", numbers)

# Convert list into NumPy array and calculate statistics
arr = np.array(numbers)
print(f"Mean: {np.mean(arr)}")
print(f"Median: {np.median(arr)}")
print(f"Standard Deviation: {np.std(arr)}")






# Task 3: Dictionaries and Sets

# Create dictionary named 'student'
student = {"name": "Student1", "course": "AI", "marks": 85}

# Add grade based on marks
if student["marks"] >= 80:
    student["grade"] = "A"
elif student["marks"] >= 60:
    student["grade"] = "B"
else:
    student["grade"] = "C"

# Print all keys and values using loop
print("\nStudent Details:")
for key, value in student.items():
    print(f"{key}: {value}")

# Create two sets of AI tools
set1 = {"ChatGPT", "Claude", "Bard"}
set2 = {"Gemini", "ChatGPT", "Copilot"}

print("\nUnion of sets:", set1 | set2)
print("Intersection of sets:", set1 & set2)
print("Difference of sets:", set1 - set2)







# Task 4: File Handling

# Create a text file and write student details
students = [
    {"name": "Aman", "marks": 85, "grade": "A"},
    {"name": "Riya", "marks": 72, "grade": "B"},
    {"name": "Rahul", "marks": 90, "grade": "A"},
    {"name": "Simran", "marks": 65, "grade": "B"},
    {"name": "Vikram", "marks": 78, "grade": "B"}
]

with open("ai_students.txt", "w") as f:
    for s in students:
        f.write(f"{s['name']},{s['marks']},{s['grade']}\n")

# Read file and display students scoring above 75
print("\nStudents scoring above 75:")
with open("ai_students.txt", "r") as f:
    for line in f:
        name, marks, grade = line.strip().split(",")
        if int(marks) > 75:
            print(f"{name} - {marks} - {grade}")







# Task 5: Real-World Mini Project (AI Prompt Logger)

from datetime import datetime

prompt = input("\nEnter your AI prompt: ")

# Save the prompt text with timestamp
with open("prompt_history.txt", "a") as f:
    f.write(f"{datetime.now()} - {prompt}\n")

print("Prompt saved successfully!")
