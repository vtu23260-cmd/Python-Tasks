task 4.a

#Add Elements: Add elements to the list.
list=[10,20]
a=30

list.append(a)
print(list)
#Remove Elements: Remove specific elements from the list.
list.pop(1)#by index value
print(list)
list.remove(10)#by itemname
print(list)
#Sort Elements: Sort the list in ascending and descending order.
l=[5,8,9,15,30,89]
print(sorted(l))
#Find Minimum and Maximum: Find the minimum and maximum elements in thelist.
print("The minimum value is:",min(l))
print("The maximum value is:",max(l))
#Calculate Sum and Average
print("The sum is:",sum(l))
print("The average is :",((sum(l)/len(l))))
list.insert(2,[1,2])
print(list)
list.reverse()
print(list)
print(list[0][1])

task 4.b

# Input list of integers
numbers = [1, 2, 3, 4, 5, 6]

# List comprehension to get squares of even numbers
even_squares = [x**2 for x in numbers if x % 2 == 0]

# List comprehension with formatted descriptions
descriptions = [f"Square of {x} is {x**2}" for x in numbers if x % 2 == 0]

# Display the results
print("Even Squares:", even_squares)
print("Descriptions:", descriptions)

task 4.c

#Create a Tuple: Define a tuple with elements of different data types(10, 'hello', 3.14, 'world')
tuple=(10, 'hello', 3.14, 'world')
print(tuple)
#Access Elements: Access individual elements and slices of the tuple.
for i in tuple:
    print(i)
print(tuple[1:3])
print(tuple[:-1])
#Concatenate Tuples: Combine two tuples to create a new tuple.
t2=(5,0.5)
t3=tuple+t2
print(t3)
# Tuple Unpacking
a, b, c, d = tuple
print(f"Unpacked Values: a={a}, b={b}, c={c}, d={d}")
#Membership Testing
print("Is 'hello' in tuple?", 'hello' in tuple)
#Tuple Length
print("Length of Tuple:", len(tuple))
# Using functions where applicable
numeric_tuple = (5, 10, 15)
print("Max:", max(numeric_tuple))
print("Min:", min(numeric_tuple))
print("Sum:", sum(numeric_tuple))
#Immutable Nature: Attempt to modify elements of the tuple and handle the resulting error.
tuple(3)="PI" #ERROR

task4.d

#Create a Dictionary: Define a dictionary with key-value pairs of different data types.({'name': 'Alice', 'age': 30, 'city': 'New York'}
dictionary={'name': 'Alice', 'age': 30, 'city': 'New York'}
print(dictionary)
#Access Values: Access values using keys.
print(dictionary['name'])
print(dictionary['age'])

#Modify Dictionary: Update values, add new key-value pairs, and remove existing pairs.
dictionary['name']= "James"
print(dictionary)
dictionary.pop('city')
print(dictionary)
#Iterate Over Dictionary: Use loops to iterate over keys or values.
for k in dictionary:
    print("KEY:",k)

print(dictionary.items())
