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










     

