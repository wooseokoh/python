import requests
from bs4 import BeautifulSoup

def get_names(page):
    url = "https://finance.naver.com/sise/entryJongmok.nhn?&page="+str(page)
    result = requests.get(url)
#     print(result)
    
    bs_obj = BeautifulSoup(result.content, "html.parser")
#     print(bs_obj)
    
    td_list = bs_obj.findAll("td", {"class":"ctg"})
#     print(td_list)
    
    company_names = []
    
    for td in td_list:
        company_names.append(td.find("a").text)   
#     print(company_names)
    
    return company_names

def get_now_price(page):
    url = "https://finance.naver.com/sise/entryJongmok.nhn?&page="+str(page)
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    td_list = bs_obj.findAll("td", {"class":"number_2"})
    
    now_price_list = []
    td_list_count = len(td_list)
    
    for index in range(0, td_list_count, 4):
        now_price_list.append(td_list[index].text)      
#     print(now_price_list)
    
    return now_price_list

def total_infor():
    company_names = get_names()
    now_price_list = get_now_price()
    
    print("회사이름", "\t", "주식가")
    for index in range(0,10,1):
        name = company_names[index]
        price = now_price_list[index]
        print(name,"\t",price)
    
def total_infor2(page):
    company_names = get_names(page)
    now_price_list = get_now_price(page)
    
    print(page,":페이지>> 회사이름", "\t", "주식가")
    for index in range(0,10,1):
        name = company_names[index]
        price = now_price_list[index]
        print(name,"\t",price)
        
def total_infor3(page):
    company_names = get_names(page)
    now_price_list = get_now_price(page)
    
    print(page,":페이지>> 회사이름", "\t", "주식가")
    for index in range(0,10,1):
        name = company_names[index]
        price = now_price_list[index]
        print(name,"\t",price)
        
def total_infor4(page):
    company_names = get_names(page)
    now_price_list = get_now_price(page)
    
    return company_names, now_price_list

if __name__ == '__main__':
    
    for page in range(1,11):
        total_infor3(page)
        print()
        
    total_names = []
    total_prices = []
        
    for page in range(1, 11, 1):
        company_names, now_price_list = total_infor4(page)
        total_names.extend(company_names)
        total_prices.extend(now_price_list)
        print(len(total_names))
        print(len(total_prices))
    
    print(len(total_names))
    print(len(total_prices))
    print()
    
    print(total_names)
    print(total_prices)
            
        



    
    





    
    