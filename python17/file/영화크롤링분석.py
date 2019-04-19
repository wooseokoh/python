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


# file = open("movie.txt", "wt",encoding='UTF8')
#      
# title_list = get_name()
# reserve_num = get_reserve()
# # file.write("영화"+"\t"+"예매율"+"\n")
# for index in range(0,10,1):
#     name = title_list[index]
#     price = reserve_num[index]
#     file.write(name + "\t" + price + "\n")
#     
# file.close()

file2 = open("movie.txt","r",encoding='UTF8')
    
title_list = []
reserve_list = []
    
for index in range(0,10):
    line = file2.readline()
    contents = line.split("\t")
    title_list.append(contents[0]) 
    reserve_list.append(float(contents[1].replace("\n","")))
        
print(title_list)
print(reserve_list)
 
import pandas as pd
  
df = pd.DataFrame({"영화제목":title_list,"예매율":reserve_list})
print(df)
  
import numpy as np
  
print("최고예매율", np.max(df['예매율']))
print('자세한정리', df.describe())
  
  
# 시각화 관련된 기능(그래프)
import matplotlib.pyplot as plt
    
import platform # 시스템의 os를 확인하여 꺠진 한글을 복구해줌
    
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
    
if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~') 
        
# plt.figure = tkinter와 같은 GUI
plt.figure(figsize=(10,6))
     
index = df.index
plt.scatter(df['영화제목'], df['예매율'], s=50) 
plt.xlabel('영화제목')
plt.ylabel('예매율')
plt.grid() # 격자무늬
     
plt.show()






