import telebot
from telebot import types

bot = telebot.TeleBot('6803648023:AAHuEu6RRF7eLyCT-5Iqqwzjb6H87XqRq4o')


@bot.message_handler(commands=['start', 'help', 'mute'])
def handle_start_help(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id,
                         "Привет, я твой личный помошник по чату в Телеграме.\nДля того чтобы я начал выполнять свою работу, добавь меня в свой чат")
    elif message.text == "/help":
        bot.send_message(message.from_user.id,
                         "Команды Администратора/Модератора:\n/mute - Выдать мут пользователю\n/Give role - Выдать роль пользователю\n/Ban - Выдать бан пользователю\n/Kick - Кикнуть пользователя")
    elif message.text.startswith("/mute"):
        username_to_mute = message.text.split(" ", 1)[1].strip()

        try:
            user = bot.get_chat_member(message.chat.id, username_to_mute)
            user_id = user.user.id

            bot.restrict_chat_member(message.chat.id, user_id, types.ChatPermissions())
            bot.reply_to(message, f"ВНИМАНИЕ: Пользователь @{username_to_mute} был замьючен!")
        except Exception as e:
            bot.reply_to(message, f"Не удалось выдать мут пользователю")


bot.infinity_polling()
