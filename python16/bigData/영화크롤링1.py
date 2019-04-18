import requests
from bs4 import BeautifulSoup

def get_name():
    url = "https://movie.naver.com/movie/running/current.nhn?order=reserve"
    result = requests.get(url)

    bs_obj = BeautifulSoup(result.content, "html.parser")

    dt_list = bs_obj.findAll("dt", {"class":"tit"})
#     print(len(dt_list))
#     print(dt_list)
    title_list = []
    for title in dt_list:
        title_list.append(title.find("a").text)
#         a = title.find("a")
#         print(a.text)
    return title_list
def get_reserve():
    url = "https://movie.naver.com/movie/running/current.nhn?order=reserve"
    result = requests.get(url)

    bs_obj = BeautifulSoup(result.content, "html.parser")

    dt_list = bs_obj.findAll("div", {"class":"star_t1 b_star"})
#     print(len(dt_list))
#     print(dt_list)
    reserve_num = []
    for title in dt_list:
        reserve_num.append(title.find("span", {"class":"num"}).text)
#         title = title.find("span", {"class":"num"}.text)
#         print(title.text)
    return reserve_num


file = open("moive.txt", "wt",encoding='UTF8')
 
title_list = get_name()
reserve_num = get_reserve()
file.write("영화"+"\t"+"예매율"+"\n")
for index in range(0,115,1):
    name = title_list[index]
    price = reserve_num[index]
    file.write(name + "\t" + price + "\n")

file.close()
     
 






