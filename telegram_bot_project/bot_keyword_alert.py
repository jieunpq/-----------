import telebot

API_KEY = "7153124936:AAF1JXT_vudH5F1Gg_VYLBmN3PymuKkbmxM"
bot = telebot.TeleBot(API_KEY)
alert_keywords = ["긴급", "중요", "알림"]

@bot.message_handler(func=lambda message: any(keyword in message.text for keyword in alert_keywords))
def keyword_alert(message):
    bot.reply_to(message, "🔴 중요한 메시지가 도착했습니다! 내용을 확인해 주세요.")

print("🤖 키워드 알림 봇이 실행 중입니다...")
bot.polling()