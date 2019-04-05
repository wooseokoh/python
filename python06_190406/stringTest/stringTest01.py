#9

hero = []

for i in range(0,3):
    data = input("영웅을 입력하세요 :")
    hero.append(data)
    if "배트맨" in hero:
        print("박쥐인간입니다.")
    elif "슈퍼맨" in hero:
        print("하늘을 나는군요.")
    elif "아이언맨" in hero:
        print("철의인간입니다.")

#10

hero = []
count_s = 0
count_b = 0
count_i = 0
for i in range(0,6):
    data = input("영웅을 입력하세요 :")
    hero.append(data)
for j in range(0,len(hero)):
    if hero[j] == "배트맨" :
        count_b += 1
    elif hero[j] == "슈퍼맨":
        count_s += 1       
    elif hero[j] == "아이언맨":
        count_i += 1
        
print("박쥐인간은 ",count_b,"명")
print("하늘인간은 ",count_s,"명")
print("철인간은 ",count_i,"명")

#11

friend = []

while True:
    print("1.친구리스트 출력")
    print("2.친구추가")
    print("3.친구삭제")
    print("4.이름변경")
    print("9.종료")
    menu = int(input("메뉴를 선택하세요 :"))
    if menu == 1:
        print(friend)
        continue
    elif menu == 2:
        friend.append(input("추가할 친구이름을 입력하세요 :"))
        print(friend)
        continue
    elif menu == 3:
        friend.remove(input("삭제할 친구이름을 입력하세요 :"))
        print(friend)
        continue
    elif menu == 4:
        bchange = input("변경해야 친구이름을 입력하세요 :")
        for i in range(len(friend)):
            if friend[i] == bchange:
                friend[i] = input("변경할 친구이름을 입력하세요 :")
        print(friend)
        continue
    elif menu == 9:
        print("프로그램을 종료합니다.")
        break
print("----------------------")

hero = []

for i in range(0,3):
    data = input("영웅을 입력하세요 :")
    hero.append(data)
    if "배트맨" in hero:
        print("박쥐인간입니다.")
    elif "슈퍼맨" in hero:
        print("하늘을 나는군요.")
    elif "아이언맨" in hero:
        print("철의인간입니다.")

#12
dog = []

while True:
    
    data = input("강아지이름을 입력하세요.(종료시에는 엔터키) :")
    dog.append(data)
    
    if data == "":
        print(dog)
        break