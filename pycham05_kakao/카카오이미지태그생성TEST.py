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
    for x in range(5):
        image_addr = ["http://www.jejusori.net/news/photo/201805/204575_237095_0813.jpg",
                      "https://img.withvolo.com/XXsFu4ym2n0B9wcR5JFwFKbwkFM=/0x0:1000x667/809x/62b8e83c7e93aa72f00800caf5ce5203%2Fbe36aa4a-40d8-4ac1-a1d1-d6c285d00f71-02c187c98fe3e5a0c21d5b63555762da51a0de7b.jpg",
                      "http://img.hani.co.kr/imgdb/resize/2017/1026/00500969_20171026.JPG",
                      "https://i.ytimg.com/vi/PlcglGf4S-o/maxresdefault.jpg",
                      "http://www.museumnews.kr/wordpress/wp-content/uploads/2016/04/IMG_1273-1.jpg"]
        parser = argparse.ArgumentParser(description='Detect Products.')
        parser.add_argument('image_url', type=str, nargs='?',
                            default= image_addr[x],
                            help='')


        args = parser.parse_args()

        result_json.append(generate_tag(args.image_url))

    label_eng = []
    label_kor = []
    for x in range(5):
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

