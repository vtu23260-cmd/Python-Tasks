task 1.a

a = int(input())
print("Loaves Discount")
r=185*a
d=0.6*r
a=0.4*r
print("Regular Price ", r)
print("Total Discount ", d)
print("Total Amount to be paid ", a)


task 1.b

cls = float(input(‘Enter temperature in Celsius: ‘))  
fah = (cls * 1.8) + 32  
print(‘%0.1f Celsius is equal to %0.1f degrees Fahrenheit’%(cls,fah)) 

task 1.c


import math
 # Function to find distance
def distance(x1, y1, z1, x2, y2, z2):
     d = math.sqrt(math.pow(x2 - x1, 2) +
                math.pow(y2 - y1, 2) +
                math.pow(z2 - z1, 2)* 1.0)
    print("Distance is ")
    print(d)
 # Driver Code	
x1 = float(input("Enter the X1-coordinate: "))
y1 = float(input("Enter the Y1-coordinate: "))
z1 = float(input("Enter the Z1-coordinate: "))
x2 = float(input("Enter the X2-coordinate: "))
y2 = float(input("Enter the Y2-coordinate: "))
z2 = float(input("Enter the Z2-coordinate: "))
# function call for distance
distance(x1, y1, z1, x2, y2, z2)   


task 1.d

import math 
def equationroots( x, y, z): 
    discri = y * y - 4 * x * z 
    sqrtval = math.sqrt(abs(discri))   

    # checking condition for discriminant
    if discri > 0: 
        print(" real and different roots ") 
        print((-y + sqrtval)/(2 * x)) 
        print((-y - sqrtval)/(2 * x))   

    elif discri == 0: 
        print(" real and same roots") 
        print(-y / (2 * x))   

    # when discriminant is less than 0
    else:
        print("Complex Roots") 
        print(- y / (2 * x), " + i", sqrtval) 
        print(- y / (2 * x), " - i", sqrtval) 

# Driver Program 
x = int(input())
y = int(input())
z = int(input())
if x == 0: 
        print("Input correct quadratic equation")
else:
    equationroots(x, y, z)
 to join this conversation on GitHub.
