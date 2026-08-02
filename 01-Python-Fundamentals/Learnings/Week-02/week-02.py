# Boolean & Comparison Operators

# 1. Take two numbers and check whether they are equal.

num1 = int(input("First Number:"))
num2 = int(input("Second Number:"))
num3 = num1 == num2 
print(num3)

# 2. Check whether two numbers are different.

num_1 = int(input("First Number"))
num_2 = int(input("Second Number"))
num3 = num_1 != num_2
print(num3)

# 3.  Check whether the first number is greater than the second.

nam_ = int(input("First Number:"))
nam_1 = int(input("Second Number:"))
print(nam_ > nam_1)

# 4. Check whether the first number is greater than or equal to the second

num0 = int(input("First Number:"))
num1 = int(input("Second Number:"))
print(num0 >= num1)

# 5. Print the result of 15 < 8

num1  = 15
num2 = 8
print(15 < 8)

# 6. Take your age and check if it is greater than 18.v

age_ = int(input("Enter Age:"))
criteria_ = age_ > 18
print("I'm adult:", criteria_)

# 7. Take your marks and check if they are greater than 40.

marks_ = int(input("Enter Marks"))
criteria_ = marks_ > 40
print(criteria_)

# 8. Take your height and check if it is greater than 6 feet.

height_ = int(input("Enter Height:"))
criteria_ = height_ > 6
print(criteria_)

# 9. Take two floating-point numbers and compare them.

num1 = float(input("Enter First Float number:"))
num2 = float(input("Enter Second Float Number:"))
print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)

# 10. Compare two cities.
city1 = input("First City:")
city2 = input("Second City:")

print(city1 > city2)
print(city1 < city2)
print(city1 == city2)
print(city1 != city2)
print(city1 > city2)
print(city1 < city2)

# 11. Compare the length of two names using len()

first = "Rudra"
second = "Aanchal"
print(len(first) == len(second))
print(len(first) != len(second))
print(len(first) > len(second))
print(len(first) < len(second))
print(len(first) <= len( second))
print(len(first) >= len(second))

# 12. Compare two mobile numbers (as strings)
a = "4567890"
b = "2346534"
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)
print(a < b)
print(a > b )

# if Statement

# 13. Check if a number is positive.

a = int(input("Enter Number:"))

if a > 0:
    print("Positive number")

# 14. Check if salary is greater than 50000

salarly_ = int(input("Enter Salarly:"))    

if salarly_ > 50000:
    print("Salarly")

# 15. check if attendance is greater than 75%

days_ = int(input("ENTER DAYS:"))
total_ = int(input(" ENTER TOTAL Class:"))
cal_per = days_/total_*100

if cal_per > 75:
    print("passed!Attendance is  %, which is greater than 75%")


# 16. Check if a string length is greater than 5

stri_ = input("Enter Name")
leng_ = len(stri_)

if leng_ > 5:
    print("This string length greater than 5:")


# 16. Check if a password length is greater than 8.

pass_ = input("Enter Password:")
length_pass = len(pass_)

if length_pass > 8:
    print("Password length is greater than 8")

# 17. Scholarship eligibility

scholar_qualification = int(input("Enter Father Income:"))

if scholar_qualification < 500000:
    print("Congralulation! U are eligible for Scholarship") 


# 18. Sports trial eligibility

attended_ = int(input("Entrer days"))
all_overdays = int(input("Total Session"))
total_attend = attended_/all_overdays*100

if  total_attend > 75:
    print("Congratulation! You are Eligible For Scholarship")











 








