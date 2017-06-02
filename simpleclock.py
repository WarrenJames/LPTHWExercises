# Simple Clock
import os
from datetime import datetime
now = datetime.now()

def ct():
    time = datetime.now()
    clear()
    return time



def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def clock():
    while True:
        print ct()



clock()
