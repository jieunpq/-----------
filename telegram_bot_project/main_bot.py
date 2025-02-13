import telebot
from telebot import types
from bot_weather import setup_weather_responses
from bot_keyword_alert import setup_keyword_alerts
from bot_translator import setup_translator
from bot_scheduler import setup_scheduled_messages
from bot_group import setup_group_messages

API_KEY = '7153124936:AAF1JXT_vudH5F1Gg_VYLBmN3PymuKkbmxM'
bot = telebot.TeleBot(API_KEY)

# 모듈 함수 설정
setup_weather_responses(bot)
setup_keyword_alerts(bot)
setup_translator(bot)
setup_scheduled_messages(bot)
setup_group_messages(bot, '-4601050259')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "안녕하세요! 저는 다양한 기능을 제공하는 챗봇입니다🤖\n"
        "사용할 수 있는 명령어는 다음과 같습니다:\n"
        "🌤️날씨 정보 조회 /weather\n"
        "👥그룹 메시지 전송 '/groupmsg [메시지 내용]'\n"
        "⏰메시지 예약 '/schedule [시간] [메시지 내용]'\n"
        "🌐메시지 번역 /translate\n"
        "📌메뉴 다시 보기 /start\n"
        "🔎도움말 /help\n\n"
        "📢긴급 메시지 알림 기능이 켜졌습니다."
    )
    bot.send_message(message.chat.id, welcome_text)

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "[🔎도움말] 아래는 자주 묻는 질문과 답변입니다:\n"
        "1. 날씨 정보는 어떻게 받나요?\n"
        "   - '/weather'을 명령어 전송 후, '[도시이름(영문)]'를 입력하여, 날씨 정보를 조회할 수 있습니다.\n"
        "2. 메시지를 어떻게 예약하나요?\n"
        "   - '/schedule [시간] [메시지 내용]' 형식을 사용하여 메시지를 예약할 수 있습니다.\n"
        "3. 메시지를 어떻게 번역하나요?\n"
        "   - '/translate' 명령어 전송 후, '[번역하고 싶은 메시지]'를 입력하여, 메시지를 번역할 수 있습니다.\n"
        "4. 그룹 메시지는 어떻게 보내나요?\n"
        "   - '/groupmsg [메시지 내용]' 형식을 사용하여 그룹에 메시지를 전송할 수 있습니다.\n"
        "5. 긴급 알림 기능은 무엇인가요?\n"
        "   - 긴급/중요/알림 등의 내용이 포함된 메시지가 수신되면, 챗봇이 알림 문자를 보냅니다.\n"
        "     (/start 입력 후, 자동으로 설정됨)\n"
    )
    bot.send_message(message.chat.id, help_text)

@bot.message_handler(func=lambda message: True)  # 가장 낮은 우선순위
def handle_message(message):
    bot.send_message(message.chat.id, "죄송합니다, 이해하지 못했습니다. '/help'를 입력하여 도움말을 확인하세요.")

bot.polling()
