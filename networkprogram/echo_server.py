from socket import *


# === 서버 소켓 재사용 설정 ===
host = "localhost"  # 자기 자신(로컬 컴퓨터) IP
port = 54321  # 포트 번호

server_socket = socket(AF_INET, SOCK_STREAM)  # 소켓 생성
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 포트를 즉시 재사용 가능하도록 설정

server_socket.bind((host, port))  # IP와 포트를 소켓에 할당 (바인딩)
server_socket.listen(100)  # 최대 100개의 클라이언트 요청 대기 상태로 설정

# 클라이언트 연결 요청 대기
client_socket, client_address = server_socket.accept()  # 클라이언트 연결 요청 수락
print(str(client_address) + " 클라이언트 접속 하였습니다")

# === 반복 처리로 실시간 데이터 송수신 ===
while True:
    data = client_socket.recv(1024)  # 클라이언트가 보낸 데이터 수신
    print("받은 데이터 : " + data.decode("utf-8"))
    client_socket.sendall("안녕하세요. 저는 서버입니다.".encode("utf-8"))  # 응답 데이터 전송
