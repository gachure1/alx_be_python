# Ask the user to enter a number
number = int(input("Enter a number to see its multiplication table: "))

# Loop from 1 to 10 and print the multiplication result
for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")

