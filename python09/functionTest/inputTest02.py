'''
입력값 5개를 받아서 리스트에 넣은 후
다음과 같이 출력하는 함수를 정의하여 호출 실행
내가 좋아하는 색깔은 green, red, orange, white, blue



'''


def value():
    color = []
    for x in range(0,5):
        color.append(input())
    return print(color, end = " ")


if __name__ == '__main__':
    print("내가 좋아하는 색깔은 ")
    value()

