# For loop
# A for loop is used to iterate over a sequence (like a list, tuple, string, etc.) or other iterable objects.
# The syntax of a for loop is:
# for variable in sequence:
#     # code to execute
# Example 1: Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Example 2: Iterating over a string
for letter in "hello":
    print(letter)
# Example 3: Using the range() function to iterate over a sequence of numbers
for i in range(5):
    print(i)
# Example 4: Iterating over a dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")
# Example 5: Nested for loops
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
# Example 6: Using the break statement to exit a loop
for i in range(10):
    if i == 5:
        break
    print(i)
# Example 7: Using the continue statement to skip an iteration
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
# Example 8: Using the else clause with a for loop
for i in range(5):
    print(i)
else:
    print("Loop completed successfully!")
# Example 9: Using a for loop with a list comprehension
squares = [x**2 for x in range(10)]
print(squares)
# Example 10: Using a for loop to iterate over a file
# with open('file.txt', 'r') as file:
#     for line in file:
#         print(line.strip())

# Examples
for i in range(1, 11):
    print(i)

for i in range(1, 11, 2):
    print(i)

for item in ["apple", "banana", "cherry"]:
    print(item)

for item in "Python":
    print(item)

print('----'*20)

# Exercise: Calculate the total price of items in a list using a for loop.

prices = [10, 20, 30, 40, 50]
print("Prices:",prices)
total = 0
for price in prices:
    total += price
print(f"Total price: {total}")
