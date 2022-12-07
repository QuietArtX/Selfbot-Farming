from flask import Flask
import colorama
from colorama import Fore
from threading import Thread


app = Flask('')


@app.route('/')

def home():

    return 'Created By QuietArt'
    

def run():

  app.run(host='0.0.0.0',port=8080)
print(f'''{Fore.GREEN}
Project Is Online & SelfBot Is Ready''')

def keep_alive():  

    t = Thread(target=run)

    t.start()
