# ★★★★★★★★★★★★
# for y in range(0,3):
#     for i in range(0,10,1):
#         print("★", end = "")
#     print()


# aa = [[1,2,3,4],[5,6],[7,8,9]]
# 
# print(len(aa))
# print(len(aa[0]))
# print(len(aa[1]))
# print(len(aa[2]))


index = int(input("층수를 입력하세요 :"))

for y in range(0,index+1):
    for i in range(0,y,1):
        print("★",end = "")
    print()

for x in range(0,10,1):
    print("★"* x)

x = 0
while x < 10:
    print("★"* x)
    x += 1
