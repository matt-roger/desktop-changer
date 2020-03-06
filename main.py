import json
import requests
import ctypes
import os

with open("secret.json", "r") as read_file:
    data = json.load(read_file)

cwd = os.getcwd()
client_id = data["client_id"]
params = "/photos/random"
api = "https://api.unsplash.com"+params+"?client_id="+ client_id
headers = {"User-Agent": "Mozilla/5.0"}

res = requests.get(api, headers=headers)

if(res.status_code == 200):
    data = res.json()
    image_link = data["links"]["download"]
    image_res = requests.get(image_link)
    
    #create a new file and save the photo
    with open("img.jpeg", "wb") as out_file:
        out_file.write(image_res.content)

    ctypes.windll.user32.SystemParametersInfoW(20, 0, cwd+"\img.jpeg" , 0)

    print(cwd+"\img.json")
