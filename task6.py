task 6.a

def copy_files(file_paths):
    for file_path in file_paths:
        if os.path.exists(file_path):
            with open(file_path, 'r') as original_file:
                original_content = original_file.read()
                copy_file_path = file_path.split('.')[0] + '_copy.' + file_path.split('.')[1]
                with open(copy_file_path, 'w') as copy_file:
                    copy_file.write(original_content)
                print(f"Contents copied from {file_path} to {copy_file_path} successfully.")
        else:
            print(f"Error: File '{file_path}' not found.")

# Example usage:
import os
file_list = ['file1.txt', 'file2.txt', 'file3.txt']  # List of file paths
copy_files(file_list)


task 6.b


def write_employee_report(filename):
    employees = [
        {"name": "Alice", "department": "HR"},
        {"name": "Bob", "department": "Engineering"},
        {"name": "Charlie", "department": "Finance"}
    ]
    
    with open(filename, "w") as file:
        for employee in employees:
            line = f"Name: {employee['name']}, Department: {employee['department']}\n"
            file.write(line)
# Example usage:
write_employee_report("employee_report.txt")


task 6.c


def teacher_notes_word_count():
    # Step 1: Create a file and write student notes
    file_name = input("Enter the file name: ")
    with open(file_name, 'w') as file:
        print("Enter student notes (press Enter on an empty line to stop):")
        while True:
            line = input()
            if not line:
                break
            file.write(line + '\n')

    # Step 2: Display the content of the file
    print("\nFile Content:")
    with open(file_name, 'r') as file:
        content = file.read()
        print(content)

    # Step 3: Count occurrences of a chosen word
    word = input("Enter the word to count: ")
    count = content.split().count(word)
    print(f"\nThe word '{word}' occurs {count} times.")

# Run the program
teacher_notes_word_count()



task 6.d


import csv

# Read CSV file
file_name = input("Enter CSV file name: ")
records = []

with open(file_name, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        records.append(row)

# Display all records
print("\nStudent Records:")
for r in records:
    print(f"Id: {r[0]}, Name: {r[1]}, Grade: {r[2]}, Attendance: {r[3]}")

# Calculate average attendance
total = sum(int(r[3]) for r in records)
average = total / len(records)
print(f"\nAverage Attendance: {average:.2f}")
