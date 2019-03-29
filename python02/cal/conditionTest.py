# 조건문
'''
data = 10;

if data > 100:
    print("조건이 맞습니다.");
else :
    print("조건이  틀렸습니다.");
'''    

'''
한 수를 입력 받는다.
이 수가 100보다 작으면 100보다 작은 숫자가 들어왔군요. 출력
프로그램이 끝났습니다. 출력    

data = int(input("숫자 :"));

if data < 100:
    print("100보다 작은 숫자가 들어왔군요.");
else :
    print("조건이  틀렸습니다.");

print("프로그램이 끝났습니다.");

'''

'''
두 수를 입력받는다.
더 큰 숫자를 찾는다.

data1 = int(input("숫자1 :"));
data2 = int(input("숫자2 :"));

if data1 < data2:
    print(data2,"이 더 크다");
else :
    print(data1,"이 더 크다");
'''
    
'''
하나의 예올 사원이 실적 목표를 달성하였을 경우에는 실적 목표를 초과한 금액의 10%를 성과급으로 받는 프로그램을 생성하라

goal = int(input("실적 :"));

if goal > 1000 :
    print("실적을 달생했습니다.", "당신의 보너스는",(goal-1000)*0.1);
else :
    print("다음 기회에");
'''
    
'''
아이디와 비밀번호가 맞는지 확인하시오

user = "root";
pw = "1234";

iUser = input("user: ");

if user == iUser :
    iPw = input("pw: ");
    if pw == iPw :
        print("아이디와 비밀번호가 맞습니다.");
    else:
        print("비밀번호가 틀렸습니다.");
else :
    print("아이디가 틀렸습니다.")
'''

'''
 키보드에서 입력받은 정수가 홀수인지 짝수인지를 말해주는 프로그램 작성
 
 t = int(input("숫자 : "));

if t % 2 == 0 :
    print(t," 짝수");
else:
    print(t," 홀수");                             
'''
          
'''
자장면 한 그릇은 4500원입니다
일행이 5명이상이면 주인이 2000원 할인해준다
우리가 낸 금액은 얼마일까요

crew = int(input("일행 : "));
mun = 4500;

if crew >= 5:
    print("자장면값 :",(mun * 5)-2000,"원");
else:
    print("자장면값 :",mun*5,"원");
'''
    
'''
교보문고에 가서 1000원짜리 스티커 3장과 2500원짜리 책갈피를 4개 샀습니다.
우수회원 할인으로 10% 할인을 받았습니다.
내가 낸 금액은 얼마일까요?

p1 = 1000;
p2 = 2500;

total = 0;

sticker = int(input("몇장 :"));
book = int(input("몇개 :"));

if (p1*sticker) + (p2*book) > 10000:
    total = (p1*sticker) + (p2*book) * 0.1;
    print(int(total));
else:
    total = (p1*sticker) + (p2*book);
    print(int(total));
    
'''
    
'''
자장면 4500
짬뽕 3500
자장면 금액
짬뽕금액
전체주문금액

black = 4500;
red = 3500;

b = int(input("그릇 :"));
r = int(input("그릇 :"));

tblack = black * b;
tred = red * r;
total = tblack + tred;

print("자장면의 가격은 ", tblack);
print("짬뽕의 가격은 ", tred);    
print("전체의 가격은 ", total);
'''

'''
다음과 같이 출력
오늘의 기온은? 20
오늘 나의 평가는? B
나의 신발 사이즈는? 250.2

오늘은 20도, 나의 평가는 B, 신발은 250.2

t = int(input("오늘의 기온은?"));
d = input("오늘 나의 평가는?");
s = float(input("나의 신발 사이즈는?"));    

print("오늘은",t,"나의평가는",d,"신발은",s);    
'''

'''
두 수를 입력받아 같은지 비교하고 아래와 같이 출력하시오

data1 = int(input("숫자1 :"));
data2 = int(input("숫자2 :"));

if data1 == data2:
    print("두수가 같습니다");
else :
    print("두수가 다릅니다");
'''

'''
receivemoney = int(input("받은돈: "));
total = int(input("상품의 총액: "));
tax = total * 0.1;
rest = receivemoney - total;

print("부가세:",int(tax));
print("잔돈:1",rest);
'''

'''
key_borad = int(input("키보드 가격: "));
key_cnt = int(input("키보드 갯수: "));
mouse = int(input("마우스 가격: "));
mouse_cnt = int(input("마우스 갯수: "));

key_total = key_borad*key_cnt;
mouse_total = mouse*mouse_cnt;
total = key_total+mouse_total;

print("키보드 총 가격: ",key_borad*key_cnt);
print("마우스 총 가격: ",mouse*mouse_cnt);
print("제품 총 가격: ",total);
'''

'''
name = input("당신의 이름은:");
age = input("당신의 나이는:");
div = input("당신의 소속은:");
'''






