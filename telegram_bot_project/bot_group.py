import telebot
import schedule
import time

API_KEY = "7153124936:AAF1JXT_vudH5F1Gg_VYLBmN3PymuKkbmxM"  # 📌 본인의 API 키 입력
GROUP_CHAT_ID = "-4601050259"  # 📌 그룹의 Chat ID 입력

bot = telebot.TeleBot(API_KEY)

# 그룹에 메시지 전송하는 함수
def send_group_message():
    bot.send_message(GROUP_CHAT_ID, "📢 이 메시지는 일정 시간마다 자동으로 전송됩니다! ⏰")
 
# 1시간마다 메시지 전송
schedule.every(1).hours.do(send_group_message)  # ⏰ 원하는 간격으로 변경 가능

print("🤖 그룹 메시지 봇이 실행 중입니다...")

# 무한 루프로 스케줄 실행 (반복 실행)
while True:
    schedule.run_pending()
    time.sleep(1)