class Day:
    
    working = ''
    time = ''
    place = ''
    
    # 생성자
    def __init__(self,working,time,place):
        self.working = working
        self.time = time
        self.place = place

    # 맴버 메소드
    def __str__(self):
        return self.working + ', ' + str(self.time) + ', ' + self.place

one = Day("자바공부", 10, "강남")
print(one)
two = Day("여행", 15, "강원도")
print(two)
three = Day("운동", 11, "피트니스")
print(three)

sum = one.time + two.time + three.time

print("전체 하는 일의 시간은 :", sum)
print("평균 하는 일의 시간은 :", int(sum/3))
print("매일 무엇을 얼마나 어디에서 했는지 프린트 :",(one.working,one.place))
print("매일 무엇을 얼마나 어디에서 했는지 프린트 :",(two.working,two.place))
print("매일 무엇을 얼마나 어디에서 했는지 프린트 :",(three.working,three.place))
print("며칠 간 했는지 :",sum/24)
