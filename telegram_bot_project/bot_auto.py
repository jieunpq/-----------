import telebot

API_KEY = "7153124936:AAF1JXT_vudH5F1Gg_VYLBmN3PymuKkbmxM"  # 📌 본인의 API 키 입력

bot = telebot.TeleBot(API_KEY)

# 'start' 또는 'hello' 입력 시 자동 응답
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "안녕하세요! 😊 저는 자동화된 텔레그램 봇입니다.")

# 키워드 기반 자동 응답
@bot.message_handler(func=lambda message: True)
def keyword_responses(message):
    text = message.text.lower() # 입력한 메시지를 소문자로 변환

    if "안녕" in text or "hello" in text:
        bot.reply_to(message, "안녕하세요! 😊")
    elif "날씨" in text:
        bot.reply_to(message, "🌤️ 오늘 날씨는 좋습니다! ☀️")
    elif "이름" in text:
        bot.reply_to(message, "저는 텔레그램 자동화 봇입니다! 🤖")
    else:
        bot.reply_to(message, "죄송해요, 이해하지 못했어요. 😅")

print("🤖 자동 메시지 봇이 실행 중입니다...")
bot.polling()
