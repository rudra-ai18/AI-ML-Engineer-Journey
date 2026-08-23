
print("="*40)
print(" STUDENT DETAILS")
print("="*40)
print()


# Student Details

def get_student_data():
    name =     input(" Enter Your Name              :")
    age =  int(input(" Enter Your Age               :"))
    math = int(input(" Enter Your Maths Marks       :"))
    pyth = int(input(" Enter Your Python Marks      :"))
    eng =  int(input("  Enter Your English Marks    :"))
    ml =   int(input(" Enter Your AI/ML Basic Marks :"))
    return name,age,math,pyth,eng,ml





def calculate_total(math,pyth,eng,ml):
    total = math + pyth + eng + ml
    return total

name, age, math, pyth, eng, ml = get_student_data()
total = calculate_total( math, pyth, eng, ml)


 


def calculate_avg(total):
    avg = total/4
    return avg

def calculate_grade(avg):
    if avg >=90:
        grade = "A+"
    elif avg >= 80:
        grade = "A"   
    elif avg >= 70:
        grade = "B"   
    elif avg >= 60:
        grade = "C"    
    elif avg >= 50:
        grade = "D"
    elif avg >= 40:
        grade = "E"    
    else:
        grade ="F"



    return grade

avg = calculate_avg(total)
grade = calculate_grade(avg)


def check_result(avg):
    if avg >= 50:
        status = "pass"
    else:
        status = "fail"    


    return status  

avg = calculate_avg(total)
grade = calculate_grade(avg)  


status = check_result(avg)

def display_report(name, age, math, pyth, eng, ml, total, avg, grade, status):
    display_report(name, age, math, pyth, eng, ml, total, avg, grade, status)
    







print("="*40)
print(" STUDENT PERFORMANCE ANALYZER")
print("="*40)
print()


print("Name:", name)
print("Age :", age)
print()
print("Maths :", math) 
print("Python:",pyth)
print("English:",eng )    
print("AI/ML:", ml)
print()

print("-"*40) 
print()
print("Total  :",total)
print("Average:",avg)
print("Grade  :",grade)
print("Result :",status)
print()
print("="*40)
















