import threading
import time

#클래스기반으로 쓰레드 만들기
# threading.Thread 클래스를 상속받아서 새로운 클래스를 만든다.
# run() 메소드를 오버라이딩
class Worker(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    #run() 메소드는 쓰레드가 실행할 코드를 포함한다.
    def run(self): # main 함수 역할
        print("sub thread start! ", threading.current_thread().name)
        time.sleep(3)
        print("sub thread end! ", threading.current_thread().name)

for i in range(5):
    name = f"thread number: {i}"
    t = Worker(name)
    t.start() # 쓰레드 실행은 run 메소드가 아님 start 메소드로 실행