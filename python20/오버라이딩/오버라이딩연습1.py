class Shape:
    
    name = 'ok'
    
    def fun1(self): # 일반메소드
        print('함수1 호출되다.')
        
    def fun2(self): # 추상메소드
        pass
    
s1 = Shape()
s1.fun1()
s1.fun2()
