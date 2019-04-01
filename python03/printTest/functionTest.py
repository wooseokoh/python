
'''
입력을 받아서 두 수를 곱한 후, 곱한수가 10000원이 넘으면 2000원 할인
'''

'''
def inputFunc():
    person = int(input("인원 :"))
    price = int(input("가격 :"))
    return person * price
                
# print("총합은 :", inputFunc())


def process(x):
    if x >= 10000 :
        y = x - 2000
    else:
        y = x
    return y

result = inputFunc()

print("두수를 곱한값", result)

total = process(result)

print("두수를 곱한값", total)
'''

'''
입력받는 함수 정의 
    좋아하는 색은 (빨강 :1 노랑 :2 파랑 :3)
입력받은 값을 반환받아,
    1이면 파이썬 스터디반
    2이면 장고 스터디반
    3이면 웹구축 스터디반
'''
'''
def color():
    choice = input("좋아하는 색을 입력하세요 (빨강,노랑,파랑) :")

    if choice == "빨강":
        x = 1
    elif choice == "노랑":
        x = 2
    else:
        choice == "파랑"
        x = 3 
    return x 

def study(x):
    if x ==  1:
        print("파이썬 스터디반")
    elif x == 2:
        print("장고 스터디반")
    else:
        x == 3
        print("웹구축 스터디반") 
    return x 
    
print(study())
'''





