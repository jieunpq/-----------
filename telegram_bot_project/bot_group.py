import telebot

API_KEY = "7153124936:AAF1JXT_vudH5F1Gg_VYLBmN3PymuKkbmxM" # 📌 본인의 API 키를 입력
GROUP_CHAT_ID = "-4601050259" # 📌 메시지를 받을 그룹 채팅 ID 입력 

bot = telebot.TeleBot(API_KEY)

# 그룹에 메시지 전송하는 함수
def send_group_message():
    bot.send_message(GROUP_CHAT_ID, "📢 이 메시지는 그룹에 자동으로 전송되었습니다!")

send_group_message()

print("🤖 그룹 메시지 봇이 실행되었습니다.")