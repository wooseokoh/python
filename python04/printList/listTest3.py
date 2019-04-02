# name = [] #비어있는 리스트
# 
# print(name)
# name.append("김아무개")
# name.append("박아무개")
# print(name)
# 
# data = input("이름을 입력")
# name.append(data)
# print(name) 컨 + /

# name2 = []
# 
# for i in range(0,13):
#     data2 = input("이름을 입력하세요 :")
#     name2.append(data2)
# 
# print(name2)

list = [1,5,8,2,3,9,7]
print(list)

list.append(4)
print(list)
print(list.pop())
print(list)
print(list.sort())
print(list)
print(list.reverse())
print(list)
print(list.index(8))
print(list)
list.remove(1)
print(list)
list.extend([6,1,4])
print(list)

list2 = [10,12,11]
list.extend(list2)
print(list)

list3 = sorted(list2)
print(list2)
print(list3)



min = list3[0]
max_index = len(list3)-1
max = list3[max_index]

print("최소값 :", min)
print("최대값 :", max)


print("최소값의 위치:", list2.index(min))
print("최대값의 위치:", list2.index(max))

print(list2)
list2.insert(0, 4)
print(list2)

print(list2.count(4))

list3.clear()
print(list3)

print(list2)
print(list2.remove(4))
print(list2)

print(len(list2))

print("--------------------------------")
list4 = [1,2,3]
list5 = [4,5,6]

print(list4.extend([7,8,9]))
print(list4)
print(list4.extend(list5))
print(list4)

# list copy

list6= []
list6 = list4

print(list4)
print(list6)
print("-------------- 얕은복사  -------------------")
list[0] = 0
print(list4)
print(list6)

print("----------------깊은복사-------------------")

list7 = []
list7 = list4.copy()
print(list4)

print(list7)
print(list6)



























