import threading
import time

class Multi:
    sp = ''
    def __init__(self,sp):
        self.sp = sp
    def show(self):
        for _ in range(0,50):
            sp = self.sp
            print(sp, end= '')
car1 = Multi('☆')
car2 = Multi('□')
car3 = Multi('☏')
th1 = threading.Thread(target= car1.show) # 입력값은 딕셔너리
th2 = threading.Thread(target= car2.show)
th3 = threading.Thread(target= car3.show)
th1.start()
print()
th2.start()
print()
th3.start()