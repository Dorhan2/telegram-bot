import telebot
import os
import random
import requests
bot = telebot.TeleBot("773994396:AAFv5rMpLV6GdNdEtO8ohRXgQJt6fmyDcfM")

# @bot.message_handler(command=["stop"])
# def handle_start(message):
#       hide_markup = telebot.types.ReplyKeyboardRemove()
#       hide_markup.row()
#       bot.send_message(message.from_user.id,"ti petux",reply_markup=hide_markup)


@bot.message_handler(commands=["start"])
def handle_start(message):
        user_markup = telebot.types.ReplyKeyboardMarkup(True,False)
        user_markup.row("/start", "/stop")
        user_markup.row("Dnevnik", "Score")
        bot.send_message(message.from_user.id, "Слыш ты", reply_markup=user_markup)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "Dnevnik" or message.text == "dnevnik":
        directory = 'C:\Memi'
        all_files_in_direct=os.listdir(directory)
        print(all_files_in_direct)
        print(id)
        random_file = random.choice(all_files_in_direct)
        img= open(directory + '/' + random_file,'rb')
        bot.send_chat_action(message.from_user.id, "upload_photo")
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text == "Score" or message.text == "score":
        bot.send_message(message.chat.id, "LaL")
    else:
        bot.send_message(message.chat.id, "LoL KeK cheburek")

# @bot.message_handler(content_types=["text"])
# def handle_text(message):
#     if message.text == "Score" or message.text == "score":
#         bot.send_message(message.chat.id, "LaL")
#     # elif message.text == "Dnevnik" or message.text == "dnevnik":
#     #     bot.send_message(message.chat.id, "BoM")
#     else:
#         bot.send_message(message.chat.id, "LoL KeK cheburek")





bot.polling(none_stop=True,timeout=3.5)#interval=0)