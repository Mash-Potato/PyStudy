# Chapter03_4
# 파이썬 튜플(Tuple)
# 리스트와 비교 중요(튜플은 리스트와 2가지 다르다)
# 튜플 자료형(순서o, 중복o, 수정x, 삭제x) =불변(중요한 값일때 사용)
# 팩킹 언팩킹 지원

# 선언
a = ()
b = (1)
print(type(a))
print(type(b)) # 원소가 하나일때는 int
b = (1,)
print(type(b)) # ,추가해줌
c = (11, 12, 13, 14)
d = (100 ,1000, 'Ace', 'Base', 'Captain')
e = (100 ,1000, ('Ace', 'Base', 'Captain'))

# 인덱싱
print('>>>>>')
print('d - ', d[1])
print('d - ', d[0] + d[1])
print('d - ', d[-1])
print('e - ', e[-1])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1])) # 튜플을 리스트로 변환

# 수정x
# d[0]=1500 # 에러발생

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])

# 튜플 연산
print('>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)

# 튜플 함수
a = (5, 2, 3, 1, 4)
print('a - ', a)
print('a - ', a.index(3)) # 3의 인덱스 가져오기
print('a - ', a.count(3)) # 3의 갯수
print()

# 팩킹 & 언팩킹(Packing and Unpacking)

# 팩킹
t = ('foo', 'bar', 'baz', 'quz')

print(t)
print(t[0])
print(t[1])

# 언팩킹1
(x1, x2, x3, x4) = t
print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

# 팩킹 & 언팩킹1
t2 = 1, 2, 3
t3 = 4
x1, x2, x3 = t2
x4, x5, x6 = (4, 5, 6)

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)

