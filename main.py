from speech import speak,listen
from command import process_command
from ai import ask_ai
from greeting import wish
print("===========================")
print("      AURA AI ASSISTANT    ")
print("      POWERED BY GEMINI    ")
print("===========================")
print()
print('Say " Hello Aura " to wake up the voice assistant ')
while True:
    wake_word=listen()

    if wake_word and "hello aura" in wake_word.lower():
        greeting=wish()

        speak(f"{greeting}, I am Aura, How can i help you ")
        command=listen()

        speak

        if command =="":
            continue
        print("You :",command)

        if "exit" in command:
            speak("Goodbye have a nice day")
            break

        if "open youtube" in command or"open google"in command or "time" in command or "date" in command or "open notepad " in command or "open calculator" in command or "open camera" in command or "search youtube for" in command or "search" in command or "take screenshot" in command or "remember" in command or "show my notes" in command or "open" in command or "ram usage " in command or "CPU usage " in command or "open website" :
            process_command(command)

        else:
            try:

                response=ask_ai(command)
                print("Aura :",response)
                speak(response)
            except Exception as e:
                print("Error :", e)
                print("Sorry i couldn't get response from the AI")
