task 3.a

# Function to find k'th non repeating character 
# in string 
from collections import OrderedDict   
def kthRepeating(input,k): 
    # OrderedDict returns a dictionary data structure having characters of input 
    # string as keys in the same order they were inserted and 0 as their default value 
    dict=OrderedDict.fromkeys(input,0) 
      # now traverse input string to calculate  frequency of each character 
    for ch in input: 
        dict[ch]+=1
      # now extract list of all keys whose value is 1 from dict Ordered Dictionary 
    nonRepeatDict = [key for (key,value) in dict.items() if value==1] 
      # now return (k-1)th character from above list 
    if len(nonRepeatDict) < k: 
        return 'Less than k non-repeating characters in input.' 
    else: 
        return nonRepeatDict[k-1] 
# Driver function 
if __name__ == "__main__": 
    inp = str(input())
    k = int(input())
    print (kthRepeating(inp, k))

    
    task 3.b
    
    import math
def cosine(x,n):
    cosx = 1
    sign = -1
    for i in range(2, n, 2):
        pi=22/7
        y=x*(pi/180)
        cosx = cosx + (sign*(y**i))/math.factorial(i)
        sign = -sign
    return cosx
x=int(input())
n=int(input())
print(round(cosine(x,n),2))

task 3.c

dataloader.py
import pandas as pd
def load_data():
    df = pd.read_csv("students.csv")
    return df

statshelper.py
import numpy as np
from scipy import stats
def subject_mean(df, subject):
    return np.mean(df[subject])
def subject_std(df, subject):
    return np.std(df[subject])
def subject_mode(df, subject):
    return stats.mode(df[subject], keepdims=True).mode[0]

main.py
# Step 1: Imports
from dataloader import load_data
from statshelper import subject_mean, subject_std, subject_mode
import pandas as pd
# Step 2: Load CSV data
df = load_data()
# Step 3: Subjects to analyze
subjects = ["Math", "Science", "English"]
# Step 4: Collect results
results = []
for subj in subjects:
    mean_val = subject_mean(df, subj)
    std_val = subject_std(df, subj)
    mode_val = subject_mode(df, subj)
    results.append([subj, mean_val, std_val, mode_val])
# Step 5: Create results table
results_df = pd.DataFrame(results, columns=["Subject", "Mean", "Standard Deviation", "Mode"])
print(results_df)

task 3.d

import pandas as pd
import numpy as np
# Create sample sales data
data = pd.DataFrame({
    'Product': ['Laptop', 'Headphones', 'Mouse', 'Keyboard'] * 5,
    'Units_Sold': np.random.randint(5, 50, 20),
    'Price_per_Unit': np.random.randint(1000, 5000, 20)
})
# Calculate total sales for each row
data['Total_Sales'] = data['Units_Sold'] * data['Price_per_Unit']
# Find top-selling product
top_product = data.groupby('Product')['Total_Sales'].sum().idxmax()
# Calculate total sales
total_sales = data['Total_Sales'].sum()
# Show results
print("Top Selling Product:", top_product)
print("Total Sales: ₹", total_sales)
print("\nSample Data:\n", data)

task 3.e

my_toolkit/
    __init__.py
    geometry_utils.py
    text_utils.py
main.py


my_toolkit/geometry_utils.py
import math

def area_circle(radius):
    return math.pi * radius ** 2

def perimeter_rectangle(length, width):
    return 2 * (length + width)

def pythagoras(a, b):
    return math.sqrt(a**2 + b**2)

my_toolkit/text_utils.py
def to_uppercase(s):
    return s.upper()

def word_count(s):
    return len(s.split())

def is_palindrome(s):
    s_clean = ''.join(s.lower().split())
    return s_clean == s_clean[::-1]

my_toolkit/__init__.py
from .geometry_utils import area_circle, perimeter_rectangle, pythagoras
from .text_utils import to_uppercase, word_count, is_palindrome

main.py
from my_toolkit import area_circle, perimeter_rectangle, pythagoras
from my_toolkit import to_uppercase, word_count, is_palindrome

# Geometry functions
print("Area of circle (r=5):", round(area_circle(5), 2))
print("Perimeter of rectangle (4x6):", perimeter_rectangle(4, 6))
print("Hypotenuse (3,4):", round(pythagoras(3, 4), 2))

# Text functions
print("Uppercase:", to_uppercase("hello world"))
print("Word count:", word_count("Python is fun"))
print("Is palindrome (level):", is_palindrome("level"))
