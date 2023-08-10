#pyTelegramBotAPI
import telebot, compress_photo, text_message_processing

TOKEN = "6430171578:AAEHVk6g0h7GVkuR12piZRt9LrCRmn2Yi0U"

bot = telebot.TeleBot(TOKEN)

last_message_flag = None

@bot.message_handler(commands=["start"])
def start(message):
    global last_message_flag
    last_message_flag = None
    bot.send_message(message.chat.id , "Я так давно тебя не видела, дорогой! Мяу!")    
    
@bot.message_handler(content_types=["text"])
def text_response(message):
    
    global last_message_flag
    
    last_message_flag = text_message_processing.response(bot, message)   

@bot.message_handler(content_types=['photo'])
def photo_processing(message):
    global last_message_flag
    print(last_message_flag)
    if last_message_flag == "ask_for_pic_proc":
       photo_name = compress_photo.compress_photo(bot, message)

       with open(photo_name, "rb") as file:
           bot.send_document(message.chat.id, file)
       last_message_flag = None

bot.polling(non_stop=True)