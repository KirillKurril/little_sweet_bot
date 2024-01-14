from PIL import Image
from io import BytesIO
import os
import requests

def compress_photo(bot, message):
    print("Принято фото на обработку")
    photo_url = bot.get_file_url(message.photo[-1].file_id)
    response = requests.get(photo_url)
    img = Image.open(BytesIO(response.content))
    width, height = img.size
    print(f"photo width: {width}\nphoto height: {height}")
    proportion = 512/width if width >= height else 512/height
    new_size = (int(width * proportion), int(height * proportion))
    resized_img = img.resize(new_size)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    photo_name = os.path.join(current_dir, f"photo_processing\\{message.from_user.username}.png")
    resized_img.save(photo_name)
    return photo_name