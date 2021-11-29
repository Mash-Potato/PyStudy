# Chapter03_5
# 파이썬 딕셔너리(Dictionary)
# 범용적으로 가장 많이 사용 (JSON)
# 딕셔너리 자료형(순서X, 키 중복X, 수정o, 삭제o)

# 선언
a = {'name': 'Kim', 'phone': '01033337777', 'birth': '870514'}
b = {0: 'Hello Python'}
c = {'arr': [1, 2, 3, 4]}
d = {
    'Name': 'Niceman',
    'City': 'Seoul',
    'Age': 33,
    'Grade': 'A',
    'Status': True
}
e = dict([
    ('Name', 'Niceman'),
    ('City', 'Seoul'),
    ('Age', 33),
    ('Grade', 'A'),
    ('Status', True)
])
f = dict(
    Name='Niceman',
    City='Seoul',
    Age=33,
    Grade='A',
    Status=True
)

# a=[f1, f2, f3..] 리스트로 학생의 정보 입력.

# 출력
print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)
print()

print('a - ', a['name']) # 키 존재x -> 에러 발생
print('a - ', a.get('name1')) # 키 존재x -> None 보통 get씀.
print('b - ', b[0])
print('b - ', b.get(0))
print('f - ', f.get('City'))
print('f - ', f.get('Age'))

# 딕셔너리 추가
a['address'] = 'Seoul'
print('a - ', a)
a['name'] = 'Seoul'
print('a - ', a)
a['rank'] = [1, 2, 3]
print('a - ', a)
print()

# 딕셔너리 개수(Key의 개수)
print('a - ', len(a))
print('b - ', len(b))
print('c - ', len(c))
print('d - ', len(d))

# dict_keys, dict_values, dict_items : 반복문(__iter__)에서 사용 가능
print(dir(dict))
print('a - ', a.keys())
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())
print('a - ', list(a.keys()))
print('b - ', list(b.keys()))

print()

print('a - ', a.values())
print('b - ', b.values())
print('c - ', c.values())

print('a - ', list(a.values()))
print('b - ', list(b.values()))

print()

print('a - ', a.items())
print('b - ', b.items())
print('c - ', c.items())

print()

print('a - ', a.pop('name'))
print('a - ', a)
print('c - ', c.pop('arr'))
print('c - ', c)

print()

print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)

print()

print('a - ', 'birth' in a)
print('d - ', 'City' in d)
print('d - ', 'city' in d)

# 수정
a['test'] = 'test_dict'
print('a - ', a)
a['address'] = 'dj'
print('a - ', a)
a.update(birth='910904')
print('a - ', a)
temp = {'address': 'Busan'}
a.update(temp)
print('a - ', a)