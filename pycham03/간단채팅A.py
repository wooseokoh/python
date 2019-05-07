import socket

# 네트워크 통신을 하려면, socket이 필요
# 음성통신에서 전화기 역할
# 네트워크 통신 == 소켓 통신.

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # 송신용
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # 수신용
print("1. A채팅 소켓 준비 완료..")
sock2.bind(('192.168.0.113', 3333))
print('ip/port binding 완료. binding된 port번호는 3333번..')

while True:
    # 먼저, 데이터를 받는다.
    data, addr = sock2.recvfrom(1024)
    print('채팅B 입력>>', data.decode('utf-8'))

    # 송신할 데이터 입력 후 전송.
    data2 = input('채팅A 입력 : ')
    sock.sendto(data2.encode('utf-8'), ('192.168.0.113', 4444))