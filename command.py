import webbrowser
from datetime import datetime
import os
import pyautogui
from speech import speak
from datetime import datetime
import psutil
from ui import friday,info,error,user

apps = {
    "chrome":"chrome",
    "calculater":"calc",
    "notepad":"notepad",
    "paint":"mspaint",
    "cmd":"cmd",
    "vs code":"code",
    "file explorer":"explorer"
}
websites = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "github": "https://www.github.com",
    "chatgpt": "https://chatgpt.com",
    "instagram": "https://www.instagram.com",
    "facebook": "https://www.facebook.com",
    "linkedin": "https://www.linkedin.com",
    "amazon": "https://www.amazon.com"
}


def get_date():
    today=datetime.now().strftime("%d %B %Y")
    return f"today date is {today}"


def process_command(command):
   
    if "time" in command:
        current = datetime.now().strftime("%I:%M %p")
        friday(f"The current time is {current}")
        speak(f"The curren time is {current}")
  
    elif "date" in command:
        date=get_date()
        friday(date)
        speak(date)
    elif "search" in command:
        search=command.replace("search","").strip()
        speak(f"searching {search}")
        webbrowser.open(f"https://www.google.com/results?search_query={search} ")

    elif "take screenshot" in command:
        speak("Taking screenshot")
        screenshot=pyautogui.screenshot()
        screenshot.save("screenshot.png")
        speak("screenshot saved successfully")
    elif "remember" in command:
        note=command.replace("remember","").strip()

        with open("notes.txt","a") as file:
            file.write(note+"\n")

        speak("Okay i have saved your note")

    elif "ram usage" in command:
        ram=psutil.virtual_memory()
        used=ram.percent
        print(f"RAM usage in {used} percent")
        speak(f"RAM Usage in {used} percent")
        
    elif "cpu usage" in command:
        cpu=psutil.cpu_percent(interval=1)
        print(f"CPu usage in {cpu} percent")
        speak(f"CPU usage in {cpu} percent")

    elif "disk usage " in command or "storage" in command:
        disk=psutil.disk_usage("/")
        total=round(disk.total/(1024**3),2)
        free=round(disk.free/(1024**3),2)
        used=disk.percent
        friday(f"Disk usage in {used} percent\nTotal storage is {total} gigabytes\nFree storage is {free} gigabytes")
        speak(f"Disk usage in {used} percent\nTotal storage is {total} gigabytes\nFree storage is {free} gigabytes")


    elif command.startswith("open "):
        name = command.replace("open","").strip().lower()

        if name in apps:
            speak(f"opening {name}")
            os.system(f"start {apps[name]}")
        elif name in websites:
            speak(f"opening {name}")
            webbrowser.open(websites[name])
        else:
            friday("I don't know that application,")
            speak("I don't know that application,")
   

    elif "show my notes" in command:
        with open("notes.txt","r") as file:
            notes=file.read()

        if notes:
            speak(notes)
        else:
            speak("you have no notes")
    elif "search youtube for " in command:
        query=command.replace(f"search youtube for","").strip()
        speak(f"searching youtube for {query}")
        webbrowser.open (f"https://www.youtube.com/results?search_qeary={query} ")

    elif "open calculater" in command:
        speak("Opening calculater")
        os.system("calc")
    elif "exit" in command:
        speak("Goodbye! Have a nice day.")
        exit()
    else:
        ("ask anything")