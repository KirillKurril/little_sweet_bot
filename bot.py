#pyTelegramBotAPI
import telebot, re, sys, time
from random import randrange as rand 


TOKEN = "6430171578:AAEHVk6g0h7GVkuR12piZRt9LrCRmn2Yi0U"

bot = telebot.TeleBot(TOKEN)

send_pic = r".*?(пришли|скинь|отправь).*?(пичку|фотку|фотографию|фотокарточку)"

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id , "Я так давно тебя не видела, дорогой! Мяу!")    
    
@bot.message_handler(content_types=["text"])
def text_response(message):
    print(message.text)
    print (re.search(send_pic, message.text.lower))

    if any(substr in message.text.lower() for substr in ["иди нахуй", "нахуй иди","пошла нахуй", "нахуй пошла", "в пизду иди", "иди в пизду", "ты сука", "сука ты"]):
        print(1)
        bot.reply_to(message, "За базаром следи, сын ебаной шлюхи, я твоей матери ебало разобью (^ ω ^)")

    elif any(substr in message.text.lower() for substr in ["привет", "приффки", "приф", "хай", "хой", "хайль", "шо ты", "прив", "здарова", "панкам хой, остальным соболезную"]):
        bot.send_message(message.chat.id, "Привет-привет! А я уже успела по тебе соскучиться (>ω^)")

    elif  "анекдот" in message.text.lower():
        with open("audios/XD.ogg", "rb") as voice_file:
            bot.send_voice(message.chat.id, voice_file)

    elif any(substr in message.text.lower() for substr in ["мяу", "котик"]):
          bot.send_message(message.chat.id , "Мяу мяу (´｡• ᵕ •｡`) ")

    elif any(substr in message.text.lower() for substr in ["пока", "до скорого", "до встречи", "увидимся", "пока-пока", "мне пора"]):
        bot.send_message(message.chat.id , "Неееет, не уходи, не уходи! Побудь со мной ещё немножечко. Я буду очень-очень скучатб ~(>_<~)")

    elif message.text == "25.08":
        sys.exit()

    elif re.search(send_pic, message.text.lower()):
        time.sleep(2)
        bot.send_message(message.chat.id , "аок")
        time.sleep(2)
        bot.send_message(message.chat.id , "щя")
        bot.send_animation(message.chat.id ,"sohry/loading.gif")

    else:
        match rnum:= rand(5):
            case 0:
                bot.send_message(message.chat.id , "жесть")
            case 1:
                bot.send_message(message.chat.id , "треш")
            case 2:
                bot.send_message(message.chat.id , "капец")
            case 3:
                bot.send_message(message.chat.id , "беднявочка")    
            case 4:
                bot.send_message(message.chat.id , "А что это? Я о таком в твиттере ещё не читала (・・ ) ?")    


bot.polling(non_stop=True)