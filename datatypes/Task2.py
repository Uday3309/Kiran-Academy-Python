# WAP to accept a value and its corresponding base system (Binary, Octal, or Hexadecimal) from the user. 
# Convert the input into a Decimal integer and display the result back to the terminal.

# Accept a Binary number and the base system number from the user for the conversion.
binnumber=input("Enter a Binary number, (ex:0b0001): ")
binbase=input("Enter the base number for the binary number, (ex:2, 8, 16): ")

# Accept a Octal number and the base system number from the user for the conversion.
octalnumber=input("Enter a Octal number, ex: 0o1234: ")
octalbase=input("Enter the base number for the octal number, (ex: 8): ")

# Accept a HexaDecimal number and the base system number from the user for the conversion.
hexanumber=input("Enter a Hexadecimal number, ex: 0xFace : ")
hexabase=input("Enter the base number for hexa number, (ex: 16): ")

# converting Binary number to decimal number
binresult=int(binnumber,int(binbase))

# converting Octal number to decimal number
octalresult=int(octalnumber, int(octalbase))

# converting HexaDecimal number to decimal number
hexaresult=int(hexanumber, int(hexabase))

print(f"The number {binnumber} in base {binbase} is {binresult} in decimal.")
print(f"The number {octalnumber} in base {octalbase} is {octalresult} in decimal.")
print(f"The number {hexanumber} in base {hexabase} is {hexaresult} in decimal.")