import random

while True:
    
    user = int(input("가위 0, 바위1,보자기 2, 종료 3:"))
    
    if user == 3:
        print("게임을 종료합니다.")
        break
    
    com = random.randint(1,3)

    if user < com:
        user = user + 3

    result = user - com

    if result == 1:
        print("YOU WIN")
    elif result == 2:
        print("YOU LOSE")
    else:
        print("DRAW")

    print("COM",com)
    