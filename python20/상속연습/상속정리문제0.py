class Person():
    name = ''
    p_num = ''
    number = ''
    depart = ''
    age = 0
    
    def work(self):
        print('일하다')
    def talk(self):
        print('대화하다')
    def __init__(self, name, p_num, number, depart, age):
        self.name = name
        self.p_num = p_num
        self.number = number
        self.depart = depart
        self.age = age
        
class Manager(Person):
    department = ''
    def event(self):
        print('관리감독하다')
    
    def __init__(self, name, p_num, number, depart, age, department):
        Person.__init__(self, name, p_num, number, depart, age)
        self.department = department

m1 = Manager('A','123','010-1234-123','인사부', 30, '인사')
print('이름은' + m1.name + '입니다')
print('나이는' + str(m1.age) + '입니다')
m1.talk()
m1.event()

m2 = Manager('B','456','010-5678-5678','총무부', 30, '회계')
print('이름은' + m2.name + '입니다')
print('나이는' + str(m2.age) + '입니다')
m2.talk()
m2.event()
 



