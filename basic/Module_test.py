# 모듈 사용 실습

import sys

print(sys)
print(type(sys))
print(sys.path)
print(type(sys.path))

# 모듈 경로 삽입
# sys.path.append('C:\\Python\\PyStudy\\math')  # 영구적 사용은 환경변수 추가

# print(sys.path)

# import test_module

# 모듈 사용
# print(test_module.power(10, 3))

import Chapter06_02
print(Chapter06_02.add(10, 100000))
