task 7.a

    # 1. Print a welcome message
    print("Welcome to the Student Grades Analyzer!\n")
    
    # 2. Determine and print the number of students
    num_students = len(student_names)
    print("Number of students:", num_students)
    
    # 3. Print the type of the student names list and the grades list
    print("\nType of student_names list:", type(student_names))
    print("Type of student_grades list:", type(student_grades))
    
    # 4. Find and print the highest and lowest grade
    highest_grade = max(student_grades)
    lowest_grade = min(student_grades)
    print("\nHighest grade:", highest_grade)
    print("Lowest grade:", lowest_grade)
    
    # 5. Print the list of grades sorted in ascending order
    sorted_grades = sorted(student_grades)
    print("\nSorted grades:", sorted_grades)
 
    # 6. Print the list of grades in reverse order
    reversed_grades = list(reversed(sorted_grades))
    print("Reversed grades:", reversed_grades)
    
    # 7. Generate and print a range of grade indices from 1 to the number of students
    grade_indices = list(range(1, num_students + 1))
    print("\nGrade indices from 1 to number of students:", grade_indices)

# Run the analysis
analyze_student_grades()


task 7.b

def add(a, b):
        return a + b
def subtract(a, b):
    return a - b
multiply = lambda a, b: a * b
divide = lambda a, b: a / b if b != 0 else "Error: Division by zero"

# Regular function for greeting
greet = lambda name: f"Hello, {name}! Welcome to the program."

def main():
    # Demonstrating the use of lambda functions
    num1 = int(input("enter num1:"))
    num2 = int(input("enter num2:"))
    
    print("Arithmetic Operations:")
    print("Sum of", num1, "and", num2, ":", add(num1, num2))
    diff=subtract(num1, num2)
    print("Difference between", num1, "and", num2, ":", diff)
    if diff< 0:
        print("The difference is negative!")
    elif diff==0:
        print("The difference is Zero!")
    else:
        print("The difference is Positive!")

    print("Product of", num1, "and", num2, ":", multiply(num1, num2))
    print("Quotient of", num1, "and", num2, ":", divide(num1, num2))    
    # Greeting the user
    user_name = "Alice"
    print("\nGreeting:")
    print(greet(user_name))

# Run the main function
if __name__ == "__main__":
    main()

task 7.c


# Recursive function to reverse a string
def reverse_string(s):
    if len(s) == 0:   # base case
        return s
    return reverse_string(s[1:]) + s[0]

# Test cases
print("Reverse of 'hello' =", reverse_string("hello"))
print("Reverse of 'python' =", reverse_string("python"))
print("Reverse of 'recursion' =", reverse_string("recursion"))



task 7.d


from functools import reduce

# Sample data
student_names = ["Alice", "Bob", "Charlie", "Diana"]
student_grades = [65, 72, 58, 70]

print("Original Grades:")
print(list(zip(student_names, student_grades)))

# 1. Scale grades using map and lambda (e.g., add 20 internal points to each grade)
scaled_grades = list(map(lambda x: x + 20, student_grades))
print("\nScaled Grades (+20 points):")
print(list(zip(student_names, scaled_grades)))

# 2. Filter students with grades above 90 using filter and lambda
high_achievers = list(filter(lambda x: x > 90, scaled_grades))
print("\nStudents with grades above 90:", high_achievers)

# 3. Calculate total and average using reduce
total = reduce(lambda a, b: a + b, scaled_grades)
average = total / len(scaled_grades)
print("\nTotal of scaled grades:", total)
print("Average of scaled grades:", average)

# 4. Sort grades in ascending order using sorted and lambda
sorted_grades = sorted(scaled_grades)
print("\nSorted Grades (Ascending):", sorted_grades)


# 5. Sort grades in descending order using sorted and lambda
sorted_desc = sorted(scaled_grades, reverse=True)
print("\nSorted Grades (Descending):”, sorted_desc )
