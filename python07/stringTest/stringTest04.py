#1
while True:
    data3 = int(input("종료 : 0, 진행 : 1 :"))
    if data3 == 0:
        break
    if data3 == 1:
        data1 = int(input("첫번째 숫자를 입력하세요 :"))
        data2 = int(input("두번쨰 숫자를 입력하세요 :"))
        if data1 == data2:
            print("Same")
        elif data1 < data2:
            print("두번째숫자가 더크다")
        else:
            print("첫번째숫자가 더크다")
            
#2   
while True:
    data = int(input("종료 : 0, 진행 : 1 :"))
    if data == 0:
        break
    if data == 1:
        data1 = int(input("숫자를 입력하세요 :"))
        if data1 % 2 == 1:
            print("홀수")
        else:
            print("짝수")
            
#3
while True:
    data3 = int(input("종료 : 0, 진행 : 1 :"))
    if data3 == 0:
        break
    if data3 == 1:
        month = int(input("몇월입니까? :"))

        if 3 <= month <= 5:
            print("봄")
        elif 6 <= month <= 8:
            print("여름")
        elif 9 <= month <= 11:
            print("가을")
        elif month == 1 or month == 2 or month == 12:
            print("겨울")
        else:
            print("다시입력해주세요")
            continue  
        
#4
data_list = []
 
for x in range(0,6):
    data = int(input("숫자입력 :"))
    data_list.append(data)
print(data_list)

max = data_list[0]

for y in range(0,6):
    if max < data_list[y]:
        max = data_list[y]
print(max)

#5
while True:
    data = int(input("종료 : 0, 진행 : 1 :"))
    if data == 0:
        break
    if data == 1:
        num1 = int(input("첫번째 숫자를 입력하세요 :"))
        cal = input("연산기호를 입력하세요 :")
        num2 = int(input("두번째 숫자를 입력하세요 :"))  
        if cal == "+":
            result = num1 + num2
            print(num1 + num2)
        elif cal == "-":
            result = num1 - num2
            print(result)
        elif cal == "*":
            result = num1 * num2
            print(result)   
        elif cal == "/":
            result = num1 / num2
            print(result)
        else:
            print("다시 입력해주세요")

#6
data1 = int(input("첫번째 숫자를 입력하세요 :"))
data2 = int(input("두번쨰 숫자를 입력하세요 :"))
sum = 0
for x in range(data1,data2+1):
    sum += x
print(sum)

#7
person = ["김아무개","송아무개","정아무개","이아무개"]
score = [100,85,90,70]
result = 0

print("전체학생수 :", len(person),"명")
print("--------------------------")
for x in range(0,4):
    print(person[x],":",score[x])
print("--------------------------")

for y in score:
    result += y
print("평균 :",result/len(person),"점")

#8
data = {"김아무개" : 100,"송아무개" : 85,"정아무개" : 90,"이아무개" : 70}
result = 0
person = []
scoere = []

person = list(data.keys())
score = list(data.values())

print("전체학생수 :",len(data),"명")
print("--------------------------")

for i in range(0,4):
    print(person[i],":",score[i])

print("--------------------------")

for y in data:
    result += data[y]
print("평균 :",result/len(data),"점")

#9

