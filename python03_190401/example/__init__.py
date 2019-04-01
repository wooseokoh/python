stock = [2,5,5,5,5]

x = int(input("입력하세요"))

while True:
    if x == 1:
        print("갯수",stock[0])
        if stock[0] == 0:
            print("Sold out")
            break
        else:
            stock[0] -= 1
            print("갯수",stock[0])
    