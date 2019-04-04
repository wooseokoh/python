# singer = {1: "송아무개",2: "김아무개",3: "박아무개"}
# 
# print(singer)
# 
# print(singer[1])
# print(singer[2])
# print(singer[3])
# 
# print()

# data2 = {"name": "송아무개", "age":100, "소속": "kg"}
# 
# print(data2)
# 
# print(data2["name"])
# print(data2["age"])
# print(data2["소속"])
# 
# print(data2.keys())
# print(data2.values())
# print(data2.items())
# 
# print()
# data2["소속"] = "구로점"
# print(data2)

# 1)
# singer라는 빈 딕셔너리를 만들고,
# 가수이름, 인원수, 대표곡, 소속사 입력
# 모든 항목(item 키+값) 프린트
#
# 2) 깊은 복사, 얕은 복사

# singer = {}
# 
# singer["가수이름"] = "트와이스"
# singer["인원수"] = 9
# singer["대표곡"] = "SIGNAL"
# singer["소속사"] = "jyp"
# 
# print(singer)
# print(singer.items())
# 
# artist = {}
# artist = singer
# print(artist)
# 
# print("얕은복사")
# singer["대표곡"] = "summer"
# print(singer)
# print(artist)
# 
# print("깊은복사")
# singer2 = singer.copy()
# singer["대표곡"] = "spring"
# print(singer)
# print(singer2)

# data1 = ["감자", "고구마", "양파"]
#  
# for i in range(0,3,1): # 0,1,2 총 3번 돌아감
#     print(data1[i])
#  
# for j in data1:
#     print(j)
# 
# data2 = "나는 파이썬 프로그래머"
# 
# for z in data2:
#     print(z)

singer = {1: "송아무개",2: "김아무개",3: "박아무개"}
data3 = singer.keys()
    
print(data3)

for l in data3:
    print(singer[l])
    
for k in singer.keys():
    print(singer[k])

print(1 in singer)
print("나" in data3)
print("감자" in singer)





