# What is a while loop?
# A while loop is a control flow statement that allows code to be executed repeatedly
# as long as a certain condition is true. The syntax of a while loop is:
# while condition:
#     # code to execute
# Example 1: Using a while loop to print numbers from 1 to 10
i = 1
while i <= 10:
    print(i)
    i += 1
# Example 2: Using a while loop to print even numbers from 1 to 10
i = 1
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1
# Example 3: Using a while loop to iterate over a list
fruits = ["apple", "banana", "cherry"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
# Example 4: Using a while loop to iterate over a string
text = "hello"
i = 0
while i < len(text):
    print(text[i])
    i += 1
# Example 5: Using a while loop with a break statement
i = 1
while True:
    print(i)
    if i == 5:
        break
    i += 1
# Example 6: Using a while loop with a continue statement
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
# Example 7: Using a while loop with an else clause
i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("Loop completed successfully!")
# Example 8: Using a while loop to create a simple menu
while True:
    print("Menu:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("You selected Option 1")
    elif choice == "2":
        print("You selected Option 2")
    elif choice == "3":
        print("Exiting the menu.")
        break
    else:
        print("Invalid choice. Please try again.")

# Exercise

i = 1 
while i <= 5:
    print(i)
    i += 1
print('Done!')
print('----'*20)

i =1
while i <= 10:
    print('*'*i)
    i += 1

