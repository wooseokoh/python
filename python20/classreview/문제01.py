class Girl:
    name = ''
    age = 0
    money = 10000
    
    def __init__(self,name,age):
        self.name = name # 인스턴스 변수 (이름과 나이가 다르기 때문에)
        self.age = age # 인스턴스 변수
        Girl.money -= 1000 # 클래스 변수 (지갑은 하나) = 정적인 클래스 변수
    
    def play(self):
        print('매일 놀아요')
    def watch(self):
        print('티비를 봐요')
        
girl1 = Girl('A',10)
print(Girl.money)
girl2 = Girl('B',12)
print(Girl.money)

print(girl1.name)
print(girl2.name)

girl1.play()
print(girl1.play())




