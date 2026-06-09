# Bitwise operators: &, |, ^, ~, <<, >>
a = 5  # 0b0101
b = 3  # 0b0011
print("Bitwise AND (a & b):", a & b)  # 0b0001 -> 1
print("Bitwise OR (a | b):", a | b)   # 0b0111 -> 7
print("Bitwise XOR (a ^ b):", a ^ b)  # 0b0110 -> 6
print("Bitwise NOT (~a):", ~a)     # 0b1010 -> -6 (in two's complement)
print("Left Shift (a << 1):", a << 1)  # 0b1010 -> 10
print("Right Shift (a >> 1):", a >> 1) # 0b0010 -> 2