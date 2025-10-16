task 2.a

score =int(input("Enter the score:"))
if score>=90:
    print("The Grade is A")
elif (score <=89 and score>=80):
    print("The Grade is B")
elif(score <=79 and score >=70):
    print("The Grade is C")
elif( score <=69 and score >=60):
    print("The Grade is D")
else:
    print("The Grade is F")

    task 2.b
    
    # Displaying the first 10 natural numbers
print("The first 10 natural numbers are:")
for i in range(1, 11):  # Loop from 1 to 10
    print(i)

    
    task 2.c
    
    
    Program:
x=input()
c=0
for i in x:
    if (ord(i)>64 and ord(i)<91):
        c+=1
print(c+1)


task 2.d



a=int(input())
p=0
b=a
while(b>0):
    r=b % 10
    p=p*10+r
    b=b//10
if (p==a):
    print ("Mirror")
else:
    print("No Mirror")
