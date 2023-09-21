import socket
import time

# TCP 소켓 생성
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ("localhost", 5000)

try:
    s.connect(address)

    while True:
        received_time = s.recv(1024).decode()
        print("현재 시각:", received_time)
        time.sleep(1)

except KeyboardInterrupt:
    print("클라이언트 종료")
finally:
    s.close()
