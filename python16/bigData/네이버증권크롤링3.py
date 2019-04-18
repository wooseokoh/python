import requests
from bs4 import BeautifulSoup

def get_price(code): # 입력값 code
    # 인터넷 연결하기
    url = "https://finance.naver.com/item/main.nhn?code="+code
    result = requests.get(url)
#     print(result)
    
    bs_obj = BeautifulSoup(result.content, "html.parser")
#     print(bs_obj)
    
    no_today = bs_obj.find("p", {"class":"no_today"})
#     print(no_today)
    
    blind_now = no_today.find("span", {"class":"blind"})
#     print(blind_now.text)
    return blind_now.text


company_codes = ["027740", "005930", "020560","002995","001745","215600","136480","068270","054780","044960"]
company_names = ["마니커", "삼성전자", "아시아나항공","금호산업우","sk네트웍스우","신라젠","하림","셀트리온","키이스트","이글벳"]

index = 0
for code in company_codes:
    price = get_price(code)
    name = company_names[index]
    print(name,":", price)
    index = index + 1
    
    
    
    
    