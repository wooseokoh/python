class Person():
    name = ''
    age = 0
    
    def work(self):
        print('일하다')
    
    def talk(self):
        print('대화하다')
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class Man(Person):
    
    job = ''
    car = ''
    
    def event(self):
        print('회사가다')

    def __init__(self, name, age, job, car):
        Person.__init__(self, name, age)
        self.job = job
        self.car = car

class Betman(Man):
    
    money = 1000
    power = ''
    
    def event(self):
        print('악당을 물리치다')
        
    def __init__(self, name, age, job, car, money, power):
        Man.__init__(self, name, age, job, car)
        Person.__init__(self, name, age)
        self.money = money
        self.power = power

# print(Betman.money)
m1 = Man('홍길동', 30, '회사원', '트럭')
print(m1.job)
m1.event()
b1 = Betman('배트맨', 30, '재벌', '차', Betman.money, 100)
print(b1.name)
print(b1.money)
b1.event()