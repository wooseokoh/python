class Person:
    name = None
    gender = None
    age = None
    
    count = 0
    ageSum = 0
    
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age
        
        Person.count = Person.count + 1
        Person.ageSum += self.age
    
    def work(self):
        print("일한다")
        
    def char(self):
        print("친화력 있다")

    def __str__(self):
        return self.name + ' ' + self.gender + ' ' + str(self.age)
     
p1 = Person('홍길동','남',30)

print(p1)
p1.work()
print(Person.count,'명')

p2 = Person('철수','남',40)

print(p2)
p2.work()
print(Person.count,'명')

p3 = Person('수박','남',50)

print(p3)
p3.work()
print(Person.count,'명')

print(int(Person.ageSum/3),'살')




