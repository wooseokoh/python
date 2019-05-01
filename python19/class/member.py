class Member:
    id = ''
    pw = ''
    grade = ''
    mileage = ''
    
    # 생성자
    def __init__(self,id,pw,grade,mile):
        self.id = id
        self.pw = pw
        self.grade = grade
        self.mile = mile
        
list_total =[]
for index in range(0,3,1):
    list = []
    id = input("아이디를 입력하세요 :")
    pw = input("비밀번호를 입력하세요 :")
    grade = input("등급을 입력하세요 :")
    mile = input("마일리지를 입력하세요 :")
    list = [id,pw,grade,mile]
    list_total.append(list)
    print()
    
p1 = Member(list_total[0][0],list_total[0][1],list_total[0][2],list_total[0][3])
p2 = Member(list_total[1][0],list_total[1][1],list_total[1][2],list_total[1][3])
p3 = Member(list_total[2][0],list_total[2][1],list_total[2][2],list_total[2][3])

sum = int(p1.mile)+int(p2.mile)+int(p3.mile)

print("%s의 비밀번호는 %s입니다 " %(p1.id,p1.pw))
print("%s는 %s이고 마일리지는 %s입니다" %(p2.id, p2.pw, p2.mile))
print("총 마일리지는 %d입니다." %(sum))
print("평균 마일리지는 %d입니다." %(sum/3))

