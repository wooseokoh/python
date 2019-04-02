'''
여러개의 값을 저장, 하나의 이름을 사용

num = [10,45,87,23,86,94]

'''
num = [10,45,87,23,86,94]

print(num[0])
print(num[1])
print(num[2])
print(len(num),"개")


num[2] = 66

print(num[2])

for i in range(0,len(num)):
    print(i, ":",num[i])

