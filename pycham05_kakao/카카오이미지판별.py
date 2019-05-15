import requests # 의존성있는 라이브러리(다른 라이브러리가 같이 설치됨)
import argparse # 인자값을 줘서 동작을 다르게 하고 싶은 경우
import sys
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

API_URL = 'https://kapi.kakao.com/v1/vision/product/detect'
MYAPP_KEY = '1714af7aa1a65997f5a628ab58ee63fd' # 카카오 REST API키

def detect_product(image_url):

    headers = {'Authorization': 'KakaoAK {}'.format(MYAPP_KEY)}
    try:
        data = { 'image_url' : image_url}
        resp = requests.post(API_URL, headers=headers, data=data)
        print(resp)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        print(str(e))
        sys.exit(0)

def show_products(image_url, detection_result):
    try:
        image_resp = requests.get(image_url)
        image_resp.raise_for_status()
        file_jpgdata = BytesIO(image_resp.content)
        image = Image.open(file_jpgdata)
    except Exception as e:
        print(str(e))
        sys.exit(0)

    draw = ImageDraw.Draw(image)
    for obj in detection_result['result']['objects']:
        x1 = int(obj['x1'] * image.width)
        y1 = int(obj['y1'] * image.height)
        x2 = int(obj['x2'] * image.width)
        y2 = int(obj['y2'] * image.height)
        draw.rectangle([(x1, y1), (x2, y2)], fill=None, outline=(255, 0, 0, 255))
        draw.text((x1 + 5, y1 + 5), obj['class'], (255, 0, 0))
    del draw

    return image

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Detect Products.')
    parser.add_argument('image_url', type=str, nargs='?',
                        default="http://t1.daumcdn.net/alvolo/_vision/openapi/r2/images/06.jpg",
                        help='')
    # 다른것 F12이용 하여 가져오기

    args = parser.parse_args()

    detection_result = detect_product(args.image_url)

    print(detection_result)
    print(detection_result['result'])
    print(detection_result['result']['objects'])
    for object in detection_result['result']['objects']:
        print('x1: ', object['x1'], 'y1: ', object['y1'], 'class: ', object['class'])
    print(len(detection_result['result']['objects']))

    image = show_products(args.image_url, detection_result)

    image.show()

