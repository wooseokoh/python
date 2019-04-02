# a 선언
a = [8,3,1,7,5,4,2,6,9]
print(a)

# a 정렬
a.sort()
print(a)

# 최솟값 

for i in range(0, len(a)):
    min = a[0]
    if min > a[i]:
        min = a[i]
print(min)

# 최솟값 위치
print(a[0])

# 찾고 싶은 위치
print(a[5])