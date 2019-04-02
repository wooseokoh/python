# 
# seat = [0] * 10
# 
# print(seat)
# 
# seat[0] = 1
# 
# print(seat)
# 
# index = int(input("예매좌석 번호 입력 (종료:0)>>>> "))
# 
# seat[index - 1] = 1    
# 
# print(seat)

seat2 = [0] * 10

while True:
     
    print("-------극장 예매 시스템--------")
 
    for i in range(0,10):
        print( i+1 , end =" ")
    print()
    print("--------------------------")
 
    for i in range(0,10):
        print(seat2[i], end =" ")
    print("\n--------------------------")
     
    
    index = int(input("예매좌석 번호 입력 (종료:0)>>>> "))
    
    
    if index == 0:
        print("예매 시스템을 종료합니다.")
        break
    if seat2[index - 1] == 1:
        print("예매가 된 좌석입니다.")
        print("다른 좌석을 선택하세요")
    else:
        print(index,"번호의 좌석을 예매합니다.")
        seat2[index -1] = 1
        print(index, "번호의 좌석이 예매되었습니다.")
        
    


        












