fileInput = open("data1.txt", "r")

while True:
    line = fileInput.readline()
    if line == "":
        break
    print(line)
    
fileInput.close