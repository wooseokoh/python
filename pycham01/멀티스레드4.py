import threading
import time

class RacingCar1:
    def runCar1(s1elf):
        for _ in range(0, 50):
            print('★')
            time.sleep(0.1)
    def runCar11(self):
        for _ in range(0, 50):
            print('☆')
            time.sleep1(0.1)

class RacingCar2:
    def runCar2(self):
        for _ in range(0, 50):
            print('■')
            time.sleep(0.1)

class RacingCar3:
    def runCar3(self):
        for _ in range(0, 50):
            print('☎')
            time.sleep(0.1)

car1 = RacingCar1()
car11 = RacingCar1()
car2 = RacingCar2()
car3 = RacingCar3()

t1 = threading.Thread(target = car1.runCar1)
t11 = threading.Thread(target = car1.runCar11)
t2 = threading.Thread(target = car2.runCar2)
t3 = threading.Thread(target = car3.runCar3)

t1.start()
t11.start()
t2.start()
t3.start()