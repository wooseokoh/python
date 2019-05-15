import requests # 의존성있는 라이브러리(다른 라이브러리가 같이 설치됨)
import argparse # 인자값을 줘서 동작을 다르게 하고 싶은 경우
import sys
from collections import Counter

API_URL = 'https://kapi.kakao.com/v1/vision/multitag/generate'
MYAPP_KEY = '1714af7aa1a65997f5a628ab58ee63fd' # 카카오 REST API키

def generate_tag(image_url):

    headers = {'Authorization': 'KakaoAK {}'.format(MYAPP_KEY)}
    try:
        data = { 'image_url' : image_url}
        resp = requests.post(API_URL, headers=headers, data=data)
        # print(resp)
        resp.raise_for_status()
        # print(resp.content)
        return resp.json()
    except Exception as e:
        print(str(e))
        sys.exit(0)

if __name__ == "__main__":
    result_json = []
    for x in range(6):
        image_addr = ["http://img.hani.co.kr/imgdb/resize/2017/1121/00504228_20171121.JPG",
                      "http://img.hani.co.kr/imgdb/resize/2019/0315/00502341_20190315.JPG",
                      "https://cdn.tourboks.com/assets/media/blog/untitled%20folder/5%20towns/_Pic.%201_.jpg",
                      "https://cdn.tourboks.com/assets/media/blog/untitled%20folder/5%20towns/_Pic.%203_.jpg",
                      "https://cdn.tourboks.com/assets/media/blog/untitled%20folder/5%20towns/_Pic.%205_.jpg",
                      "https://ichef.bbci.co.uk/news/624/cpsprodpb/145C9/production/_103810438_gettyimages-134644324.jpg"]
        parser = argparse.ArgumentParser(description='Detect Products.')
        parser.add_argument('image_url', type=str, nargs='?',
                            default= image_addr[x],
                            help='')


        args = parser.parse_args()

        result_json.append(generate_tag(args.image_url))


    label_eng = []
    label_kor = []
    for x in range(6):
        label_eng.append(result_json[x]['result']['label'])
        label_kor.append(result_json[x]['result']['label_kr'])
    print('label_eng: ', label_eng,'label_kor: ', label_kor, sep='\n')

    eng_list = []
    kor_list = []
    print(label_eng[0][0])
    for x in label_eng:
        for y in x:
            eng_list.append(y)
    print(eng_list)
    for x in label_kor:
        for y in x:
            kor_list.append(y)
    print(kor_list)

    count_eng = Counter(eng_list)
    count_kor = Counter(kor_list)
    print(count_eng)
    print(count_kor)
    print("----------영어버전-----------")
    findword = Counter(count_eng)
    prefer = findword.most_common()
    maxword = prefer[0][1]
    command = []
    for num in prefer:
        if num[1] == maxword:
            command.append(num[0])

    print(command)  # 많은 단어




