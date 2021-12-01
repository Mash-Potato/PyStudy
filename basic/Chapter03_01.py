# Chapter03_1
# 숫자형

# 파이썬 지원 자료형
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자형(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전
"""

# 데이터 타입
str1 = "python"
bool = True
str2 = 'Anaconda'
float_v = 10.0 #10.0! = 10
int_v = 7
list = [str1, str2]
print(list)
dict = {
    "name":"Machine Learning",
    "version":2.0
}
tuple = (7, 8, 9)
tuple2 = 7, 8, 9
set = {3, 5, 7}

# 데이터 출력
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float_v))
print(type(int_v))
print(type(dict))
print(type(tuple))
print(type(tuple2))
print(type(set))

# 숫자형 연산자
"""
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절댓값
pow(x,y) x ** y
"""

# 정수 선언
i = 77
i2 = -14
big_int = 7777777777777777777999999999999999999999999

# 정수 출력
print(i)
print(i2)
print(big_int)
print()

# 실수 출력
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3/9
print(f)
print(f2)
print(f3)
print(f4)

# 연산 실습
i1 = 10
i2 = 3
print("here :", i1/i2)  # 실수 출력
print("here :", i1//i2)  # 정수 출력
big_int1 = 77777777777777777999999999999999999234
big_int2 = 34534654345634565143653134523341536345
f1 = 1.234
f2 = 4.567

# +
print(">>>>>+")
print("i1 + i2 : ", i1 + i2)
print("f1 + f2 : ", f1 + f2)
print("big_int1 + big_int2 : ", big_int1 + big_int2)

# -
print(">>>>>-")
print("i1 - i2 : ", i1 - i2)
print("f1 - f2 : ", f1 - f2)
print("big_int1 - big_int2 : ", big_int1 - big_int2)

# *
print(">>>>>*")
print("i1 * i2 : ", i1 * i2)
print("f1 * f2 : ", f1 * f2)
print("big_int1 * big_int2 : ", big_int1 * big_int2)

# / (//몫, /실수 출력)
print(">>>>>/")
print("i1 / i2 : ", i1 / i2)
print("f1 / f2 : ", f1 / f2)
print("big_int1 / big_int2 : ", big_int1 / big_int2)
print()

# 형 변환 실습
a = 3.
b = 6
c = .7
d = 12.7

# 타입 출력
print(type(a), type(b), type(c), type(d))

# 형 변환
print(float(b))
print(int(c))
print(int(True))
print(int(False))
print(float(False))
print(complex(3))
print(complex('3')) # 문자형 -> 숫자형
print(complex(False)) # 문자형 -> 숫자형

# 수치 연산 함수
print(abs(-7))

x, y = divmod(100,8)
print(x, y)
print(pow(5,3), 5 ** 3)

# 외부 모듈
import math

print(math.ceil(5.1)) # x 이상의 수에서 가장 작은 정수
print(math.pi) # 원주율








