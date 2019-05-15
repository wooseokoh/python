import requests # 의존성있는 라이브러리(다른 라이브러리가 같이 설치됨)
import argparse # 인자값을 줘서 동작을 다르게 하고 싶은 경우
import sys
from PIL import Image # Pillow를 설치하면 의존적으로 PIL이 따라온다.

API_URL = 'https://kapi.kakao.com/v1/vision/face/detect'
MYAPP_KEY = '1714af7aa1a65997f5a628ab58ee63fd' # 카카오 REST API키

def detect_face(filename):
    headers = {'Authorization':'KakaoAK {}'.format(MYAPP_KEY)}
    #접속
    try:
        files = {'file' : open(filename, 'rb')} # read byte(이미지파일) 카카오방식
        resp = requests.post(API_URL, headers=headers, files=files)
        #접속 상태 확인
        print(resp)
        resp.raise_for_status()
        print("비전 kakao 접속 ok...")
        return resp.json()
    except Exception as e:
        print(str(e))
        sys.exit(0) # 프로그램 종료
    #결과를 json으로 받아옴.

def mosaic(filename, detection_result):
    image = Image.open(filename) # 이미지를 Open

    for face in detection_result['result']['faces']:
        x = int(face['x']*image.width)
        w = int(face['w'] * image.width)
        y = int(face['y'] * image.width)
        h = int(face['h'] * image.width)
        box = image.crop((x,y,x+w, y+h))
        box = box.resize((15,15), Image.NEAREST).resize((w,h), Image.NEAREST)
        image.paste(box, (x,y,x+w, y+h))

        return image
if __name__ == '__main__':

    # 카카오에 접속해서 얼굴에 대한 정보를 받아옴.
    parser = argparse.ArgumentParser(description='Mosaic faces...')
    parser.add_argument('image_file', type=str, nargs='?', default='./img/face1.jpg', help='image file to hide faces')
    args = parser.parse_args()
    detection_result = detect_face(args.image_file)
    # print(detection_result)
    print("---------------------------------")
    print(detection_result['result']['faces'])
    # 받아온 정보 중 위치값을 이용해서 모자이크 처리함.
    image = mosaic(args.image_file, detection_result)
    image.show()
