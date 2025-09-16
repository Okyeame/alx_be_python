# pattern_drawing.py

# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter for while loop
row = 0

# Outer loop (while) to handle rows
while row < size:
    # Inner loop (for) to handle columns
    for col in range(size):
        print("*", end="")  # Print * without moving to a new line
    print()  # Move to the next line after finishing one row
    row += 1
