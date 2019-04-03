# seat  = [[1,2,3],[4,5,6]]
# 
# print(len(seat), end =" ") # end =" " 옆으로 출력
# print(len(seat[0]), end =" ")
# print(len(seat[1]), end =" ")
# 
# print("\n------------------------------")
# 
# seat2 = [[1,2,3,4],[5,6],[7,8,9]]
# 
# print(len(seat2[0]), end =" ")
# print(len(seat2[1]), end =" ")
# print(len(seat2[2]), end =" ")
# print()
# 
# for i in range(0,3):
#     print(len(seat2[i]), end =" ")



def choice():
    
    row = int(input("예매 행을 입력 :"))
    col = int(input("예매 열을 입력 :"))
    
    if seat2[row - 1][col -1] == 1:
        print("이미 예매가 된 좌석입니다.")
        print("다른 좌석을 예매하세요")
    elif seat2[row - 1][col -1] == " ":
        print("없는좌석 입니다.")
        print("다른 좌석을 예매하세요")
    else:
        seat2[row -1][col -1] = 1
        print(row,"행",col,"열" "요청하신 자리에 예매되었습니다.")

    
seat2 = [[0,0,0,0,0,0,0,0],[0,0," "," "," "," ",0,0],[0,0,0," "," ",0,0,0]]

while True:
    
    print("------영화예매 프로그램입니다.-----")
    
    print("     ", end =" ")
    
    for i in range(1,9):
        print("", i, end = " ")
    print("\n------------------------------")    
    
    for x in range(0,len(seat2)): # 행을 출력해주는 반복
        print(x+1,"행 : ", end = " ")
        for y in range(0,len(seat2[x])): # 열을 출력해주는 반복
            print(seat2[x][y], end = "  ")
        print()
        
    choice()
    away = int(input("종료 : 0 , 진행 : 1 : "))
    if away == 0:
        print("프로그램을 종료합니다.")    
        break
    else:
        continue

             
             
             
            
            
            