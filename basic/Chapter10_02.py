# Chapter10_2
# Project1 실습
# Hangman(행맨) 미니 게임 제작(2)
# 프로그램 완성 및 최종 테스트

# csv 처리
import csv
# 랜덤
import random
# 사운드
import winsound
# 시간
import time

# 처음 인사
name = input('Enter Your Name : ')
print('Hi, ' + name, 'Time to play hangman game!')
print()
time.sleep(1)
print('Start, Loading...')
print()
time.sleep(0.5)

# csv 단어 리스트
words = []

# 문제 csv 파일 로드
with open('./resource/word_list.csv', 'r') as f:
    reader = csv.reader(f)
    # Header skip
    next(reader)
    for c in reader:
        words.append(c)

# print(words)

# 리스트 섞기
random.shuffle(words)

q = random.choice(words)

# 정답 단어
word = q[0].strip()  # .strip() 양쪽 공백 제거

# 추측 단어
guesses = ''

# 기회
turns = 10

# 핵심 while Loop
# 찬스 카운트가 남아있을경우
while turns > 0:
    # 실패 횟수
    failed = 0
    
    # 정답 단어 반복
    for x in word:
        # 정답 단어 내에 추측 문자가 포함되어 있는 경우
        if x in guesses:
            # 추측 단어 출력
            print(x, end=' ')
        else:
            # 틀린 경우 대시로 처리
            print('_', end=' ')
            failed += 1
    # 단어 추측이 성공 한 경우
    if failed == 0:
        print()
        print()
        # 성공 사운드
        winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME)
        print('Congratulation! The Gueeses is correct.')
        # while 구문 중단
        break
    print()

    # 추측 단어 문자 단위 입력
    print()
    print('Hint :', q[1].strip())  # print('Hint : {}'.format(q[1].strip())) 동일
    guess = input('guess a Character : ')

    # 단어 더하기
    guesses += guess

    # 정답 단어에 추측한 문자가 포함되어 있지 않으면
    if guess not in word:
        # 기회 횟수 감소
        turns -= 1
        print()
        # 오류 메시지
        print('Oops! Wrong')
        # 남은 기회 출력
        print('You have chance :', turns, 'more guesses!')

        if turns == 0:
            # 실패 사운드
            winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)
            # 실패 메시지
            print('You hangman game failed. Bye!')

















