# Chapter08_1
# 파이썬 내장 함수(Built-in Functions)
# 자주 사용하는 함수 위주
# 사용하다보면 자연스럽게 숙달
# str(), int(), tuple() 형변환 이미 학습

# 절대값
# abs()

print(abs(-3))

# all: (and) iterable 요소 검사(True, False)
print(all([1, 2, 3]))
print(all([1, 2, 0]))
print(all([1, 2, '']))

# any : (or) iterable 요소 검사(True, False)
print(any([1, 2, 3]))
print(any([0]))
print(any([0, '']))

# chr : 아스키 -> 문자, ord : 문자 -> 아스키
print(chr(44))
print(chr(67))
print(ord('C'))
print(ord(','))

# enumerate : 인덱스 + iterable 객체 생성
for i, name in enumerate(['abc', 'bcd', 'efg']):
    print(i, name)

# filter : 반복가능한 객체 요소를 지정한 함수 조건에 맞는 값 추출
def conv_pos(x):
    return abs(x) > 2

print(list(filter(conv_pos, [1, -3, 2, 0, -5, 6])))
print(list(filter(lambda x: abs(x) > 2, [1, -3, 2, 0, -5, 6])))

# id : 객체의 주소값(레퍼런스) 반환
print(id(int(5)))
print(id(4))

# len : 요소 길이 반환
print(len('abcdef') - 1)
print(len([1, 2, 3, 4, 5, 6]))

# Max, min : 최대값, 최소값
print(max([1, 2, 3]))
print(max('Python Study'))

print(min([1, 2, 3]))
print(min('Python Study'))
print(ord(' '))
print(min('PythonStudy'))
print(ord('P'))

# map : 반복가능한 객체 요소를 지정한 함수 실행 후 추출
def conv_abs(x):
    return abs(x)

print(list(map(conv_abs, [-3, 2, 0, 5, -5, 6])))
print(list(map(lambda x: abs(x), [-3, 2, 0, 5, -5, 6])))

# pow : 제곱값 반환
print(pow(2, 10))

# range : 반복가능한 객체(iterable) 반환
print(range(1, 10, 2))
print(list(range(1, 10, 2)))
print(list(range(0, -15, -1)))

# round : 반올림
print(round(6.5781, 2))
print(round(6.5781, 1))
print(round(5.6))
print(round(5.4))

# sorted : 반복가능한 객체(iterable) 정렬 후 반환
print(sorted([6, 7, 4, 3, 1, 2]))

a = sorted([6, 7, 4, 3, 1, 2])
print(a)
print(sorted(['p', 'y', 't', 'h', 'o', 'n']))

# sum : 반복가능한 객체(iterable) 합 반환
print(sum([6, 7, 8, 9, 10]))
print(sum(range(1, 100)))

# type : 자료형
print(type(3))
print(type({}))
print(type({''}))
print(type(()))
print(type([]))

# zip : 반복가능한 객체(iterable)의 요소를 묶어서 반환
print(list(zip([(1, 3), (2, 2)])))
print(*[(1, 3), (2, 2)])
print(list(zip(*[(1, 3), (2, 2)])))
print(list(zip([10, 20, 30],[40, 50, 60])))
print(list(zip([10, 20, 30],[40, 50])))
print(zip([10, 20, 30],[40, 50, 60]))
print(type(list(zip([10, 20, 30],[40, 50, 60]))[0]))
