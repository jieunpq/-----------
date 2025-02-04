import telebot

API_KEY = "7153124936:AAF1JXT_vudH5F1Gg_VYLBmN3PymuKkbmxM"  # 📌 본인의 API 키를 입력

bot = telebot.TeleBot(API_KEY)

# 'start' 또는 'hello' 입력 시 자동 응답
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "안녕하세요! 🤖 자동 응답 기능이 추가되었습니다.")

# 특정 단어가 포함된 메시지에 자동 응답
@bot.message_handler(func=lambda message: "안녕" in message.text)
def say_hello(message):
    bot.reply_to(message, "안녕하세요! 😊 저는 자동화된 텔레그램 봇입니다.")

print("🤖 자동 메시지 봇이 실행 중입니다...")
bot.polling()
