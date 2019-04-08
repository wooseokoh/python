'''
1. 인원 총 커피값 계산, 인원당 * 커피값
2. 총 지불 금액, 인원당* 커피값이 15000원 초과시, 할인 2000원
'''

def coffeeSum(person,price):
    sum =  person * price
    return sum

def coffeeSale(sum):
    if sum >= 15000:
        print(sum - 2000)


if __name__ == '__main__':
    
    person = int(input("인원 :"))
    price = int(input("커피값 :"))
    
    sum = coffeeSum(person, price)
    
    coffeeSale(sum)
    
    
    
