money = int(input("돈을 넣어주세요 :"))

if money == 0:
    print("종료")
    
stock = [5,5,5,5,5]

while True:

    if money == 0 or money < 1000:
        print("다음에 또 이용해 주세요")
        break

    set = int(input("메뉴를 고르세요 :"))

    if set == 0:
        print("프로그램을 종료합니다.")
        break
    
    elif set == 1:
        if stock[0] == 0:
            print("Sold out, 다른메뉴를 골라주세요")
        else:
            stock[0] -= 1
            cola = 1000
            money = money - cola
            print("코카콜라는 %d입니다. 잔돈은 %d입니다." % (cola, money))
            print("남은재고는 %d개입니다."% stock[0])
            
    elif set == 2:
        if stock[1] == 0:
            print("Sold out, 다른메뉴를 골라주세요")
        else:
            if money < 1500:
                print("돈이 모자라네요")
            else:
                stock[1] -= 1
                poka = 1500
                money = money - poka
                print("포카리는 %d입니다. 잔돈은 %d입니다." % (poka, money))
                print("남은재고는 %d개입니다."% stock[1])
            
    elif set == 3:
        if stock[2] == 0:
            print("Sold out, 다른메뉴를 골라주세요")
        else:
            if money < 1300:
                print("돈이 모자라네요")
            else:
                stock[2] -= 1
                sprite = 1300
                money = money - sprite
                print("스프라이트는 %d입니다. 잔돈은 %d입니다." % (sprite, money))
                print("남은재고는 %d개입니다."% stock[2])
            
    elif set == 4:
        if stock[3] == 0:
            print("Sold out, 다른메뉴를 골라주세요")
        else:
            if money < 1200:
                print("돈이 모자라네요")
            else:
                stock[3] -= 1
                rice = 1200
                money = money - rice 
                print("식혜는 %d입니다. 잔돈은 %d입니다." % (rice, money))
                print("남은재고는 %d개입니다."% stock[3])
        
    elif set == 5:
        if stock[4] == 0:
            print("Sold out, 다른메뉴를 골라주세요")
        else:
            if money < 1100:
                print("돈이 모자라네요")
            else:
                stock[4] -= 1
                orange = 1100
                money = money - orange
                print("쌕쌕는 %d입니다. 잔돈은 %d입니다." % (orange, money))
                print("남은재고는 %d개입니다."% stock[4])
    else:
        print("다시입력해주세요.")
