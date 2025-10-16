task 9.a

# Initialize the list of grades
grades = [85, 90, 78, 92, 88]

# Display the grades list
print("Grades List:", grades)

# Prompt the user to enter the index of the grade they want to view
try:
    index = int(input("Enter the index of the grade you want to view: "))
    # Attempt to display the grade at the specified index
    print(f"The grade at index {index} is: {grades[index]}")
except IndexError:
    # Handle the case where the index is out of range
    print("Invalid index. Please enter a valid index.")
except ValueError:
    # Handle the case where the input is not an integer
    print("Invalid input. Please enter a numerical index.")

    
    task 9.b
    
    # Custom Exception
class NegativeNumberError(Exception):
    pass  

try:
    # Take user input
    num1 = int(input("Enter the numerator: "))
    num2 = int(input("Enter the denominator: "))

    # Check for negative numbers
    if num1 < 0 or num2 < 0:
        raise NegativeNumberError("Negative numbers are not allowed")

    # Perform division
    result = num1 / num2
    print(f"Result: {num1} / {num2} = {result}")

except ValueError:
    print("Error: Please enter valid numeric values.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except NegativeNumberError as e:
    print(f"Error: {e}")

finally:
    print("Calculation Attempt Finished")

Sample Output 1 (Valid Input):
Enter the numerator: 20
Enter the denominator: 5
Result: 20 / 5 = 4.0
Calculation Attempt Finished


task 9.c

import os

# 1. Define custom exception
class EmptyFileError(Exception):
    pass

filename = input("Enter the filename: ")

file = None
try:
    # 3. Try opening the file
    file = open(filename, "r")

    # 4. Check if file is empty
    if os.path.getsize(filename) == 0:
        raise EmptyFileError("The file is empty.")

    # 5. Read and process content
    content = file.read()
    words = content.split()
    print(f"The file has {len(words)} words.")

# 6. Handle exceptions
except FileNotFoundError:
    print("Error: The specified file was not found.")
except EmptyFileError as e:
    print(f"Error: {e}")

# 7. Finally block
finally:
    if file:
        file.close()
    print("File operation completed")
