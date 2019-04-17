import os

file_name = input("읽어오기를 희망하는 파일이름을 입력하세요....>>")

file = "D:/temp/" + file_name+".txt"

print(os.path.exists(file))

if os.path.exists(file):
    fileInput = open(file, "r")

    total_line = fileInput.readlines()
    print(total_line)

    for x in total_line:
        print(x)
    
        fileInput.close
else:
    print("해당 파일이 없습니다. 다시 확인해주세요.")