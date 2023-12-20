'''
Write a python code to print an American flag on the screen.
Expected Output:

* * * * * * * ====================================
 * * * * * * *====================================
* * * * * * * ====================================
 * * * * * * *====================================
* * * * * * * ====================================
 * * * * * * *====================================
==================================================
==================================================
==================================================
==================================================
'''
"""
# The following lines print the pattern of stars and equal signs to represent the American flag
print("* * * * * * * ====================================")
print(" * * * * * * *====================================")
print("* * * * * * * ====================================")
print(" * * * * * * *====================================")
print("* * * * * * * ====================================")
print(" * * * * * * *====================================")
print("==================================================")
print("==================================================")
print("==================================================")
print("==================================================")
"""

def printUSAFlag(height, width):
    s = ""

    # Iterate over each row and column to construct the flag pattern
    for i in range(height):
        for j in range(width):
            if i < 9*height/15 and j < 12*width/46:
                # Check the position to determine whether to print '*' or ' '
                if (i+j)%2 == 0 and j != 12*width/46 - 1:
                    s += '*'  # Add '*' to the pattern
                else:
                    s += " "  # Add empty space to the pattern
            else:
                s += '='  # Add '=' to the pattern for the remaining area

            if j == width - 1:
                s += '\n'  # Add a newline character at the end of each row
            else:
                s += ''  # Add an empty character for formatting purposes

    print(s)  # Print the final pattern

'''
width = int(input("Width: "))
height = int(input("Height: "))
'''

# Call the function to print the American flag with given dimensions
printUSAFlag(10, 50)