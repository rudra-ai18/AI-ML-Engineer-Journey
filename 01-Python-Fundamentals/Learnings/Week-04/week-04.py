# Function

# 1.
def hello():
    print("This is a hello function so I am doing")


# hello()

# 2.Positional Arguments

def sum(a,b):
    print(f"The sum of your numbers is {a +b}")


sum(12,45)
sum(45,45)


# 3. Default Arguments

def hello(name,age):
    print(f"Your name is {name} and your age is {age}")

hello("Rudra Pratap Singh Chauhan",21)

# 4. Keyword Argument

def intro(name,age):
    print(f"my name is {name} and your age is {age}")


intro(age =21,name ="Rudra Pratap Singh Chauhan")


# 5. Default Arguments

def sum(a,b=45): # b=45 is default parameter
    print(f"The sum of two number is {a+b}")

sum(20)
sum(20,43) # 43 changes value in parameter so this ic called argument default

# 6. return

def hello():
    return "Hello! how are you"

print(hello())

# 7. Create a function greet() that prints "Hello Python".

def greeting():
    print("Hello Python ")

greeting()

# 8. Create a function that prints your name, course and college.

def Studnformation(name,course,college):
    print(f"My name is: {name}")
    print(f"Course    : {course}")
    print(f"College:{college}")

StudentInformation(name = "Rudra Pratap Singh Chauhan",course = "BS in AI and DS",college = "IIT Jodhpur")

# 9. Create a function that prints numbers from 1 to 10.

def count():
    for i in range(1, 11):
        print(i)


# count()

# 10. Create a function that prints even numbers from 1 to 20.

def even():
    for i in range(1,21):
        if i%2 == 0:
            print(i)

even()
    
# 11. Create a function that prints the multiplication table of 5

def table():
    n = int(input("Enter a number which number table you want:-"))
    for i in range(n,n*10+1,n):
        print(i)

# table()

# 12. Create a function that prints "Welcome to AI Engineering".

def greetings(name):
    print(f"welcome to AI Engineering {name}")

greetings("Rudra Pratap Singh Chauhan")


# 13. Create a function that prints a formatted student profile.

def StudentProfile(name,age,course,college,year):
    print(f"Name {name}")
    print(f"Age {age}")
    print(f"Course {course}")
    print(f"College {college}")
    print(f"Year {year}")




StudentProfile(name = "Rudra Pratap Singh Chauhan",age = 21,course = "BS in AI and DS",college = "IIT Jodhpur",year = "2nd")

# 14. Function to calculate the sum of 1 to 100

def sum():
    sum = 0
    for i in range(1,101):
        sum = sum + i
        print(sum)

sum()    

# 15. Function to print squares from 1 to 20.

def square():
    for i in range(1,21):
        print(f"The square of {i} is {i **2}")


square()

# 16. Function to print cubes from 1 to 10.

def cube():
    for i in range(1,11):
        print(f"The cube of {i} is {i**3}")

cube()        


# 17. Function to print numbers in reverse.

def reverse():
    for i in range(100,0,-1):
        print(f"reverse order  {i}")

reverse()

# 18. Function to print all numbers divisible by 3

def divisible():
    for i in range(1,100):
        if i%3 == 0:
            print(f"divisible by 3 is {i}")

divisible()

# Parameters & Arguments


# 19. Function that takes a name and prints a greeting.

def greeting(name):
    print(f"Hello! {name}, Welcome back")

greeting("RUDRA PRATAP SINGH CHAUHAN")    

# 20. Function that takes age and prints age category.

def ageCategory(age):
    print(f"Hello! my age is {age}")

ageCategory(21)    

# 21. Function that takes two numbers and prints their sum.

def Arithematic(a,b):
    print(f"Sum of a and b is {a+b}")
    print(f"Subtraction of a and b is {a - b}")
    print(f"multiply of a and b is {a*b}")
    
 

Arithematic(a = 12,b=25)    

# 22 Function that takes a number and prints its table.

def table(a):
    print(f)
    for i in range(a,a*10+1,a):
        print(f"{i}")

table(2)

# 23.Create a function that prints "Welcome to AI Engineering".

def greet():
    print("Welcome to AI Engineering")


greet()


# 24. Create a function that prints a formatted student profile. 

def studentprofile():
    nam = input("Student Name:")
    course = input("Course:")
    Year = int(input("Enter year"))
    print()
    print("="*40)
    print(f"Student")
    print("="*40)
    print()
    print(f"Student Name:{nam}")
    print(f"Course Name :{course}")
    print(f"Year        : {Year}")




studentprofile()



# 25. Function that takes a number and checks whether it is even or odd.

def checker(a):
    if a % 2 == 0:
        print(f"It's a Even Number {a}")
    else:
        print(f"It's a Odd Number {a}")


checker(5)


# 26. Function that takes marks and prints grade

def marks(math,science,english):
    total = math + science+ english
    print(f"Total Marks {total}")
    if total >= 300:
        print("A+")
    elif total >= 250:
        print("A")
    elif total >= 200:
        print("B+")
    elif total >= 150:
        print("B")
    elif total >= 100:
        print("C+")
    else:
        print("C, Means u are fail")


marks(math = 10,science = 100,english = 60)


# 27. Function that takes age and determines voting eligibility.

def votingeligiblity(age):
    print("Voting Eligiblity")
    if age >= 18:
        print("You are Eligible for Voting")
    else:
        print("You are Not Eligible for Voting")

votingeligiblity(20)


# 28. Function that takes percentage and returns grade category.

def sum(a,b):
    return a + b


print(sum(30,90))

# 29. Function returning square.

def square(a):
    return a**2

print(square(7))

# 30. Function returning even/odd status.

def check(a):
    if a % 2 == 0:
        return "It's a Even Number"
    else:
        return "it's a Odd Number"

print(check(9))    


# 31. Function returning largest of two numbers.

def secondlargest(a:float,b:float):
    return a if a > b  else b


print(secondlargest(255,500))


# 32. Function returning student's grade.

def studentgrade(name,college,course):
    return name,college,course  

print(studentgrade(name ="Rudra",college = "IIT Jodhpur",course ="BS"))


# Functions + Conditions + Loops

# 33. Function that prints even numbers up to n.

def check(a):
    for i in range(2,a+1,2):
        print(i)


check(30)

# 34. Function that prints numbers in reverse.

def reverse(a):
    for i in range(a,0,-1):
        print(i)

reverse(100)

# 35. Function that calculates sum up to n.

def sum(a):
    sum = 0
    for i in range(0,a+1):
         sum = sum + i 
         print(sum)

    

sum(80)


















        










     

