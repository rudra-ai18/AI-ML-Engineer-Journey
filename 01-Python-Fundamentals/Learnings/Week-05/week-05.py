#list basics and indexing

# 1. Create a list of 5 fruits and print it.

fruit = ["Orange","Mango","Apple","Banana","Papaya"]
print(fruit)

# 2. Create a list of 5 numbers and print it.

num = [45,55,54,44,54.8]
print(num)


# 3.  Print the first element of a list.

num = [45,65,54,90]
print(num[0])

# 4. Print the lat element of a list.

num = [23,54,43,54]
print(num[3])

# 5.  Print the length of a list.

num = [23,"e",54,76.9]

for i in range(len(num)):
    print(i)

# 6. Check the data type of a list.

check = [35,"rudra",54.7,"t"]
print(type(check))

# 7.  Take 5 numbers from the user and store them in a list.

a = int(input("Enter First Number"))
b = int(input("Enter Second Number"))
c = int(input("Enter Third Number"))
d = int(input("Enter Fourth Number"))
e = int(input("Enter Fifth Number"))

list = [a,b,c,d,e]
print(list)

# 8.  Find the first 3 elements using slicing. 

name = ["rudra",45,45.6,87,98]
print(name[1:3:1])

# 9. Reverse a list using slicing.

num = [45,54,90.00,54,9]
print(num[-1:-5:-1])

# 10.  Print elements at even/odd indexes

num = [34,54,65,35]
print(num[0:3:2])


    