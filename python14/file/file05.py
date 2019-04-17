# 파일쓰기
fileOutput = open("data5.txt", "w")

fileOutput.write("나는 새로운 내용입니다.\n")
fileOutput.write("나는 새로운 내용입니다.\n")
fileOutput.write("나는 추가된 내용입니다.\n")
fileOutput.close()

# 파일읽기
fileInput = open("data5.txt", "r")

total_line = fileInput.readlines()
print(total_line)

fileInput.close()
