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

def total_infor():
    title_list = get_name()
    reserve_num = get_reserve()
     
    print("제목", "\t", "예매율")
    for index in range(0,115,1):
        name = title_list[index]
        price = reserve_num[index]
        print(name,"\t",price)

def file():
    # 파일쓰기
    fileOutput = open("moive.txt", "w")
    
    fileOutput.write()

    fileOutput.close()
    
    # 파일읽기
    fileInput = open("movie.txt", "r")
    
    total_line = fileInput.readlines()
    print(total_line)
    
    fileInput.close()



if __name__ == '__main__':
    total_infor()
    file()





