
nam01 = input("Enter Full Name      :")
fnam02 = input("Enter Father's Name :")
mnam02 = input("Enter Mother's Name :")       
Nage = int(input(" Enter Age        :"))
Ndate = int(input("Date of Birth    :"))
ncity = input(" Enter City          :")
nstat = input("Enter State          :")

print()
print("👤 PERSONAL INFORMATION")
print("-" * 60)

print("Full Name      :", nam01)
print("Father's Name  :", fnam02)
print("Mother's Name  :", mnam02)
print("Age            :", Nage)
print("Date of Birth  :", Ndate)
print("City           :", ncity)
print("State          :", nstat)



col1 = input(" Enter College Name  :")
col2 = input(" Enter Course Name   :")
col3 = int(input("Enter Semester  :"))
col4 = (input("Enter Roll number  :"))
print()
print("🎓 ACADEMIC INFORMATION")

print("College Name:", col1)
print("Course Name:", col2)
print("Semester:", col3)
print("Roll Number:", col4)





sub1 = int(input("Enter Python Marks       :"))
sub2 = int(input(" Enter Mathematics Marks:"))
sub3 = int(input(" Enter English Marks    :"))
sub4 = int(input(" Enter AI Fundamentals Marks:"))
sub5 = int(input("Enter Statistics Marks:"))
total_marks = sub1 + sub2 + sub3 + sub4 + sub5
Average_marks = total_marks//5
percent = total_marks/500*100

print()
print("🎓 ACADEMIC INFORMATION")
print("-" * 60)
print("College Name      :", col1)
print("Course Name       :", col2)
print("Semester          :", col3)
print("Roll Number       :", col4)


print()

print("Total marks:", total_marks)
print("Average Marks:", Average_marks)
print("Percentage:", percent)

height_ = float(input("Height:")) # in meters
weight_ = float(input("weight:"))
bmi_   = weight_//height_*height_

print()

print("💪 HEALTH INFORMATION")
print("="* 60)
print(height_)
print(weight_)