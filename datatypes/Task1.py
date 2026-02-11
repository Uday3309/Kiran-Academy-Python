# WAP to take input decimal numbers from the user and convert taht into binary, octal, hexadecimal number system
# and display back on terminal again.

# Convert the input string into an 'int' so we can do math
decimalnumb=int(input("Enter decimal numbers:"))

# Using Binary func
binarynumb=bin(decimalnumb)
print(f"Decimal {decimalnumb} in Binary is {binarynumb}")

# Using Octal func
octalnumb=oct(decimalnumb)
print(f"Decimal {decimalnumb} in Octal is {octalnumb}")

# Using Hexadecimal func
hexanumb=hex(decimalnumb)
print(f"Decimal {decimalnumb} in Hexadecimal is {hexanumb}")