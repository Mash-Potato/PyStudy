# Chapter03_3
# 파이썬 리스트 (타언어는 배열)
# 자료구조에서 중요
# 리스트 자료형(순서o, 중복o, 수정o 삭제o)

# 선언
a = []
print(type(a))
b = list()
c = [70, 75, 80, 85]
print(len(c))
d = [1000, 10000, 'Ace', 'Base', 'Captain', 'b']
e = [1000, 10000, ['Ace', 'Base', 'Captain']]
f = [21.42, 'foobar', 3, 4, False, 3.14159]
tmp = ["P 3000 5","S 500 3"]
n = int(input())
answer = [-1] * n

# 인덱싱
print('>>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', list(e[-1][1]))

# 슬라이싱
print('>>>>>>')
print('d - ', d[0:3])
print('e - ', e[-1][1:3])

# 리스트 연산
print('>>>>>>')
print('c + d',c+d)
print('c * 3',c*3)
print("'Test' + c[0]", 'Test' + str(c[0]))

# 값 비교
print(c == c[:3] + c[3:])
print(c)
print(c[:3])
print(c[3:])
print()

# Identity(id)
tmp = c
print(tmp, c)
print(id(tmp))
print(id(c))

# 리스트 수정, 삭제
print('>>>>>>')
c[0]=4
print('c - ', c)
c[1:2] = ['a', 'b', 'c'] # [['a', 'b', 'c']] 리스트에 리스트추가
print('c - ', c)
c[1] = ['a', 'b', 'c'] # 리스트안에 리스트추가 ([['a', 'b', 'c']] 동일)
print('c - ', c)
c[1:3] = [] # 삭제 (보통 이렇게안함)
print('c - ', c)
del c[2] # 삭제(통상)
print('c - ', c)
print()

# 리스트 함수
a = [5, 2, 3, 1, 4, 999]
print('a - ', a)
a.append(10) # 추가
print('a - ', a)
a.sort() # 정렬
print('a - ', a)
a.reverse()
print('a - ', a)
print('tta - ', a.index(999), a[0]) # 999의 인덱스 가져오기
a.insert(2, 7) # 소트 후 삽입 append는 맨뒤에 추가 insert는 위치, 값
print('a - ', a)
a.reverse()
# del a[6]
a.append(10) # 추가
a.remove(10) # 하나만 삭제
print('a - ', a)
print('a - ', a.pop()) # LIFO마지막 index 원소 삭제 (자바에서 stack.pop)
print('a - ', a)
print('a - ', a.count(4)) # 4의 갯수가 1개가있다.
print('a - ', a.count("사과")) # 4의 갯수가 1개가있다.
ex = [8, 9]
a.extend(ex)
print('a - ', a)
ex.clear() # clear 사용가능.
print('this ', ex)

# 삭제 : remove, pop, del

# 반복문 활용
while a:
    data = a.pop()
    print(data)