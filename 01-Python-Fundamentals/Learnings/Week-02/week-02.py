# # Boolean & Comparison Operators

# # 1. Take two numbers and check whether they are equal.

num1 = int(input("First Number:"))
num2 = int(input("Second Number:"))
num3 = num1 == num2 
print(num3)

# # 2. Check whether two numbers are different.

num_1 = int(input("First Number"))
num_2 = int(input("Second Number"))
num3 = num_1 != num_2
print(num3)

# # 3.  Check whether the first number is greater than the second.

nam_ = int(input("First Number:"))
nam_1 = int(input("Second Number:"))
print(nam_ > nam_1)

# # 4. Check whether the first number is greater than or equal to the second

num0 = int(input("First Number:"))
num1 = int(input("Second Number:"))
print(num0 >= num1)

# # 5. Print the result of 15 < 8

num1  = 15
num2 = 8
print(15 < 8)

# # 6. Take your age and check if it is greater than 18.v

age_ = int(input("Enter Age:"))
criteria_ = age_ > 18
print("I'm adult:", criteria_)

# # 7. Take your marks and check if they are greater than 40.

marks_ = int(input("Enter Marks"))
criteria_ = marks_ > 40
print(criteria_)

# # 8. Take your height and check if it is greater than 6 feet.

height_ = int(input("Enter Height:"))
criteria_ = height_ > 6
print(criteria_)

# # 9. Take two floating-point numbers and compare them.

num1 = float(input("Enter First Float number:"))
num2 = float(input("Enter Second Float Number:"))
print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)

# # 10. Compare two cities.
city1 = input("First City:")
city2 = input("Second City:")

print(city1 > city2)
print(city1 < city2)
print(city1 == city2)
print(city1 != city2)
print(city1 > city2)
print(city1 < city2)

# # 11. Compare the length of two names using len()

first = "Rudra"
second = "Aanchal"
print(len(first) == len(second))
print(len(first) != len(second))
print(len(first) > len(second))
print(len(first) < len(second))
print(len(first) <= len( second))
print(len(first) >= len(second))

# # 12. Compare two mobile numbers (as strings)
a = "4567890"
b = "2346534"
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)
print(a < b)
print(a > b )

# # if Statement

# # 13. Check if a number is positive.

a = int(input("Enter Number:"))

if a > 0:
    print("Positive number")

# 14. Check if salary is greater than 50000

salarly_ = int(input("Enter Salarly:"))    

if salarly_ > 50000:
    print("Salarly")

# # 15. check if attendance is greater than 75%

days_ = int(input("ENTER DAYS:"))
total_ = int(input(" ENTER TOTAL Class:"))
cal_per = days_/total_*100

if cal_per > 75:
    print("passed!Attendance is  %, which is greater than 75%")


# # 16. Check if a string length is greater than 5

stri_ = input("Enter Name")
leng_ = len(stri_)

if leng_ > 5:
    print("This string length greater than 5:")


# # 16. Check if a password length is greater than 8.

pass_ = input("Enter Password:")
length_pass = len(pass_)

if length_pass > 8:
    print("Password length is greater than 8")

# 17. Scholarship eligibility

scholar_qualification = int(input("Enter Father Income:"))

if scholar_qualification < 500000:
    print("Congralulation! U are eligible for Scholarship") 


# # 18. Sports trial eligibility

attended_ = int(input("Entrer days"))
all_overdays = int(input("Total Session"))
total_attend = attended_/all_overdays*100

if  total_attend > 75:
    print("Congratulation! You are Eligible For Scholarship")


# if-else


# # 19. Even or Odd.

value = int(input("Enter a Number:"))
if value % 2 == 0:
    print("This is a Even Number") 
else:
    print("This is a Odd Number")

# 20. . Positive or Negative.
 
number_ = int(input("Enter Number:"))

if number_ > 0:
    print("This is a +ve number")
else:
    print("this is a -ve number")

# 21. Adult or Minor

age_ = int(input("Enter Age")) 

if age_ > 18:
    print("Adult")
else:
    print("Minor")

# 22. Greater of two numbers.

num1 = int(input("Enter First Number:"))    
num2 = int(input("Enter Second Number:"))

if num1 > num2:
    print("num1 is greater:")
else:
    print("num2 is greater:")

# 23. Check if string length is greater than 10

string_len = (input(" Enter word:"))
length_ = len(string_len)

if length_ > 10:
    print("String length greater than 10 ")
else:
    print("String length is not greater than 10")

# 24. Driver's license eligibility

age_ = int(input("enter age:-")) 
name = input("Enter Name:-")   

if age_ >= 18:
    print(f"Congratulation!{name} You are eligible for Driving License")
else:
    print(f"{name}You are not eligible for Driving License")

# 25.   Scholarship eligibility  

  

scholarship_ = int(input("Enter your Father Income"))  

if scholarship_ < 500000:
    print("You are eligible for Scholarship")  
else: 
    print("You are not eligible for Scholarship")

# 26.Accept The Gender from the user as char and print the respective Greeting messge

gender_ = input("Please tell your gender (M or F):-" )

if gender_ == "M":
    print("Hello! Good Morning Sir")
else:
    print("Hello! Good Morning Mam")

# 27. If- elif ladder
#You cna also create if elif ladder using multiple conditions


#. For understanding solve this question
#. take the input of temperature in celsius.
#. Below 0℃ - "Freezing Cold
#. 0°C to 10°℃ - "Very Cold
#. 10°℃ to 20°℃ - "Cold
#. 20°C to 30℃ - "Pleasant
#. 30°℃ to 40°℃ - "Hot
#. Above 40C - "Very Hot

t = int(input("Enter temperature:"))

if t < 0:
    print(" Freezing Cold")

elif t >= 0 and t <= 10:
    print("Very cold")

elif t >= 10 and t <= 20:
    print("Cold")

elif t >= 20 and  t <= 30:
    print("Pleasant")

elif t >= 30 and t <= 40:
    print("Hot") 

elif t >= 40 and t <= 50:
    print("Very Hot")

# if-elif-else

# 28. Grade Calculator (A, B, C, D,E, F)

marks_ = int(input("Enter Marks:"))

if marks_ >= 80 and marks_ <= 100:
    print("A")

elif marks_ >= 60 and marks_ <= 80:
    print("B")   

elif marks_ >= 40 and marks_ <= 60:
    print("C")

elif marks_ >= 20 and marks_ <= 40:
    print("D")
else:
    print("E")

# 29.  Age Category (Child, Teen, Adult, Senior)

age_ = int(input("Enter your age:"))

if age_ >= 0 and age_ <= 13:
    print("child")

elif age_ >= 13 and age_ <= 18:
    print("Teen")

elif age_ >= 18 and age_ <= 50:
    print("Adult")

else:
    print("Senior Citizen")


# # 30. Mobile Recharge Plan

charges_ = int(input("Enter rupees:"))

if charges_ <= 100:
    print("only calling")

elif charges_ >= 300 and charges_ <= 100:
    print("1.5GB Data and Unlimited calls")

else:
    print("2GB+ Unlimited Dtata/per day and Unlimited Calls")

# 31.  Divisibility Rules (3 and 5)
#Write a program that checks a number:

#If divisible by both 3 and 5, print "FizzBuzz"
#If divisible only by 3, print "Fizz"
#If divisible only by 5, print "Buzz"
#Otherwise, print "Not divisible by 3 or 5" 

num1 = int(input("Enter a number:"))

if num1% 3 == 0 and num1% 5 == 0:
    print("Fizzbuzz")

elif num1%3 == 0:
    print("Fizz")

elif num1%5 == 0:
    print("buzz")

else:
    print("Not divisibly by 3 or 5")

# 32 Triangle Type Checker

#   three side lengths of a triangle a, b, and c:
#If all three sides are equal: "Equilateral"
#if two sides are equal : isoceles
#if all side are unequal: scalene

side1= int(input("Enter First Side:"))
side2 = int(input("Enter Second Side:"))
side3 = int(input("Enter Third Side:"))

if side1 == side2 and side2 == side3:
    print("Equilateral Triangle")

elif side1 == side2 or side2 == side3:
    print("Isoceles Triangle")

else:
    print("Scalene Triangle")

# 33. Valid Login System

# username (admin) and password(billu1) acces granted krna h

usern_ = input("Enter Username:")
passw_ = input("Enter Password:")

if usern_ == "admin" and passw_ == "billu1":
    print("Access granted")

else:
    ("Access denied")


# Nested if


# 34. Blood Donation Eligibility

age = int(input("Enter Age:"))

if age >= 18:
    weight = int(input("Enter Weight:"))
    if weight >= 50:
        print("U are Eligible for Blood Donation")
    else:
        print("U are Not eligible For Blood Donation")
else:
    print("Not eligible: Age must be at least 18 years")

 # 35. Nested Voting System (Check: Citizen of India? 

citizen_ = input("Enter Country:")

if (citizen_== "India") or (citizen_ == "INDIA") or (citizen_ == "india"):

    age_ = int(input("Enter age:"))
    if age_ >= 18:
        print("U are eligible for Voting ")
    else:
        print("U are Not eligible for voting")

else:
    print("Sorry! U are not a Citizen of India")


        
               

              




    

















    











 








