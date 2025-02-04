import threading
import time
import pyautogui

def print_numbers():
    for i in range(1,11):
        time.sleep(1) #1초 동안 다른 쓰레드를 돌려라
        print(1)

thread_gui = threading.Thread(target = print_numbers)
thread_gui = threading.Thread(target = print_numbers)
thread_gui.start()

pyautogui.alert('코딩유치원 자주 와주세요')
# print_numbers()

# 모든 프로그램이 쓰레드 기반인 증거
# print(threading.current_thread().name)
# print("쓰레드 확인",threading.current_thread().name)
