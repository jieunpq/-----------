import telebot
import schedule
import time

API_KEY = "7153124936:AAF1JXT_vudH5F1Gg_VYLBmN3PymuKkbmxM"  # 📌 본인의 API 키를 입력
CHAT_ID = "7846418440"  # 📌 메시지를 받을 채팅 ID 입력 (개인 또는 그룹)

bot = telebot.TeleBot(API_KEY)

# 예약된 메시지 전송 함수
def send_scheduled_message():
    bot.send_message(CHAT_ID, "⏰ 예약된 메시지입니다! 이 메시지는 자동으로 전송되었습니다.")

# 매일 오후 2시에 메시지 전송 (원하는 시간으로 변경 가능)
schedule.every().day.at("19:15").do(send_scheduled_message)

print("🤖 예약 메시지 봇이 실행 중입니다...")

# 무한 루프로 스케줄 실행
while True:
    schedule.run_pending()
    time.sleep(1)
