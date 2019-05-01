#===============================================================================
# 휴대폰
# 정적특성 - 색,회사
# 동적특성 - 인터넷검색하다, 사진을찍다.
#===============================================================================

class CellPhone:
    
    color = '';
    company = '';
    
    def search(self):
        print('인터넷 검색')
    def picture(self):
        print('사진을 찍다')
    def __str__(self): # __ <-- 내장함수
        return self.color +" "+self.company
    
p1 = CellPhone()
p1.color = '빨강'
p1.company = 'sk'

p2 = CellPhone()
p2.color = '파랑'
p2.company = 'kt'

p3 = CellPhone()
p3.color = '노랑'
p3.company = 'lg'

# 메모리 3 * 3 = 9 (맴버변수+객체)*3

p1.picture()
p2.search()
p3.picture()

print(p1)

