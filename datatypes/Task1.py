# WAP to take input decimal numbers from the user and convert taht into binary, octal, hexadecimal number system
# and display back on terminal again.

# Convert the input string into an 'int' so we can do math
d=int(input("Enter decimal numbers:"))

# Using Binary func
x=bin(d)
print(f"Decimal {d} in Binary is {x}")

# Using Octal func
x=oct(d)
print(f"Decimal {d} in Octal is {x}")

# Using Hexadecimal func
x=hex(d)
print(f"Decimal {d} in Hexadecimal is {x}")