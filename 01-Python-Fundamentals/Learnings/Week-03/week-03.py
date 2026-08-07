# # For loop

# # 1.   6 at a time

# for i in range(7):
#     print(i)

# # 2.  range(start, stop)

# for i in range(2,7):
#     print(i)

# # 3.   range(start, stop, step)

# for i in range(2,11,2):
#     print(i)


# # 4. Reverse counting range(10, 0, -1)

# for i in range(10, 0 ,-1):
#     print(i)

# # 5. Print numbers from 1 to 10 

# for i in range(1,11,1):    
#     print(i)

# # 6. Print numbers from 10 to 1.

# for i in range(10,0,-1):
#     print(i)

# # 7. Print your name 10 times.

# for i in range(5):
#     print("Rudra")


# # 8. Print numbers from 1 to 50

# for i in range(1,50):
#     print(i)


# # 9. Print numbers from 50 to 1

# for i in range(50,0,-1):
#     print(i)

# # 10. Print even numbers from 1 to 20.

# for i in range(0,20,2):
#     print(i) 


# # 11. Print odd numbers from 1 to 20.

# for i in range(1,20,2):
#     print(i)


# # 12. Print multiples of 5 till 100.

# for i in range(5,105,5):
#     print(i)

# # 13. Print squares from 1 to 20.

# for i in range(1, 21):
#     print(i**2)


# # 14. Print cubes from 1 to 15.

# for i in range(1,16):
#     print(i**3)

# # 15. . Print multiplication table of 2

# for i in range(1,11):

#     print(i*2)

# # 16. Print first 25 natural numbers.

# for i in range(1,26):
#     print(i)

# # 17. Print numbers divisible by 3

# for i in range(3,100,3):
#     print(i)

# # 18. Print numbers divisible by both 2 and 5

# for i in range(1,101):
#     if i % 2 == 0 and i % 5 == 0:
#         print(i)

# # 19. Sum of numbers from 1 to 100.
# sum = 0

# for i in range(1,101):
#     sum +=  i
#     print(sum)


# 20. Sum of even numbers till 100.

sum = 0


# for i in range(0,101,2):

#     if i%2 == 0:
#         sum += i
#         print(sum)


# 21. Sum of odd numbers till 100.

sum = 0

# for i in range(1,101,2):
#     if i%2 != 0:
#         sum += i
#         print(sum)

# 22. Print numbers from 100 to 1 using loop.

# for i in range(100,0,-1):
#     print(i)


# 22. Print every third number till 100.

# for i in range(1,101,3):
#     print(i)


# 23.  Accept an integer and Print hello world n times.

# n = int(input("Enter a number"))

# for i in range(n):
#     print("Hello World")

#24. Print natural number up to n

# n = int(input("Enter Number"))

# for i in range(1,n+1):
#     print(i)


# 25. Reverse for loop. Print n to 1.

# n =int(input("Enter number"))

# for i in range(n,0,-1):
#     print(i)

# 26. Take a number as input and print its table.

# n = int(input("Enter a number,Which number table u want:"))

# for i in range(n,(n*10)+1,n):
#     print(i)


# 27. Sum up to n terms.

# n = int(input("Enter a Number"))

# sum = 0

# for i in range(1,n+1):
#     sum = sum + i
#     print(sum)

# 28. Factorial of a number.

# n = int(input("Enter number"))

# multi = 1

# for i in range(1,n+1):
#     multi = multi*i
#     print(multi)

# 29. Print the sum of all even & odd numbers in a range seprately.  

# n = int(input("Enter a number"))

# even = 0
# odd = 0

# for i in range(1,n+1):
#     if i%2 == 0:
#         even = even + i
#     else:
#         odd = odd + i
# print(f"sum of all even{even},odd{odd}")

# 30. Print all the facotrs of numbers 

# n = int(input("Enter Number"))

# for i in range(1,n+1):
#     if n%i == 0:
#         print(i)


 # 31.  Accept a number and check if it a perfect number or not.

# n = int(input("Enter number"))

# for i in range(1,n+1):
#     if n%i == 0:
#         print(i)


# 32. Accept a number and check if it a perfect number or not and print that sum of equal to that perfect number.

n = int(input("Enter number"))

sum = 0

for i in range(1,n):
    if n%i == 0:
        sum = sum + i
                      
if sum == n:
    print("perfect number")
else:
    print("not perfect number")















