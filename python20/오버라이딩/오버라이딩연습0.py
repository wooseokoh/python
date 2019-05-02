class Bank():

    def inter(self):
        return 0

class Bad_bank(Bank):
    
    def inter(self):
        return 0.1
        
class Normal_bank(Bank):
    
    def inter(self):
        return 0.05

class Good_bank(Bank):
    
    def inter(self):
        return 0.02
    
b1 = Bank()
print(b1.inter())

b1 = Bad_bank()
print(b1.inter())

b1 = Normal_bank()
print(b1.inter())

b1 = Good_bank()
print(b1.inter())