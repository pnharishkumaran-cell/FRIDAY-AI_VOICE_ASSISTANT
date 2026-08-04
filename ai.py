from google import genai
from dotenv import load_dotenv
import os
load_dotenv()

client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

conversation_memory=[]


def ask_ai(command):
    global conversation_memory

    conversation_memory.append(f"user:{command}")

    if len(conversation_memory) >10:
        conversation_memory=conversation_memory[-10]

    prompt = f"""
    You are Friday, a smar voice assistant. you are created by author named harish
    Rules:
    -Give short and natural replies.
    -Maximum 2-3 sentence.
    -do not use bullet points
    -Do not explain unlass ask
    -If the answer is yes or no answer in one sentence.
    -Speak like a real assistant.
    -Reply naturally
    -Dont say "what you like to know"
    -Dont introduce yourself unless ask
    conversation:
    {chr(10).join(conversation_memory)}


    user:{command}
    """
    


    response=client.models.generate_content(

    
        model="gemini-2.5-flash",
        contents=prompt
    )
    return (response.text)