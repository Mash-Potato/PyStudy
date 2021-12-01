# Chapter06_2
# 파이썬 모듈
# Module : 함수, 변수, 클래스 등 파이썬 구성 요소를 모아놓은 파일 ex)문자, 메일을 보내주는 모듈
# 모듈화 : 재사용, 공용 사용할 수 있게

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y



if __name__ == '__main__':
    print('-' * 15)
    print('called! __main__')
    print(add(5, 5))
    print(subtract(15, 5))
    print(multiply(5, 5))
    print(divide(10, 2))
    print(power(5, 3))
    print(power(1, 1))
    print('-' * 15)
