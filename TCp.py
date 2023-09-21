#TCP Echo Server Program
from socket import *

port = 2500 #포트 번호
BUFSIZE =1024  #수신 버퍼 사이즈

s= socket(AF_INET, SOCK_STREAM)
s.bind(('', port)) #종단점과 소켓 결합. '임의 주소'
s.listen(1)
conn, (remotehost, remoteport) = s.accept() #연결 소켓, 연결 주소 (IP 주소 포트번호) 반환
print('connected by', remotehost, remoteport)
while True:
    data = conn.recv(BUFSIZE) #데이터 수신
    if not data: # '' 이면 종료, ''는 Flase
        break
    print("Received message: ", data.decode()) #수신 데이터 출력. 비트형으로 수신됨 문자열 변환
    conn.send(data) #수신 데이터를 되돌려 전송
conn.close()
