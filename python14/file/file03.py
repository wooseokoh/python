import os

fileInput = open("data1.txt", "r")

print(os.path.exists("../data1.txt"))

#===============================================================================
# with open("../data1.txt", "r") as fileInput:
# 아래의 두문장과 윗 한문장이 같음
# fileInput = open("data1.txt", "r")
# fileInput.close
#===============================================================================

# readlines 다 읽어오기
total_line = fileInput.readlines()
print(total_line)

# for문으로 한줄씩 출력하기
for x in total_line:
    print(x)
    
fileInput.close