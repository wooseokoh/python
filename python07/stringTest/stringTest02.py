count_blank = 0
count_alpha = 0
count_num = 0
count_t = 0

data = input("문자열을 입력하세요 :")

for x in data:
    if x.isspace():
        count_blank += 1
    elif x.isalpha():
        count_alpha += 1
    elif x.isdigit():
        count_num += 1
    else:
        count_t += 1

print("공백은 :", count_blank)
print("문자는 :", count_alpha)
print("숫자는 :", count_num)
print("--------------------------")

data = input("문자열을 입력하세요 :")

count = [0,0,0,0]

for x in data:
    if x.isspace():
        count[0] += 1
    elif x.isalpha():
        count[1] += 1
    elif x.isdigit():
        count[2] += 1
    else:
        count[3] += 1

print("공백은 :", count[0])
print("문자는 :", count[1])
print("숫자는 :", count[2])
print("--------------------------")

data = input("문자열을 입력하세요 :")

count = {"blank" : 0, "alpha" : 0, "num" : 0, "나머지" : 0}

for x in data:
    if x.isspace():
        count["blank"] += 1
    elif x.isalpha():
        count["alpha"] += 1
    elif x.isdigit():
        count["num"] += 1
    else:
        count["나머지"] += 1

print(count)








