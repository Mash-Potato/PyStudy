# Chapter02_1
# 파이썬 완전 기초
# Print 사용법

# 기본 출력
print('Python Start!') # 보통 작은따옴표 사용
print("Python Start!")
print('''Python Start!''')
print("""Python Start!\n""")

# separator 옵션
print('P','y','t','h','o','n',sep='')
print('010','7777','1234',sep='-')
print('Python','Google.com\n',sep='@')

# end 옵션
print('Welcom to',end=' ')
print('IT News',end=' ')
print('Web Site\n')

# file 옵션
import sys

print('Learn Python\n', file=sys.stdout)

# format 사용(d,s,f) o,x도 있음 d=digit=3,s=string='python',f=float=3.14555
print('%s %s' %('one','two'))
print('{} {}'.format('one','two'))
print('{} {}'.format('one',2))
print('{1} {0}'.format('one\n','two')) # index

# %s
print('%10s' %('nice')) # 10개의 자리를 확보, 양수는 0부터 공백
print('{:>10}'.format('nice')) # >,생략일시 위와 동일

print('%-10s' %('nice')) # 10개의 자리를 확보, 음수는 0부터 대입
print('{:10}'.format('nice')) # <,생략일시 왼쪽부터

print('{:_>10}'.format('nice')) # 빈문자 채움
print('{:^10}'.format('nice')) # 가운데 정렬

print('%.5s' %('nice'))
print('%5s' %('python study')) # 공간이 적어도 모두 출력
print('{:10}'.format('python study')) # 공간이 적어도 모두 출력
print('%.5s' %('python study')) # .이 있을경우 공간만큼 출력후 나머지 절삭
print('{:10.5}'.format('pythonstudy')) # 10공간 확보하고 6글자이후 공백
print()

# %d
print('%d %d' %(1,2))
print('{} {}'.format(1,2))
print()
print('%4d' %(42))
print('%4d' %(42123423452)) # 공간이 적어도 모두 출력
print()
print('{:<4d}'.format(42)) # 문자일경우엔 {:>4} 가능 정수일경우엔 d붙임.
print('{:10}'.format('42')) # 문자열 생략일시 왼쪽부터
print('{:4d}'.format(42)) # 문자열과 달리 정수형일경우 생략하면 오른쪽부터
print()

# %f
print('%f'% (3.1414234234532)) # 6자리까지 나옴
print('{:f}'.format(3.1414234234532))
print('%032.18f'% (32.141423434634234532)) # 18자리까지 나옴

print('%06.2f' %(3.141592653589793))
print('{:06.2f}'.format(3.141592653589793))
