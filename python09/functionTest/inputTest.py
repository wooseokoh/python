
def cal(x,y,z):
    
    if y == "+":
        r = x + z
        print("두 수의 합은",r)
        return r
    elif y == "-":
        r = x - z
        print("두 수의 차는",r)
        return r
    elif y == "*":
        r = x * z
        print("두 수의 곱은",r)
        return 
    elif y == "**":
        r = x ** z
        print("두 수의  제곱은",r)
        return 
    elif y == "/":
        r = x / z
        print("두 수의  나누기는",r)
        return 
    
if __name__ == '__main__':
    
    print("계산기 시작")
    x = int(input("숫자 :"))
    y = input("연산자를 입력하세요 :")
    z = int(input("숫자 :"))


    cal(x,y,z)







    