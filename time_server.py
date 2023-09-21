import socket
import time

# TCP 소켓 생성
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ("localhost", 5000)  # 호스트 주소와 포트 번호 설정
s.bind(address)
s.listen(5)

while True:
    client, addr = s.accept()  # 클라이언트 연결 대기
    print("Connection requested from", addr)

    while True:
        try:
            time.sleep(1)
            current_time = time.ctime(time.time())
            client.send(current_time.encode())  # 현재 시간을 클라이언트에게 전송
        except Exception as e:
            print("Error:", str(e))
            break

    client.close()
