# Chapter 05_2
# 파이썬 사용자 입력
# Input 사용법
# 기본타입(str)

# 예제1
name = input("Enter Your Name : ")
grade = input("Enter Your Grade : ")
company = input("Enter Your Company name : ")

print(name, grade, company)

# 예제2
num = input("Enter number : ")
name = input("Enter Your Name : ")
print("type of number", type(num), num *3)
print("type of name", type(name))

# 예제3
first_number = int(input("Enter number1 : "))
second_number = int(input("Enter number2 : "))
total = first_number + second_number
print("first_number + second_number", total)

# 예제4
float_number = float(input("Enter float : "))

print("input float_number : ", float_number * 1.11231)
print("input type : ", type(float_number))

# 예제5
print("FirstName - {0}, LastName - {1}".format(input("Enter first name : "), input("Enter second name : ")))
