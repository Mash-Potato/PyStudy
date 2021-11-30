# Chapter 05_1
# 파이썬 함수(function)
# 함수의 장점
# 1.함수 단위로 설계, 개발 가능
# 2.코드의 재사용성
# 3.코드의 안정성, 지정 개발로 수정이 쉬움
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def function_name(parameter):
#     code

# 예제1
def first_func(w):
    print("Hello,", w)


word = "Good boy"

first_func(word)
print(first_func)


# 예제2
def return_func(w):
    value = "Hello," + str(w)
    return value


c = return_func("Good boy2")
print(c)


# 예제3(다중 반환)
def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3


a1, a2, a3 = func_mul(10)
print(a1, a2, a3)


# 튜플 리턴
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)


q = func_mul2(20)
print(type(q), q, list(q))


# 리스트 리턴
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]


p = func_mul2(30)
print(type(p), p, set(p))


# 딕셔너리 리턴
def func_mul3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'v1': y1, 'v2': y2, 'v3': y3}


d = func_mul3(30)
print(type(d), d, d.get('v2'), d.items(), d.keys())

# 중요
# *args, **kwargs ex) func_mul3(*args, **kwargs)

print()

# *args(언팩킹) 가변 인자 사용


def args_func1(*args):  # 매개변수 명 자유
    for i, v in enumerate(args):
        print('Result : {}'.format(i), v)  # 튜플 넘어올때 자주 사용
    print('-------------')


args_func1('Lee')
args_func1('Lee', 'park')
args_func1('Lee', 'park', 'Kim')


def args_func2(args):  # 매개변수 명 자유
    for i, v in enumerate(args):
        print('Result : {}'.format(i), v)  # *=튜플 넘어올때 자주 사용
    print('-------------')


args_func2('Lee')

# **kwargs(언팩킹)


def kwargs_func(**kwargs):  # 매개변수 명 자유 **=딕셔너리 형태
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print('-------------')


kwargs_func(name='Kim')
kwargs_func(name1='Kim', name2='Lee', name3='Goo', sendSMS=True)


# 전체 혼합
def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)


example(10, 20, "Lee", "Kim", "Park", "cho", age1=20, age2=30, age3=40)


# 중첩 함수
def nested_func(num):
    def func_in_func(num2):
        print(num2)
    print("in func")
    func_in_func(num + 100)


nested_func(100)

# 실행 불가
# func_in_func(1000)

# 람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화
# 남발 시 가독성 오히려 감소


# def mul_func(x, y):
#    return x * y

# lambda x, y:x * y

# 일반적 함수 -> 할당
def mul_func(x, y):
    return x * y


print(mul_func(10, 50))

mul_func_var = mul_func
print(mul_func_var(20, 50))

# 람다 함수 -> 할당
lambda_mul_func = lambda x, y: x * y
print(lambda_mul_func(50, 50))


def func_final(x, y, func):  # 함수를 인자로 받을때 람다 사용
    print(">>>>>>", x * y * func(100, 100))


func_final(10, 20, lambda x, y: x * y) # 함수를 인자로 받을때 람다 사용
func_final(10, 20, lambda_mul_func) # 함수를 인자로 받을때 람다 사용
func_final(10, 20, mul_func_var)
