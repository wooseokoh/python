class Dog:
    #맴버 변수
    color = '';
    field = '';
    
    #생성자
    def __init__(self, color, field):
        self.color = color
        self.field = field
        
    #맴버 메소드
    def jump(self):
        print('뛰고있다')
    
    def sleep(self):
        print('자다')
    
    def __str__(self):
        return self.color + ', ' + self.field
    
# 인스턴스를 생성할때 매개변수의 수는 생성자의 매개변수 수와 일치시킨다.(self 제외)
dog1 = Dog('갈색','푸들')
print(dog1)
dog2 = Dog('흰색','진돗개')
print(dog2)
