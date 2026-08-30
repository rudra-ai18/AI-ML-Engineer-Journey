print("="* 60)
print("      STUDENT INFORMATION MANAGEMENT SYSTEM")
print("="* 60)

print()



print("\n" + "=" * 60)
print("👤 PERSONAL INFORMATION")
print("=" * 60)

name = input("Enter Full Name       : ")
father_name = input("Enter Father's Name   : ")
mother_name = input("Enter Mother's Name   : ")
age = int(input("Enter Age             : "))
dob = input("Enter Date of Birth   : ")
city = input("Enter City            : ")
state = input("Enter State           : ")

print("\n" + "-" * 60)
print("PERSONAL INFORMATION")
print("-" * 60)
print("Full Name       :", name)
print("Father's Name   :", father_name)
print("Mother's Name   :", mother_name)
print("Age             :", age)
print("Date of Birth   :", dob)
print("City            :", city)
print("State           :", state)

print("\n" + "=" * 60)
print("📚 SUBJECT MARKS")
print("=" * 60)

sub1 = int(input("Enter Python Marks        : "))
sub2 = int(input("Enter Mathematics Marks   : "))
sub3 = int(input("Enter English Marks       : "))
sub4 = int(input("Enter AI Fundamentals     : "))
sub5 = int(input("Enter Statistics Marks    : "))

total_marks = sub1 + sub2 + sub3 + sub4 + sub5
average_marks = total_marks / 5
percentage = (total_marks / 500) * 100

print("\n" + "-" * 60)
print("SUBJECT MARKS")
print("-" * 60)
print("Python Marks        :", sub1)
print("Mathematics Marks   :", sub2)
print("English Marks       :", sub3)
print("AI Fundamentals     :", sub4)
print("Statistics Marks    :", sub5)
print("-" * 60)
print("Total Marks         :", total_marks)
print("Average Marks       :", round(average_marks, 2))
print("Percentage          :", round(percentage, 2), "%")








height_ = float(input("Height:")) # in meters
weight_ = float(input("weight:"))
bmi_   = weight_//height_*height_

print()

print("💪 HEALTH INFORMATION")
print("="* 60)
print(height_)
print(weight_)
print("BMI:", bmi_)

print()

print("💰 FEE DETAILS")
print("="* 60)
admi = int(input("Admission fee:"))
tuit = int(input("tuition fee:"))
library_f = int(input("Library fee:"))
exam_ = int(input("Exam Fee:"))
total = admi + tuit + library_f + exam_

print()

print("💰 FEE DETAILS")
print("="* 60)

print(admi)
print(tuit)
print(library_f)
print(exam_)
print("Total fee:", total)

print()
print("📞 CONTACT INFORMATION")
print("="* 60)
myinf = int(input("Mobile Number:"))
mail = input("Email:")
Adress = input("Address:")

print()
print("📞 CONTACT INFORMATION")
print("="* 60)
print(Adress)
print(myinf)
print(mail)
print(Adress)

print()

print("="* 60)
print("THANK YOU FOR USING THIS SYSTEM")
print("="* 60)













