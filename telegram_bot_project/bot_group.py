def setup_group_messages(bot, group_chat_id):
    @bot.message_handler(commands=['groupmsg'])
    def send_group_message(message):
        if len(message.text.split()) > 1:
            text = message.text.split(maxsplit=1)[1]  # 명령어 뒤의 텍스트를 추출
        else:
            text = ""  # 기본 메시지 설정

        bot.send_message(group_chat_id, text)  # 그룹 채팅에 메시지 보내기
        bot.reply_to(message, f"메시지가 그룹 '{group_chat_id}'에 전송되었습니다.💌")  # 사용자에게 전송 확인 메시지 보내기

        
