class Bouns:
    
    data = 10000
    name = None
    age = None
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Bouns.data = Bouns.data - 1000
        
    def play(self):
        print("놀다")
    
    def tv(self):
        print('tv를본다')
    
    def __str__(self):
        return self.name + ' ' + str(self.age)
    
p1 = Bouns('김민지',10) 
p2 = Bouns('김지영',12) 


print(p1)
p1.play()

print(p2)
p2.tv()
print(Bouns.data)

