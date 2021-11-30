# Chapter04_3
# 파이썬 반복문 in 흐름 제어(flow control)
# while 실습

# while <expression>:  while == if 동일
#     <statement(s)>

# 예제1
n = 5
while n > 0:
    print(n)
    n -= 1

# 예제2
a = ['foo', 'bar', 'baz']

while a:  # a == True 무한반복
    print(a.pop())  # a.pop(-1) 동일, 보통 for

print()

# 예제3
# break
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print("Loop Ended.")

print()

# 예제4
# continue
m = 5
while m > 0:
    m -= 1
    if m == 2:
        continue
    print(m)
print("Loop Ended.")

# if 중첩
# 예제5
i = 1
while i <= 10:
    print('i:', i)
    if i == 6:
        break
    i += 1

# while - else 구문
# 예제6
n = 10
while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break
else:
    print('else out.')

print()

# 예제7
a = ['foo', 'bar', 'baz', 'qux']
s = 'baz'
i = 0
while i < len(a):
    if a[i] == s:
        print(s, "found!")
        break
    i += 1
else:
    print(s, "not found in list.")
    
# 무한 반복
# while True:
#     print('Foo')

# 예제8
a = ['foo', 'bar', 'baz']
while True:
    if not a:
        break
    print(a.pop())