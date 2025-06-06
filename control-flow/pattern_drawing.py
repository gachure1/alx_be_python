# Ask the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer while loop for rows
while row < size:
    # Inner for loop for columns (printing asterisks in one line)
    for col in range(size):
        print("*", end="")
    # Move to the next line after a row is printed
    print()
    # Increment row counter
    row += 1
