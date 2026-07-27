from colorama import Fore,init
int(autoreset=True)

def friday(text):
    print(Fore.GREEN + f"Friday :{text}")
def user(text):
    print(Fore.CYAN + f"user :{text}")
def info(text):
    print(Fore.YELLOW + text)
def error(text):
    print(Fore.RED + text)