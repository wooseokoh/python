import json
import os
import re
import urllib.request
import time
import random
import datetime

 

from bs4 import BeautifulSoup
from requests import get
from selenium import webdriver
from urllib.error import HTTPError
from urllib.parse import urlencode


DRIVER_DIR = 'C:\\Users\\user\\Downloads\\chromedriver_win32\\chromedriver.exe'


def get_naver_token():


    chromedriver_path = os.environ.get('CHROMEDRIVER_PATH')

    chromedriver_path = DRIVER_DIR

    print(chromedriver_path )

    naver_cid = "T1A9iunc50tdCmJ5R4H3"

    naver_csec = "giuBBpz2Wd"

    naver_redirect = "https://developers.naver.com/popup/nid"

    driver = webdriver.Chrome(DRIVER_DIR)

    driver.implicitly_wait(3)
    driver.get('https://nid.naver.com/nidlogin.login')

    id = 'w_wv'  #ID  직접 입력

    pw = 'tkdtjr123' #비번은 직접 입력

    driver.execute_script("document.getElementsByName('id')[0].value=\'" + id + "\'")
    time.sleep(1)
    driver.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'")
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
    time.sleep(1)

    state = "REWERWERTATE"

    req_url = 'https://nid.naver.com/oauth2.0/authorize?response_type=code&client_id=%s&redirect_uri=%s&state=%s' % (naver_cid, naver_redirect, state)

    driver.get(req_url)
    time.sleep(1)


    redirect_url = driver.current_url
    temp = re.split('code=', redirect_url)
    code = re.split('&state=', temp[1])[0]
    driver.quit()

    print(redirect_url)

    url = "https://nid.naver.com/oauth2.0/token?"
    print(url)

    data = "grant_type=authorization_code" + "&client_id=" + naver_cid   + "&client_secret=" + naver_csec + "&redirect_uri=" + naver_redirect + "'&code=" + code + "&state=" + state
    print(data)

 

    request = urllib.request.Request(url, data=data.encode("utf-8"))
    request.add_header('X-Naver-Client-Id', naver_cid)
    request.add_header('X-Naver-Client-Secret', naver_redirect)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    token = ''
    if rescode == 200:
        response_body = response.read()
        js = json.loads(response_body.decode('utf 8'))
        token = js['access_token']
    else:
        print("Error Code:", rescode)
        return None

 

    if len(token) == 0:
        return None
    print(token)

    header = "Bearer " + token # Bearer 다음에 공백 추가
    url = "https://openapi.naver.com/v1/nid/me"
    request = urllib.request.Request(url)
    request.add_header("Authorization", header)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)
 

if __name__ == '__main__':

    get_naver_token()

 

    