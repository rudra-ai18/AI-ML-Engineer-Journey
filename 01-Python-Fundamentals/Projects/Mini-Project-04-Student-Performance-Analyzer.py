
print("="*40)
print(" STUDENT aPERFORMANCE ANALYZER")
print("="*40)
print()


# Student Details

def get_student_data():
    name = input(  "Enter Your Name             :")
    age = int(input("Enter Your Age             :"))
    math = int(input("Enter Your Maths Marks    :"))
    pyth = int(input("Enter Your Python Marks   :"))
    eng = int(input("Enter Your English Marks   :"))
    ml = int(input("Enter Your AI/ML Basic Marks:"))
    return name,age,math,pyth,eng,ml


name, age, math, pyth, eng, ml = get_student_data()
dec = ("-"*20, "MARKS", "-"*20)    

print()

def get_calculate_total(math,pyth,eng,ml):
    total = math + pyth + eng + ml
    return total
total = get_calculate_total(math, pyth, eng, ml)


 


def get_calculate_avg(total):
    avg = total/4
    return avg








