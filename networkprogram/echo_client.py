import socket

# === 클라이언트 소켓 재사용 설정 ===
import socket

server_host = 'localhost'  # 연결할 서버 IP
server_port = 54321  # 연결할 서버 포트 번호

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 클라이언트 소켓 생성
client_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 포트를 재사용 가능하도록 설정

# 서버와 연결
client_sock.connect((server_host, server_port))
print(f'Server: {server_host}, {server_port}와 정상적으로 연결')

# === 클라이언트와 실시간 데이터 송수신 ===
while True:
    message = input(">>> ")  # 사용자 입력 메시지
    client_sock.sendall(message.encode('utf-8'))  # 입력 데이터를 서버로 전송
    message = client_sock.recv(1024)  # 서버로부터 응답 수신
    print(f"server: {message.decode()}")  # 서버 응답 출력