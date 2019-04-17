fileInput = open("data1.txt", "r")

# readline() 한줄 읽어오기
line = fileInput.readline()
print(line)
line = fileInput.readline()
print(line)
line = fileInput.readline()
print(line)

fileInput.close()