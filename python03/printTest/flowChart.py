'''
import datetime

now = datetime.datetime.now()
hour = now.hour
print(hour)

if hour <= 22:
    print("아직 집에 갈 시간이 멀었군요")

else:
    print("집에 갈 시각이군요")
'''
'''
1. 태어난 해를 입력
2. 나이를 계산(year이용)
3. 나이가 18살 이상이면 성년, 미만이면 미성년
4. 성년/미성년 판별 프로그램 종료합니다. 프린트

import datetime
import time

now = datetime.datetime.now()

year = int(input("태어난 해를 입력하세요. :"))

age = now.year - year + 1

if age >= 18: 
    gender = input("성별을 입력하세요 (남자,여자):")
    if gender == "남자":
        print(age,"남자 성년")
    else:
        print(age,"여자 성년")
else:
    print(age,"미성년입니다.")

print("성년/미성년 판별 프로그램을 종료합니다.")

'''
'''
당신의 점수를 입력하세요.

60점 이상이면 합격입니다.
60점미만, 40점 미만이면 과락불합격 아니면, 그냥 불합격

socre = int(input("점수를 입력하세요. :"))

if socre >= 60: 
    print("합격")
elif 40 <= socre < 60:
    print("과락불합격")
else:
    print("불합격")

print("프로그램을 종료합니다.")
'''
import random

target = random.randrange(1,2)

count = 0

while True:
    
    data = int(input("숫자를 입력하세요,종료는 0 :"))
    count += 1
    
    if data == 0:
        print("프로그램을 종료합니다.")
        break
    
    if target == data:
        print("정답입니다.")
        print(count)
        break
    
    else:
        print("숫자를 다시 입력하세요.")
        print("-----------------")
        
        if data > target:
            print("너무 크다")
        else:
            print("너무 작다")


















    
    
    
    