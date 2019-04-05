
data = input("문자열을 입력하세요 :")
# North Atlantic Treaty Organization
trdata = data.title()
num = trdata.split()

data2 = []

for x in num:
    data2.append(x[0])
    
for y in data2:
    print(y, end = "")
