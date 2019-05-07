import socket

# 네트워크 통신을 하려면, socket이 필요
# 음성통신에서 전화기 역할
# 네트워크 통신 == 소켓 통신.

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP 방식
print("1. 소켓 준비 완료..")
sock.bind(('192.168.0.113', 7000))
print('ip/port binding 완료. binding된 port번호는 7001번..')

while True:
    data = input('전송할 데이터 : ')
    sock.sendto(data.encode('utf-8'), ('192.168.0.113', 6000))
    print('데이터 송신완료')