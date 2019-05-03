import turtle

t = turtle.Pen()

while True:
    방향 = input("왼쪽: 0, 오른쪽 : 1 >>" )
    각도 = int(input("각도를 입력하세요 :" ))
    if 방향 == '0':
        t.left(각도) # 왼쪽으로 90도 방향을 전환
        t.forward(200) # 앞으로 쭉 진행
    if 방향 == '1':
        t.right(각도) # 오른쪽으로 90도 방향을 전환
        t.forward(200) # 앞으로 쭉 진행



