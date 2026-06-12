# Nested loops
# A nested loop is a loop that is contained within another loop. The inner loop will be executed once for each iteration of the outer loop.
# Example of a nested loop
for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

# Exercise
numbers = [5,2,5,2,2]
for x_count in numbers:
    print('x' * x_count)

numbers = [5,2,5,2,2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

