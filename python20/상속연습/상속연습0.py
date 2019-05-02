# 부모클래스
class Car():
    color = ''
    speed = 0
    def speed_up(self):
        print('속도를 UP')
        
    def speed_down(self):
        print('속도를 Down')
    
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed
        
# 자식클래스
# car의 부품을 재사용함
class Truck(Car): 
    적재량 = 0
    def 적재량알아보기(self):
        return self.적재량
    def __init__(self, color, speed, 적재량):
        self.color = color
        self.speed = speed
        self.적재량 = 적재량

truck1 = Truck('검정', 100, 10)
print(truck1.color) # car
print(truck1.speed) # car
print(truck1.적재량) # truck
truck1.speed_up()
truck1.speed_down()
print(truck1.적재량알아보기())
print("------------------")

truck2 = Truck('회색', 70, 50)
print(truck2.color) # car
print(truck2.speed) # car
print(truck2.적재량) # truck