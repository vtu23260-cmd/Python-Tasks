task 10.a
import matplotlib.pyplot as plt

languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.bar(languages, popularity, color='b')
plt.title('Popularity of Programming Languages')
plt.xlabel('Programming Languages')
plt.ylabel('Popularity')
plt.show()

task 10.b

import matplotlib.pyplot as plt

# Step 1
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Step 2
plt.pie(popularity, labels=languages, autopct='%1.1f%%')

# Step 3
plt.title('Popularity of Programming Languages')
plt.legend(languages, loc="best")

# Step 4
plt.show()


task 10.c

Import libraries:
pandas for reading CSV data.
matplotlib.pyplot for plotting.
Read CSV file using pd.read_csv("students.csv").
Extract student names from the "Name" column for the x-axis.
Plot each test’s marks as a separate line on the graph:
Use marker='s' for Test1, marker='o' for Test2, etc.
Use label parameter to name each line.
Add labels, title, and legend:
plt.ylabel("Marks")
plt.title("Student Marks Across Tests")
plt.legend()
Display the plot using plt.show().
