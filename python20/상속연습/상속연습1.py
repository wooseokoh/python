class Person():
    name = ''
    age = 0
    
    def sleep(self):
        print('zzz')
    def eat(self):
        print('밥먹는중')
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class Man(Person):
    power_size = 0
    
    def __init__(self, name, age, power_size):
        Person.__init__(self, name, age)
        self.power_size = power_size
    
    def fast_run(self):
        print("달리는중")
    
m1 = Man('홍길동',10,1)
print(m1.name)
print(m1.age)
print(m1.power_size)

m1.sleep()
m1.eat()
m1.fast_run()
print(m1.fast_run())


