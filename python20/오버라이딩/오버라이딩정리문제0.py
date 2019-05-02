class Student():
    age = ''
    school = ''
    
    def study(self):
        print('공부하다')
    def play(self):
        print('놀다')
    def __init__(self,age,school):
        self.age = age
        self.school = school
        
class Ele_school(Student):
    school = '초등학교'
    def study(self):
        print('영어을 공부하다')
class Mid_school(Student):
    school = '중학교'
    def study(self):
        print('사회를 공부하다')    
class High_school(Student):
    school = '고등학교'
    def study(self):
        print('정적분을 공부하다')

s1 = Student(5,'유치원')
print(s1.school)
s1.study()
s1 = Ele_school(10,Ele_school.school)
print(s1.school)
s1.study()
s1 = Mid_school(15,Mid_school.school)
print(s1.school)
s1.study()
s1 = High_school(17,High_school.school)
print(s1.school)
s1.study()