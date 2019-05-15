import requests # 의존성있는 라이브러리(다른 라이브러리가 같이 설치됨)
import argparse # 인자값을 줘서 동작을 다르게 하고 싶은 경우
import sys

API_URL = 'https://kapi.kakao.com/v1/vision/multitag/generate'
MYAPP_KEY = '1714af7aa1a65997f5a628ab58ee63fd' # 카카오 REST API키

def generate_tag(image_url):

    headers = {'Authorization': 'KakaoAK {}'.format(MYAPP_KEY)}
    try:
        data = { 'image_url' : image_url}
        resp = requests.post(API_URL, headers=headers, data=data)
        print(resp)
        resp.raise_for_status()
        print(resp.content)
        return resp.json()
    except Exception as e:
        print(str(e))
        sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Detect Products.')
    parser.add_argument('image_url', type=str, nargs='?',
                        default="http://www.jejusori.net/news/photo/201805/204575_237095_0813.jpg",
                        help='')


    args = parser.parse_args()

    result_json = generate_tag(args.image_url)

    print(result_json)
    print("----------------------")
    print(result_json['result']['label'])
    result = result_json['result']
    label_eng = result['label']
    label_kor = result['label_kr']
    print("----------------------")
    print(label_eng)
    print(label_kor)
    print("----------------------")
    for object in result_json['result']:
        print('label_eng: ', result['label'], 'label_kor: ', result['label_kr'])

