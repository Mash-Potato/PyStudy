# Chapter03_1
# 파이썬 문자형(중요)

# 문자열 생성
str1 = "i am python"
str2 = 'Python'
str3 = """How Are You?"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))

# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

# 이스케이프 문자
# I'm Boy
print("I'm Boy") # ">' 일경우 에러
print('I\'m Boy') # 역 슬래쉬(\) 사용
print('I\\m Boy') # 역 슬래쉬(\) 사용

print('a \t b') # tab만큼 간격
print('a \n b')
print('a \"\" b')
print()

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)

# 탭, 줄 바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"
print(t_s1)
print(t_s2)

# Raw String 출력
raw_s = r'D:\python\test'
print(raw_s)
print()

# 멀티 라인 입력
# 역슬래시 사용
multi_str =\
"""
문자열
멀티라인 입력
테스트
"""
multi_str2 ="asdfasdf" \
            "asdfjkbwejrfkff" \
            "ffffffffff"
print(multi_str)
print(multi_str2)
print()

# 문자열 연산
str_o1 = 'python'
str_o2 = 'Apple!'
str_o3 = 'How Are You Doing?'
str_o4 = 'Seoul Daejeon Busan Jinju'

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1) # 시퀀스는 in 사용가능(str은 시퀀스) y문자가 str_o1 에 있으면 bool 리턴
print('Y' in str_o1) # 대소문자 구분
print('P' not in str_o2)

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1), type(str(10.1)))
print(str(True), type(str(True)))
print()

# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha...)
print("Capitalize: ", str_o1.capitalize())
print("endswith?: ", str_o2.endswith('!')) # bool
print("replace", str_o1.replace("thon", "Good"))
print("sorted: ", sorted(str_o1))
print("split: ", str_o4.split(' '))

# 반복(시퀀스)
im_str = "Good Boy!"
print(dir(im_str)) # __iter__

# 출력
for i in im_str:
    print(i)

# 슬라이싱
str_s1 = "Nice Python"

print(len(str_s1))
print()

# 슬라이싱 연습
print(str_s1[0:3]) # 3-1까지 출력 0, 1, 2
print(str_s1[5:11])
print(str_s1[5:])
print(str_s1[:len(str_s1)]) # ==str_s1[:11]
print(str_s1[:len(str_s1)-1]) # ==str_s1[:10]
print(str_s1[1:9:2]) # 3번째 인수는 단위
print(str_s1[-5:])  # 음수는 오른쪽에서 왼쪽 -1부터 시작
print(str_s1[1:-2])
print(str_s1[::2])
print(str_s1[::-1])

# 아스키 코드(또는 유니코드)
a= 'A'
print(ord(a))
print(ord('z')) # 아스키 코드로
print(chr(65))
print(chr(122)) # 문자로






