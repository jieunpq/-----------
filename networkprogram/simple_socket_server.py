from socket import *  # 소켓 모듈 임포트

# === 서버 소켓 설정 ===
# 서버 소켓 생성
host = "127.0.0.1"  # 자기 자신(로컬 컴퓨터) IP
port = 12345  # 프로그램을 식별할 포트 번호

# 소켓 객체 생성 (AF_INET: IPv4, SOCK_STREAM: TCP 통신)
server_socket = socket(AF_INET, SOCK_STREAM)  
server_socket.bind((host, port))  # IP와 포트를 소켓에 할당 (바인딩)
server_socket.listen()  # 연결 요청 대기 상태로 전환

print("서버 소켓 생성 및 바인딩 완료")

# 클라이언트 연결 요청 대기
client_socket, client_address = server_socket.accept()  # 클라이언트 연결 요청 수락
print(str(client_address) + " 클라이언트 접속 하였습니다")

# === 데이터 송수신 ===
data = client_socket.recv(1024)  # 클라이언트가 보낸 데이터 수신 (최대 1024바이트)
print("받은 데이터 : " + data.decode("utf-8"))  # 바이트 데이터를 문자열로 디코딩

# 클라이언트에게 응답 데이터 전송
client_socket.sendall("안녕하세요. 저는 서버입니다.".encode("utf-8"))  # 문자열 데이터를 바이트로 인코딩 후 전송

# 서버 소켓 닫기
server_socket.close()
