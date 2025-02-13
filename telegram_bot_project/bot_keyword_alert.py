def setup_keyword_alerts(bot):
    alert_keywords = ["긴급", "중요", "알림"]

    @bot.message_handler(func=lambda message: any(keyword in message.text for keyword in alert_keywords))
    def alert_message(message):
        bot.reply_to(message, "🚨 중요한 메시지가 도착했습니다! 내용을 확인해 주세요.")

        