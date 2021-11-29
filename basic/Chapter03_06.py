# Chapter03_6
# 파이썬 집합(set)
# 집합 자료형(순서x, 중복x)

# 선언
a = set()
print(type(a))
print(a)
b = set([1, 2 ,3 ,4, 4, 4])
c = set([1, 4, 5, 6, 'bar'])
d = set([1, 2 , 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'baz', 'foo', 'qux'}
f = {42, 'foo', (1, 2, 3), 3.14159}

# 출력
print('a - ', type(a), a, 2 in a)
print('b - ', type(b), b, 2 in b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

# 튜플 변환(set -> tuple)
t=tuple(b)
print('t - ', type(t), t)
print('t - ', t[0], t[1:3])


# 리스트 변환(set -> list)
l=list(c)
l2=list(e)
print('l - ', l)
print('l2 - ', l2)

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6])

print('s1 & s2', s1 & s2)
print('s1 & s2', s1.intersection(s2))

print('s1 | s2', s1 | s2)
print('s1 | s2', s1.union(s2))

print('s1 - s2', s1 - s2)
print('s1 - s2', s1.difference(s2))

# 중복 원소 확인(return bool)
print('s1 & s2', s1.isdisjoint(s2)) # 교집합이 있으면 False, 있으면 True

# 부분 집합 확인
print('subset : ', s1.issubset(s2)) # s1은 s2의부분집합
print('subset : ', s2.issubset(s1)) # s1은 s2의부분집합
print('superset : ', s1.issuperset(s2)) # s2는 s1의 부분집합

# 추가 & 제거
s1 = set([1, 2, 3, 4])

s1.add(5)
print('s1 - ', s1)

s1.remove(2)
print('s1 - ', s1)

# s1.remove(7) # remove 없는원소 키 에러

s1.discard(3)
print('s1 - ', s1)

s1.discard(7) # discard 에러 미발생
print('s1 - ', s1)

s1.clear()
print('s1 - ', s1)

