'''
1. 더하기  2. 빼기  3. 곱하기  4. 나누기

'''

def addNum(x,y):
    z = x + y
    print("두 수의 합은",z)
def minusNum(x,y):
    z = x - y
    print("두 수의 합은",z)
def mulNum(x,y):
    z = x * y
    print("두 수의 합은",z)
def divNum(x,y):
    z = x / y
    print("두 수의 합은",z)

if __name__ == '__main__':
    print("계산기 시작")
    x = int(input("숫자 :"))
    y = int(input("숫자 :"))
    
    
    addNum(x, y)
    minusNum(x, y)
    mulNum(x, y)
    divNum(x, y)
    
    
    
    