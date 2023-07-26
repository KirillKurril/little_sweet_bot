#pyTelegramBotAPI
import telebot, re, time, os, requests
from random import randrange as rand 


TOKEN = "6430171578:AAEHVk6g0h7GVkuR12piZRt9LrCRmn2Yi0U"

bot = telebot.TeleBot(TOKEN)

last_message_flag = None

send_pic = r".*?(пришли|скинь|отправь).*?(пикчу|фотку|фотографию|фотокарточку).*?"
procces_pic = r".*?(обработ).*?(пикчу|фотку|фотографию|фотокарточку).*?"

@bot.message_handler(commands=["start"])
def start(message):
    global last_message_flag
    last_message_flag = None
    bot.send_message(message.chat.id , "Я так давно тебя не видела, дорогой! Мяу!")    
    
@bot.message_handler(content_types=["text"])
def text_response(message):
    
    global last_message_flag
    last_message_flag = None
    
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
        bot.stop_polling()

    elif "работаешь" in message.text.lower():
        bot.send_message(message.chat.id , "да :3")
        
    elif re.search(send_pic, message.text.lower()):
        time.sleep(2)
        bot.send_message(message.chat.id , "аок")
        time.sleep(2)
        bot.send_message(message.chat.id , "щя")
        with open("sohry/loading.gif", "rb") as gifka:
            load = bot.send_animation(message.chat.id , gifka)
            time.sleep(4)
            bot.delete_message(load.chat.id, load.id)
            rnum = rand(6)
            with open(f"sohry/sus_{rnum}.jpg", "rb") as photo_file:
                bot.send_photo(message.chat.id, photo_file)

    elif re.search(procces_pic, message.text.lower()):
        last = bot.send_message(message.chat.id , "Хорошо, кидай")
        last_message_flag = "ask_for_pic_proc"

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

@bot.message_handler(content_types=['photo'])
def photo_processing(message):
    global last_message_flag
    print(last_message_flag)
    if last_message_flag == "ask_for_pic_proc":
        print("Принято фото на обработку")
        photo_url = bot.get_file_url(message.photo[-1].file_id)
        photo_name = f"photo_processing/{message.from_user.username}.jpg"
        with open(photo_name, "wb") as file:
            file.write(requests.get(photo_url).content)
        last_message_flag = None

bot.polling(non_stop=True)