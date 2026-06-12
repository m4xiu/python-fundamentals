# Function 
# A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function.
# A function can return data as a result.
# Creating a Function
# In Python a function is defined using the def keyword:
def my_function():
  print("Hello from a function")
# Calling a Function
# To call a function, use the function name followed by parenthesis:
my_function()
# Arguments
# Information can be passed to functions as arguments. Arguments are specified after the function name, inside the parentheses.
# You can add as many arguments as you want, just separate them with a comma.
def my_function(fname):
  print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")
# If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")
# Keyword Arguments
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
# The return Statement
# To let a function return a value, use the return statement:
def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

#Exercise
def greet_name():
  print('Hi there!')
  print('Welcome aboard!')

print('Start')
greet_name()
print('Finish')