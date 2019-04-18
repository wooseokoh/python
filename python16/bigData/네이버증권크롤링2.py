import requests
from bs4 import BeautifulSoup

def get_price(code): # 입력값 code
    # 인터넷 연결하기
    url = "https://finance.naver.com/item/main.nhn?code="+code
    result = requests.get(url)
    print(result)
    
    bs_obj = BeautifulSoup(result.content, "html.parser")
#   print(bs_obj)
    
    no_today = bs_obj.find("p", {"class":"no_today"})
    print(no_today)
    
    blind_now = no_today.find("span", {"class":"blind"})
    print(blind_now.text)

get_price("005930")
get_price("051900")
get_price("035420")
