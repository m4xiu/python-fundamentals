# Identity Operators: is, is not
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("Is a identical to b?", a is b)      # False
print("Is a identical to c?", a is c)      # True
print("Is a not identical to b?", a is not b)  # True
print("Is a not identical to c?", a is not c)  # False

# Explanation:
# The 'is' operator checks if two variables point to the same object in memory.
# In this example, 'a' and 'b' are two different lists with the same content, so 'a is b' returns False.
# However, 'c' is assigned to   'a', so 'a is c' returns True because they point to the same object in memory.