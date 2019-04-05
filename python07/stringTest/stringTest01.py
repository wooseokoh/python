# data = "파이썬은 아주 Easy!!!! but high"
#  
#  전부 대문자 변환
# print(data.upper())
#  전부 소문자 변환
# print(data.lower())
#  각 단어의 앞 글자만 대문자로 변한
# print(data.title())
#  대/소문자 변환
# print(data.swapcase())
 
data = "파이썬은 아주 Easy!!!! but high"
 
print(len(data))
print(data.count(" "))
print(data.find("아주"))
print(data.startswith("파"))
print(data.endswith("h"))

data = "   파이썬은 아주 Easy!!!! but high   "

print(data.strip())
print(data.rstrip())
print(data.lstrip())

data2 = data.replace("파이썬", "장고")
print(data2)
print(data2.split("!!!!"))

