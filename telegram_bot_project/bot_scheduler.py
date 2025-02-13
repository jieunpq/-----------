import schedule
import time
import threading

def setup_scheduled_messages(bot):
    def send_scheduled_message(chat_id, text):
        bot.send_message(chat_id, text)

    @bot.message_handler(commands=['schedule'])
    def schedule_message(message):
        try:
            msg_parts = message.text.split()
            schedule_time = msg_parts[1]  # "HH:MM" 형식
            schedule_text = " ".join(msg_parts[2:])
            chat_id = message.chat.id

            schedule.every().day.at(schedule_time).do(send_scheduled_message, chat_id, schedule_text)
            bot.reply_to(message, f"🕒 {schedule_time}에 '{schedule_text}' 메시지가 예약되었습니다.")
        except IndexError:
            bot.reply_to(message, "예약 형식이 잘못되었습니다. 예시: /schedule 09:00 회의 시작합니다.")

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

# 스케줄러 스레드 시작
scheduler_thread = threading.Thread(target=run_scheduler)
scheduler_thread.start()
