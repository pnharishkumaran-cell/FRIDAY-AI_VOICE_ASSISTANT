from colorama import Fore,Style,init
import sys
import time
def type_text(text,color=Fore.WHITE,delay=0.03):
    print(color,end="")
    for char in text:
        print(char,end="",flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL)
    print()



init(autoreset=True)

def friday(text):
    type_text(f"Friday :{text}",Fore.GREEN)
def user(text):
    type_text(f"user :{text}",Fore.CYAN)
def info(text):
    type_text(f"Friday:{text}",Fore.YELLOW)
def error(text):
    type_text(text,Fore.RED)