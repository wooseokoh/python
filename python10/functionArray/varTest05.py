import os
import calendar

if __name__ == '__main__':
    
    cal = calendar.month(2019,4)
    print(cal)
    
    print(os.getcwd()) # 이 파일의 현재 위치 찾아주는 명령어
    
    os.chdir("c:") # c로 위치를 변경

    print(os.getcwd()) # 이 파일의 현재 위치 찾아주는 명령어
    
    print(os.listdir(".")) # 위치에 있는 파일을 . 으로 구분
    
    
