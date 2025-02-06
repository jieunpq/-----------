import telebot

API_KEY = "7153124936:AAF1JXT_vudH5F1Gg_VYLBmN3PymuKkbmxM" # 📌 본인의 API 키 입력

bot = telebot.TeleBot(API_KEY)

# 'start' 또는 'hello' 명령어를 입력하면 메시지 응답
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "안녕하세요! 봇이 정상적으로 작동하고 있습니다. 😊")

print("🤖 봇이 실행 중입니다...")
bot.polling()  # 봇이 계속 실행되도록 설정
