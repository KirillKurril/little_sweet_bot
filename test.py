import requests

url = "https://www.imgonline.com.ua/resize-image.php"

response = requests.get(url)
html_content = response.text

data = {
    "imwigth" : "512",
    "imheight" : "512"
    
}