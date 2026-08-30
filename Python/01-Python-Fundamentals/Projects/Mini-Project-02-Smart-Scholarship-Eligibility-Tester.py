print("="* 60)
print("     🎓 SMART SCHOLARSHIP TESTER SYSTEM 🎓     ")
print("="* 60)

print()

print("Welcome")

print()
name = input("Enter Name          : ")
age = int(input("Enter Age           : "))
sub1 = float(input("Enter Maths Marks   : "))
sub2 = float(input("Enter Science Marks : "))
sub3 = float(input("Enter English Marks : "))
attendance = float(input("Enter Attendance    : "))
income = int(input("Enter Family Income : "))

total = sub1 + sub2 + sub3
avg = total/3
scholarship_status = ""
reason = ""



if avg >= 90 and attendance >= 90 and income <= 300000:
    
    scholarship_status = "Full Scholarship"
    reason = "Excellent Performance"

elif avg >= 80 and attendance >= 80:
    
    scholarship_status = "Half Scholarship"
    reason = ("Good Performance")

elif avg >= 70 and attendance >= 70:
    
    scholarship_status  = "Merit Certificate"
    reason = "Average Performance"

else:

    scholarship_status = "Not Eligible"
    reason = "Criteria not met"


print()

print("="* 30)
print ("  Result Summary  ")
print("="* 30)

print()

print("Name          :", name)
print("Age           :", age) 

print()

print("Maths Marks   :", sub1)
print("Science Marks :", sub2)
print("English Marks :", sub3)

print()
print("Attendance    :", str(attendance) + "%")
print("Family Income :", income)
print()
print("-"* 40)
print()
print("Total Marks   :", total)
print("Average       :", avg)
print()
print("Scholarship :", scholarship_status)
print("Reason      :", reason)

print()
print("="* 40)
print(" THANK YOU ")
print("="* 40)
    
    


