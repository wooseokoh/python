import requests
from bs4 import BeautifulSoup

def get_names(page):
    url = "https://finance.naver.com/sise/entryJongmok.nhn?&page="+str(page)
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    
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
#     print(td_list)
    
    now_price_list = []
    
    td_list_count = len(td_list)
    
    for index in range(0, td_list_count, 4):
        now_price_list.append(td_list[index].text)
    
#     print(now_price_list)
    
    return now_price_list

def total_info():
    company_names = get_names()
    now_price_list = get_now_price()
    
    print("회사이름", "\t", "주식가")
    for index in range(0, 10, 1):
        name = company_names[index]
        price = now_price_list[index]
        print(name, "\t", price)
        
def total_info2(page):
    company_names = get_names(page)
    now_price_list = get_now_price(page)
    
    print(page, ":페이지>> 회사이름", "\t", "주식가")
    for index in range(0, 10, 1):
        name = company_names[index]
        price = now_price_list[index]
        print(name, "\t\t", price)
        
def total_info3(page):
    company_names = get_names(page)
    now_price_list = get_now_price(page)
    
    return company_names, now_price_list

def total_info4(page):
    company_names = get_names(page)
    now_price_list = get_now_price(page)
    
    file = open(str(page) + ".txt", "w") # page가 int이기 때문에 str 변환
    
    for index in range(0,10,1):
        name = company_names[index]
        price = now_price_list[index]
        file.write(name+"\t"+price+"\n")
    
# for page in range(1,11,1):
#     total_info4(page)
    
# file2 = open("1.txt","r")
# for line in range(0,10):
#     line = file2.readline()
#     print(line)
#     contents = line.split("\t") # 분리 시키기
#     print(contents[0]) # 회사이름
#     print(contents[1]) # 회사주식가
    
# file2 = open("1.txt","r")
# for line in range(0,10):
#     line = file2.readline()
#     contents = line.split("\t") # 분리 시키기
#     print(contents[0]) # 회사이름
#     print(int(contents[1].replace(",",""))+100000) # 회사주식가, ","를 공백으로 바꾸고 int형으로 바꿈

file2 = open("1.txt","r")

name_list = []
price_list = []

for line in range(0,10):
    line = file2.readline()
    contents = line.split("\t")
    name_list.append(contents[0]) 
    price_list.append(int(contents[1].replace(",","")))
    
print(name_list)
print(price_list)

# 데이터 프레임을 만들어줌. 빅데이터 분석 여러기능
import pandas as pd

df = pd.DataFrame({"회사이름":name_list,"주식가":price_list})
print(df)

# 수학과 관련된 여러기능    
import numpy as np

print("최고가", np.max(df['주식가']))
print("자세한정리",df.describe())
    
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

# # plt.figure = tkinter와 같은 GUI
# plt.figure(figsize=(10,6))
# 
# index = df.index
# plt.scatter(df['회사이름'], df['주식가'], s=50) # x,y축 이름 지정과 데이터를 점으로 표시
# plt.xlabel('회사이름')
# plt.ylabel('주식가')
# plt.grid() # 격자무늬
# 
# plt.show()


plt.figure()

plt.xlabel('회사이름')
plt.ylabel('주식가')
df['주식가'].sort_values().plot(kind='barh',grid=True,figsize=(10,10))

plt.show()




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
