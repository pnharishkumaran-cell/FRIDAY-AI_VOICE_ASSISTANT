from speech import speak,listen
from command import process_command
from ai import ask_ai
from greeting import wish
from colorama import Fore,Style,init
from ui import friday,user,error,info
init(autoreset=True)
print(Fore.CYAN + "=" * 50)
print(Fore.YELLOW + "          FRIDAY AI ASSISTANT")
print(Fore.GREEN + "          Powered by Gemini")
print(Fore.CYAN + "=" * 50)

print(Fore.WHITE + "\nStatus      : Ready")
print(Fore.WHITE + "Microphone : Connected")
print(Fore.WHITE + "AI         : Online")
print(Fore.WHITE + "Version    : 1.0\n")

print(Fore.MAGENTA + 'Say "Hello Friday" to wake the assistant.\n')
while True:
    wake_word=listen()

    if "hello friday" in wake_word or "hey friday" in wake_word:

        greeting=wish()

        speak(f"{greeting},How can i help you ")

        while True:

            command=listen()

            if command =="":
                continue
            user(command)

            if "exit" in command:
                speak("Goodbye have a nice day")
                exit()

            if "open youtube" in command or"open google"in command or "time" in command or "date" in command or "open notepad " in command or "open calculator" in command or "open camera" in command or "search youtube for" in command or "search" in command or "take screenshot" in command or "remember" in command or "show my notes" in command or "open" in command or "ram usage " in command or "CPU usage " in command:
                process_command(command)

            else:
                try:

                    response=ask_ai(command)
                    info(response)
                    speak(response)
                except Exception as e:
                    error(e)
                    error("Sorry i couldn't get response from the AI")
