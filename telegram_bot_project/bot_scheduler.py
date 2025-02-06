import telebot
import schedule
import time

API_KEY = "7153124936:AAF1JXT_vudH5F1Gg_VYLBmN3PymuKkbmxM"  # 📌 본인의 API 키 입력
CHAT_ID = "7846418440"  # 📌 메시지를 받을 채팅 ID 입력 (개인 또는 그룹)
bot = telebot.TeleBot(API_KEY)
scheduled_message = []


# 예약된 메시지 전송 함수
def send_scheduled_message(chat_id, text):
    bot.send_message(chat_id, text)

@bot.message_handler(commands=['schedule'])
def schedule_message(message):
    try:
        msg_parts = message.text.split()
        schedule_time = msg_parts[1] # "HH:MM" 형식
        schedule_text = " ".join(msg_parts[2:])
        chat_id = message.chat.id

        # 스케줄 등록
        schedule.every().day.at(schedule_time).do(send_scheduled_message, chat_id, schedule_text)
        bot.reply_to(message, f"🕒 {schedule_time}에 '{schedule_text}' 메시지가 예약되었습니다.")
    except Exception as e:
        bot.reply_to(message, "❌ 예약 형식이 잘못되었습니다. 예시: /schedule 09:00 회의 시작합니다.")

print("🤖 예약 메시지 봇이 실행 중입니다...")

# 무한 루프로 스케줄 실행
while True:
    schedule.run_pending()
    time.sleep(1)
