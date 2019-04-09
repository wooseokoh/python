
x = 300

def call():
    
    x = 200
    print("함수 내의  x 값 (지역변수):", x)
    
    y = 300
    print("함수 내의  y 값 (지역변수):", y)
    
def call2():
    
    x = 20
    print(x)
    
if __name__ == '__main__':
    print("함수 밖의  x 값 :", x)
    call2()
    call()
    # print(y) (지역변수) 접근 불가