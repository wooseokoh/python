import requests
from bs4 import BeautifulSoup

# 인터넷 연결하기
url = "https://finance.naver.com/item/main.nhn?code=005930"
result = requests.get(url)
print(result)

# 분석하기

# BeautifulSoup(result.content, "html.parser")
# print(result.content)

bs_obj = BeautifulSoup(result.content, "html.parser")
print(bs_obj)

no_today = bs_obj.find("p", {"class":"no_today"}) # (태그,{클래스:클래스명})
print(no_today)

blind_now = no_today.find("span", {"class":"blind"})
print(blind_now)
print(blind_now.text) # text = tag 사이의 값을 가져온다


