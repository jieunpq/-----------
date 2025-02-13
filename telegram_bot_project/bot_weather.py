import requests

WEATHER_API_KEY = '7659f73cb21c8be5d03fcb44ed552d52'

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"  
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        return f"📍{city}의 현재 날씨: {weather}, 기온: {temp}°C"
    else:
        return "날씨 정보를 가져오는 데 실패했습니다."

def setup_weather_responses(bot):
    @bot.message_handler(commands=['weather'])
    def ask_weather(message):
        msg = bot.reply_to(message, "🌤️ 어느 도시의 날씨를 알고 싶으신가요? (영문으로 작성해주세요)")
        bot.register_next_step_handler(msg, send_weather)

    def send_weather(message):
        city = message.text.strip()
        weather_report = get_weather(city)
        bot.send_message(message.chat.id, weather_report)


