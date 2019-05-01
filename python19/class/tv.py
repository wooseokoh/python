class Tv:
    color ='';
    size = 0;
    count = 0;
    
    # 파라매터 없는 생성자는 기본 생성자
    
    # 파라매터 있는 생성자
    def __init__(self,color,size):
        self.color = color
        self.size = size
        Tv.count = Tv.count + 1
        # 클래스당 하나만 가지고, 생성된 객체간 공유
        # 가능한 클래스변수(static)
        
    def changeCh(self,ch):
        print(ch + "번 채널로 변경하다.")
        
    def powerOff(self):
        print("Tv를 끄다.")
        
    def __str__(self):
        return self.color + ' ' + str(self.size)
    
myTv = Tv('빨강', 50)
print(Tv.count)
yourTv = Tv('파랑', 100)
print(Tv.count)

print(myTv)
print(yourTv)