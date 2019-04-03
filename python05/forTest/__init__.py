# 배열을 입력을 받아 sort를 사용하여 정리한 후 출력

# list1 = []
# list2 = []
# 
# value = 0
# 
# for i in range(0,3):
#     for j in range(0,4):
#         list1.append(value)
#         value += 1
#     list2.append(list1)
#     list1 = []
# 
# for i in range(0,3):
#     for j in range(0,4):
#         print(list2[i][j], end =" ")
#     print("")

def para_func(*para):
    result = 0
    for num in para:
        result = result + num
    return result
hap = 0

hap = para_func(10,20)
print("%d" % hap)
hap = para_func(10,20,30)
print("%d" % hap)
