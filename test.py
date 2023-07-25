import re, time, os
print("программа запущена")
send_pic = r".*?(пришли|скинь|отправь).*?(пичку|фотку|фотографию|фотокарточку)"
str = input()
if re.search(send_pic, str):
    time.sleep(2)
    print("аок")
    time.sleep(2)
    print("щя")
    file = "sohry/loading.gif"
    print(os.path.exists(file))