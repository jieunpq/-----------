from socket import *  # 소켓 모듈 임포트

# === 클라이언트 소켓 설정 ===
host = "127.0.0.1"  # 연결할 서버 IP (자기 자신)
port = 12345  # 연결할 서버 포트 번호

client_socket = socket(AF_INET, SOCK_STREAM)  # 소켓 생성
client_socket.connect((host, port))  # 서버와 연결 요청
print("연결확인 완료")

# 클라이언트가 서버로 데이터 전송
client_socket.send("안녕하세요. 저는 클라이언트입니다.".encode("utf-8"))  # 문자열 데이터를 바이트로 인코딩 후 전송

# 서버가 보낸 데이터 수신
data = client_socket.recv(1024)  # 데이터 수신 (최대 1024바이트)
print("받은 데이터 : " + data.decode("utf-8"))  # 바이트 데이터를 문자열로 디코딩

# 클라이언트 소켓 닫기
client_socket.close()