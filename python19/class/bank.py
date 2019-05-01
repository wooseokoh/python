class Bank:
    
    product = ''
    name = ''
    money = ''
    
    # 생성자
    def __init__(self,product,name,money):
        self.product = product
        self.name = name
        self.money = money
        
b1 = Bank("청약저축", "김아무개", "500")
b2 = Bank("내비상금", "김아무개딸", "30")
b3 = Bank("자유적금", "박아무개", "100")

total = int(b1.money) + int(b2.money) + int(b3.money)

print("%s 통장에는 %s만원이 들어있어요" % (b2.product , b2.money))
print("%s 통장에는 %s만원이 들어있어요" %(b3.name,b3.money))
print("우리 집 전체 예금액은  %d만원이에요" %(total))

