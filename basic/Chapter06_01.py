# Chapter06_1
# 파이썬 클래스
# OOP, self, 인스턴스 메소드, 인스턴스 변수
# 객체 지향 프로그래밍(object oriented programming)이란
# 클래스 기반의 코딩이며 상속이 가능하다.
# 연필, 책상, 의자, 자동차 등 사물들을 전부 객체화 시킬수 있다. (객체=소프트웨어의 구현할 대상)
# 함수와 마찬가지로 재사용이 용이하다.
# 과거의 절차지향의 보다 개선되고 좋아짐.
# 그로인한 장점
# 1.개선, 수정, 에러가 발생했을시 유지보수가 용이하며 주변에 미치는 악영향 최소화하여 생산성이 향상됨(경제적이다).
# 단점
# 1.무조건 빠른건 아니다. (경우에 따라 절차지향보다 느림)

# 예제1(애견샵)

# 진돗개 =
# 리트리버 =
# 이렇게 될시 견종 이름이 바뀌거나, 견종 추가시, 변수, 코드 추가 -> 코드의 양이 늘어나고 가독성이 떨어짐.

# 클래스 and 인스턴스 차이=클래스는 틀
# 인스턴스는 하나의 클래스를 이용하여 여러가지 종류로 인스턴스화 하여 자기만의 정보를 가지고있음.(변수로 활용할수 있는 대상)
# 클래스 변수 : 직접 접근 가능, 공유
# 인스턴스 변수 : 객체마다 별도 존재
class Dog2(object):  # object 생략 가능.(object 상속), class Dog() 도 사용 가능.
    # 클래스 속성
    species = 'firstdog'  # 클래스 변수(식당의 정수기)

    # 초기화/인스턴스 속성 (=java 생성자) (객체=구현할 대상=개)
    def __init__(self, name, age):
        self.name = name  # 인스턴스 변수
        self.age = age  # 인스턴스 변수

# 클래스 정보
print(Dog2)

# 인스턴스화 (인스턴스=클래스를 가지고 코드에서 사용하는 객체, 인스턴스화=설계도를 바탕으로 구현하는것)
# 인스턴스와 객체의 차이점 = 인스턴스는 객체에 포함되고 자기만의 정보를 가지고 있다.
a = Dog2("ttori", 2)
b = Dog2("baby", 3)
c = Dog2("ttori", 2)

# 비교
print(a == b, id(a), id(b), id(c))  # a, c 파이썬 코드 입장에서는 전혀 다른 객체로 간주(인스턴스화 시킨 것들은 모두 다르다.)

# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
print('dog1', a.__dict__)
print('dog2', b.__dict__)

# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))

print(Dog2.species)
print(a.species)
print(b.species)

# 예제2
# self의 이해
class SelfTest:
    # __init__이 없으면 클래스가 코드를 실행할때 파이썬이 만들어줌 여기서 def __init__(self, name, age): 의 name, age를 안쓰기때문에 필요x
    def func1():  # 클래스 메소드
        print('func1 called')
    def func2(self):
        print(id(self))
        print('func2 called')

f = SelfTest()

print(type(f))
print(dir(f))  # 'func1', 'func2' 이 있다.
print(id(f))
# f.func1()  # 예외 발생
f.func2()  # 인스턴스로 호출

SelfTest.func1()  # 클래스 메소드기 때문에 클래스로 직접 호출
# SelfTest.func2()  # 예외 발생
SelfTest.func2(f)  # 인스턴스로 호출

print()
# 예제3
# 클래스 변수, 인스턴스 변수
class Warehouse:  # Warehouse는 현실세계에 존재(사물화)
    # 클래스 변수
    stock_num = 0  # 재고

    # 생성자, 인스턴스 메소드
    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1

    # 객체 소멸 함수(소멸자)
    def __del__(self):
        Warehouse.stock_num -= 1

# 인스턴스화(붕어빵 2개)
user1 = Warehouse('Lee')
user2 = Warehouse('Cho')
# Warehouse.stock_num = 50  # 직접 접근(1000원내고 2번할수있는데 50번 하게 만듬)
print(Warehouse.stock_num)
print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print('before :', Warehouse.__dict__)
print('>>>', user1.stock_num)  # user1의 네임스페이스에 stock_num이 없지만 Warehouse의 네임스페이스에서 찾음.(공유하기 때문에) 없으면 에러

del user1  # 인스턴스 삭제
print('after :', Warehouse.__dict__)


print()

# 예제4
class Dog:
    species = 'second_dog'

    # 강아지가 갖는 속성
    def __init__(self, name, age):
        self.name=name
        self.age=age

    # 강아지가 갖는 행동
    def info(self):
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}!".format(self.name, sound)

# 인스턴스 생성
c = Dog("july", 4)
d = Dog("marry", 10)
# 메소드 호출
print(c.info())
print(d.info())
# 메소드 호출
print(c.speak('멍'))
print(d.speak('wal'))


