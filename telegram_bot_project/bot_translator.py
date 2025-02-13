from googletrans import Translator

def setup_translator(bot):
    @bot.message_handler(commands=['translate'])
    def request_translation(message):
        msg = bot.reply_to(message, "🌐 번역할 메시지를 입력해주세요.")
        bot.register_next_step_handler(msg, perform_translation)

    def perform_translation(message):
        translator = Translator()
        try:
            translated = translator.translate(message.text, dest='ko')
            bot.send_message(message.chat.id, f"💬 번역된 메시지: {translated.text}")
        except Exception as e:
            bot.send_message(message.chat.id, "번역 오류가 발생했습니다. 다시 시도해주세요.")
