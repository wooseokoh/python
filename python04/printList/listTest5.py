
seat = [[0,0,0,0,0],[0,0,0,0,0]]
count = 0

while True:
    
    print("영화 예매 프로그램")
    print(" 0열    1열    2열    3열    4열")
    print("----------------------")
    for x in range(0,2):
        for y in range(0,5):
            print(seat[x][y], end = "    ")
        print()
    print("----------------------")    
    


    index = int(input("예매 행을 입력 :"))
    index1 = int(input("예매 열을 입력 (종료는 100):"))
    
    if index1 != 100:
        if seat[index - 1][index1 -1] == 1:
            print("이미 예매가 된 좌석입니다.")
            print("다른 좌석을 예매하세요")
        else:
            seat[index -1][index1 -1] = 1
            count += 1
            print(index,"행",index1,"열" "요청하신 자리에 예매되었습니다.")
    else:
        print("프로그램 종료")
        print(count * 10000,"만원")
        break
    