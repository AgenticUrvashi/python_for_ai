# Level 1: Easy ⭐

# Question 1


x = 10
y = 5
print(x + y)
# ans : 15

print("=========================")


# Question 2

a = 7
a = a + 3
print(a)
# ans : 10

print("===============================")


# Question 3

num = 8
if num > 5:
    print("Big")
else:
    print("Small")
# ans : Big

print("===========================")

# Question 4

for i in range(5):
    print(i)
# ans : 0
#       1
#       2
#       3
#       4

print("===========================")

# Question 5
s = 0
for i in range(1, 6):
    s = s + i
print(s)
# ans : 15

print("===================")

# Level 2: Loops ⭐⭐


# Question 6

s = 0
for i in range(1, 6):
    if i % 2 == 0:
        s = s + i
print(s)
# ans : 6

print("=======================")

# Question 7

for i in range(2, 10, 2):
    print(i)
# ans : 2
#       4
#       6
#       8

print("==========================")

# Question 8

count = 0
for i in range(5):
    count += i
print(count)
# ans : 10

print("================================")

# Question 9

for i in range(5, 0, -1):
    print(i)
# ans : 5
#       4
#       3
#       2
#       1
#      -2

print("=============================")

# Question 10

x = 1
for i in range(4):
    x = x * 2
print(x)
# ans : 2
#       4
#       8
#       16

print("===============================")

# Level 3: Nested Loops ⭐⭐⭐


# Question 11

for i in range(2):
    for j in range(3):
        print(i, j)
# ans : (0,0)
#       (0,1)
#       (0,2)
#       (1,0)
#       (1,1)
#       (1,2)

print("=============================")

# Question 12

count = 0
for i in range(3):
    for j in range(2):
        count += 1
print(count)
# ans : 6

print("========================")

# Question 13

for i in range(1, 4):
    for j in range(i):
        print("*", end="")
    print()
# ans : *
#       **
#       ***

print("=============================")

# Level 4: While Loop ⭐⭐⭐


# Question 14

i = 1
while i <= 5:
    print(i)
    i += 2
# ans : 1
#       3
#       5

print("===============================")

# Question 15

n = 10
while n > 0:
    n -= 3
    print(n)
# ans : 7
#       4
#       1

print("================================")

# Question 16

x = 1
while x < 20:
    x = x * 3
print(x)
# ans : 3
#       9
#       27

print("=======================")


# Level 5: Logic ⭐⭐⭐⭐


# Question 17

x = 5

if x % 2 == 0:
    print("A")
elif x % 5 == 0:
    print("B")
else:
    print("C")
# ans : B

print("==============================")

# Question 18

s = 0

for i in range(1, 5):
    s += i

    if s > 5:
        break

print(s)
# ans : 1
#       3
#       6

print("================================")

# Question 19

for i in range(1, 6):
    if i == 3:
        continue
    print(i)
# ans : 1
#       2
#       4
#       5

print("==============================")


# Question 20

x = 0

for i in range(3):
    x += i

for j in range(2):
    x *= 2

print(x)
# ans : i = 6
#       j = 12
#       x = 12

print("===============================")

# Challenge Questions ⭐⭐⭐⭐⭐


# Challenge 1
x = 1

for i in range(1, 5):
    x = x + i

    if x % 2 == 0:
        x = x * 2

print(x)
# ans : 19

print("==========================")

# Challenge 2
total = 0

for i in range(1, 4):
    for j in range(1, 3):
        total += i * j

print(total)
# ans : 18

print("============================")

# Challenge 3
a = 3
b = 5

a, b = b, a

print(a)
print(b)
# ans : 5
#       3

print("=========================================== pesudocode ======================================")

# 🟢 Easy Level

# 1. Print "Hello, World!".

print("Hello, World!")

print("-----------------------------------------------------------")

# 2. Input a number and print whether it is even or odd.

user_input = int(input("enter any number to identify even or odd: "))
if user_input%2==0:
    print("even")
else:
    print("odd")

print("----------------------------------------------------------")

# 3. Input two numbers and print the larger one.

nums1 = int(input("enter any number for check who is greater: "))
nums2 = int(input("enter another any number except nums1: "))
if nums1>nums2:
    print(nums1)
else:
    print(nums2)

print("---------------------------------------------------------")

# 4. Input a number and print its square.

num = int(input("enter number for squaring: "))
print(num*num)

print("----------------------------------------------------------")

# 5. Input a student's marks and print:
#  Pass (marks ≥ 35)
#  Fail (marks < 35)

mark = int(input("enter your marks to check you are fail or pass: "))
if mark>=35:
    print("PASS")
elif mark<35:
    print("FAIL")

print("--------------------------------------------------------")

# 🟡 Medium Level

# 6. Input three numbers and print the largest.

num1 = int(input("enter 1st number to check who is greater :  "))
num2 = int(input("enter 2nd number to check who is greater :  "))
num3 = int(input("enter 3rd number to check who is greater :  "))
if num1>num2 and num3:
    print(num1)
elif num2>num1 and num3:
    print(num2)
else:
    print(num3)

print("------------------------------------------------------")

# 7. Find the sum of numbers from 1 to N.

N = int(input("enter your number for sum N numbers: "))
sum = 0
for i in range(1,N+1):
    sum += i

print(sum)

print("--------------------------------------------------")

# 8. Find the factorial of a number.

N = int(input("enter any number for factorial : "))
fact = 1
for i in range(1,N+1):
    fact = fact * i
print("factorial = ", fact )

print("----------------------------------------------------")


# 9. Count how many numbers between 1 and N are divisible by 3.

N = int(input("enter any number for check divisible 3: "))
count = 0
for i in range(1,N+1):
    if i % 3 == 0:
        count += 1

print(count)

print("------------------------------------------------------")

# 10. Reverse the digits of a number.

N = int(input("enter your number for reverse: "))
reverse = 0
while N>0:
    digit = N % 10
    reverse = reverse*10 + digit 
    N = N // 10

print(reverse)

print("--------------------------------------------------------")

# 11. Count the number of digits in a number.

nums = 12345670
count = 0
while nums>0:
    nums = nums // 10
    count += 1

print(count)

print("-----------------------------------------------------")

# 12. Check whether a number is a prime number.

nums = 13
is_prime = True
for i in range(2,nums):
    if nums % i == 0:
        is_prime = False
        break

if is_prime:
    print("prime number")
else:
    print("not prime")

print("---------------------------------------------------")

# 🟠 Hard Level

# 13. Print the Fibonacci series up to N terms.

n = int(input("enter number of term for sum: "))

a = 0               #har number = pichhle do numbers ka sum.
b = 1

for i in range(n):
    print(a, end="")
    c = a + b
    a = b
    b = c

print("-----------------------------------------------")

# 14. Find the greatest common divisor (GCD) of two numbers.

num1 = 120
num2 = 150

gcd = 1                   #gretest common divisor

for i in range(1,min(num1,num2)+ 1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i

print("GCD =", gcd)

print("-------------------------------------------------------")

# 15. Find the least common multiple (LCM) of two numbers.

num1 = int(input("enter 1st number for finding LCM: "))
num2 = int(input("enter 2nd number for finding LCM: "))
lcm = max(num1,num2)
while True:
    if lcm % num1 == 0 and lcm % num2 == 0:
        print("LCM = ",lcm)
        break
    else:
        lcm += 1

print("------------------------------------------------------")

# 16. Check whether a number is an Armstrong number.

num = int(input("enter any number for armstrong nuber: "))
original = num
digits = len(str(num))                       # 153 = 3 digit , 1 ka cube + 5 ka cube + 3 ka cube = 153 
sum = 0

while num>0:
    digit = num % 10
    sum += digit ** digits
    num = num // 10

if sum == original:
    print("armstrong number")
else:
    print("not")

print("------------------------------------------------------")

# 17. Check whether a number is a palindrome.

word = input("enter any word for palindrome: ")
original = word
reverse = ""
for i in word:
    reverse = i + reverse

if reverse == original:
    print("palindrome")
else:
    print("not palindrome")

print("------------------------------------------------------")

# 18. Find the largest element in a list.

user_list = list(map(int,input("enter any numbers without coma and with space for finding largest: ").split()))
largest = user_list[0]
for i in user_list:
    if i > largest:
        largest = i
print("largest= ",largest)

print("---------------------------------------------------------")

# 19. Count the number of even and odd elements in a list.

nums = [23,54,67,12,87,45,80]
even = 0
odd = 0
for i in nums:
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print(f"Even = {even}, Odd = {odd}")

print("-------------------------------------------------------")

# 20. Find the second largest number in a list.

nums = [34,65,87,92,45,67,23]
largest = nums[0]
second_largest = nums[0]
for i in nums:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i
    
print(second_largest)

print("-----------------------------------------------------")

# 🔴 Dry Run / Logic-Based

# 21. Write pseudocode to find the sum of all even numbers in a list.

'''1. in starting take user's input for list.
   2. then take value of sum is equals to zero.
   3. take for loop for one by one element.
   4. take condition for even values.
   5. add value in sum.
   6. then print sum.'''

print("--------------------------------------------------------")

# 22. Write pseudocode to find the average of N numbers.

'''1. in starting take user's input 
   2. initilize with total = 0
   3. take for loop for add elements one by one.
   4. calculate the length of input with len(user's input) 
   5. average = total / len(user's input)
   6. print the average'''

print("---------------------------------------------------------")

# 23. Write pseudocode to swap two numbers without using a third variable.

'''1. initilize with two variables a and b having values 3 and 5.
   2. swap this values with each other using this:
      a,b = b,a
   3. print a and b separately.'''

print("----------------------------------------------------------")

# 24. Write pseudocode to remove duplicate elements from a list.

'''1. take a list from user.
   2. create new variable and store the data using this:
      unique_list = set(user_list)
   3. print the variable.
   4. because of creating new variable the original list is safe.'''

print("-----------------------------------------------------------")

# 25. Write pseudocode to search for an element in a list using linear search.

# pseudocode: 

'''1. take two variables salary and target.
   2. take for loop for check element one by one.
   3. fix the condition for found inside the loop.
   4. if no element is matches after the loop end:
       print("not found").'''

# code:

salary = [200000,400000,600000,700000,500000]
target = int(input("enter the number which you want to search: "))

for i in salary:
    if i == target:
        print("FOUND !!!")
        break
else:
    print("NOT FOUND")
    
print("-----------------------------------------------------------------")

print("===================================== function ===================================")

print("------------------------------------------------------------------")

# Level 1 (Easy)

# 1. Ek function greet() banao jo print kare:
# Hello, Welcome!

def greet():
    print("Hello,Welcome!")

print("-----------------------------------------------------------------")

# 2. Ek function square(num) banao jo kisi number ka square print kare.

def square(num):
    print(num*num)

print("-----------------------------------------------------------------")

# 3. Ek function add(a, b) banao jo do numbers ka sum print kare.

def add(a,b):
    print(a+b)

print("----------------------------------------------------------------")

# 4. Ek function even_odd(n) banao jo bataye number even hai ya odd.

def even_odd(n):
    if n % 2 == 0:
        print("even")
    else:
        print("odd")

even_odd(2)

print("----------------------------------------------------------------------")

# 5. Ek function table(n) banao jo us number ka table print kare.

def table(n):
    for i in range(1,11):
        print(n*i)

print("-------------------------------------------------------------------------")

# 🟡 Level 2 (Parameters + Return)

# 6. Ek function maximum(a, b) banao jo bade number ko return kare.

def maximum(a,b):
    maxi = a
    if maxi>b:
        maxi = a
    else:
        maxi = b
    print(maxi)

print("--------------------------------------------------------------------------")

# 7. Ek function factorial(n) banao jo factorial return kare.

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print("factorial=",fact)

print("--------------------------------------------------------------------------")

# 8. Ek function is_prime(n) banao jo return kare:
# True agar prime ho
# False agar prime na ho

def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            is_prime = False
if is_prime:
    print("True")
else:
    print("False")

print("------------------------------------------------------------------------")

# 9. Ek function count_vowels(text) banao jo string me vowels ki count return kare.

def count_vowels(text):
    text = text.lower()
    count = 0
    for i in text:
        if i in "aeiou":
            count = count +1
    print(count)

# 10. Ek function reverse_string(text) banao jo reverse string return kare.

def reverse_string(text):
    reverse = ""
    for i in text:
        reverse = i + reverse
    print(reverse)

print("-----------------------------------------------------------------------")

# 🟠 Level 3 (Loops + Functions)

# 11. Ek function sum_n(n) banao jo 1 se n tak ka sum return kare.

def sum_n(n):
    total = 0
    for i in range(1,n+1):
        total = total + i
    return total

x = sum_n(5)
print(x)

print("---------------------------------------------------------------------------")

# 12. Ek function count_even(lst) banao jo list me kitne even numbers hain, return kare.

def count_even(lst): 
    count = 0
    for i in lst:
        if i % 2 == 0:
            count = count + 1
    return count

even = count_even(4)
print(even)

print("--------------------------------------------------------------------------")

# 13. Ek function largest(lst) banao jo list ka sabse bada number return kare.

def largest(lst):
    biggest = lst[0]
    for i in lst:
        if i > biggest:
            biggest = i
    return biggest

large = largest([3,8,5,9,0])
print(large)

print("-------------------------------------------------------------------")

# 14. Ek function palindrome(text) banao jo check kare string palindrome hai ya nahi.

def palindrome(text):
    reverse = ""

    for i in text:
        reverse = i + reverse

    if reverse == text:
        return True
    else:
        return False

print("---------------------------------------------------------------------")

# 15. Ek function fibonacci(n) banao jo first n Fibonacci numbers print kare.




# 🔴 Challenge 😈

# 1. Calculator function banao:
# calculator(a, b, op)
# + → addition
# - → subtraction
# * → multiplication
# / → division
# 2. Ek function banao jo list me sirf prime numbers return kare.
# 3. Ek function banao jo sentence me sabse lamba word return kare.
# 4. Ek function banao jo kisi number ke saare factors return kare.
# 5. Ek function banao jo check kare ki string me saare characters unique hain ya nahi.
