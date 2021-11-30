# Chapter04_2
# 파이썬 반복문 in 흐름 제어(flow control)
# for 실습

# 코딩의 핵심
# for in <Collection>
#   <loop body>

for v1 in range(10):  # 0 ~ 9
    print('v1 is :', v1)

print()

for v2 in range(1, 11):  # 1 ~ 10
    print('v2 is :', v2)

print()

for v3 in range(1, 11, 2):
    print('v3 is :', v3)  # 홀수

print()

for v4 in range(2, 11, 2):
    print('v4 is :', v4)  # 짝수

print()

# 1~1000 합
sum1 = 0
for s1 in range(1, 1001):
    sum1 += s1

print('1 ~ 1000 sum :', sum1)

print('1 ~ 1000 sum :', sum(range(1, 1001)))

print(type(range(1, 11)), range(1, 11))

for s1 in range(4, 1001, 4):
    print(s1)

print('1 ~ 1000 4의 배수의 합 :', sum(range(4, 1001, 4)))
# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip (for 사용가능)

# 예제1
names = ['Kim', 'Park', 'Cho', 'Lee', 'Yoo']
for name in names:
    print('You are :', name)  # Java for-each

# 예제2
lotto_numbers = [11, 19, 21, 28, 36, 37]
for number in lotto_numbers:
    print('Current number :', number)

# 예제3
str1 = "League of Legend"
for x in str1:
    print(x)

# 예제4
tu1 = (13, 14, 15)
for x in tu1:
    print(x)

# 예제5
set1 = {13, 14, 15}
for x in set1:
    print(x)

print()

# 예제6
dict1 = {
    "name": "son",
    "age": 33,
    "city": "seoul"
}
for key in dict1:
    print('value :', dict1[key])  # 자바랑 달리 dict1에 dict1[x]가 가능

for key in dict1:
    print('value :', dict1.get(key))  # 동일

for v in dict1.values():  # 동일
    print('value :', v)

print()

for x in dict1:
    print(dict1['name'])  # 가능 3번연속 son 출력

print()

for key in dict1:
    print('Keys :', key)

print()

# 예제7
name = "FineApple"
for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())

# break
numbers2 = [10, 20, 30, 40, 50, 60, 100, 70, 80, 90, 1, 2, 3]
for x in numbers2:
    if x == 100:
        print("found : 100!")
        break
    else:
        print("not found :", x)

# continue
lt = ["1", 2, 5, True, 4.3, complex(4)]
for v in lt:
    if type(v) is bool:  # 자료형(type) 대조할때 is
        continue
    print("current type :", v, type(v))
    print("multiply by 2", v * 2)
    print(True * 3)  # True == 1

# for - else
numbers3 = [10, 20, 30, 40, 50, 60, 100, 70, 80, 90, 1, 2, 3]
for n in numbers3:
    if n == 55:
        print("Found : 55!")
        break
else:  # for 전부 반복하고 else 실행
    print("Not Found : 55")

# 구구단 출력
for i in range(2, 10):
    for j in range(1, 10):
        print('{:4d}'.format(i * j), end='')
    print()

# 변환 예제
name2 = 'Aceman'

print('Reversed :', reversed(name2))
print('List :', list(reversed(name2)))
print('Tuple :', tuple(reversed(name2)))
print('Set :', set(reversed(name2))) # 순서x, 중복x
