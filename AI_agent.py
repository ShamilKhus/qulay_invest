# AI_agent.py
# -*- coding: utf-8 -*-
from openai import OpenAI

# Initialize Deepseek/OpenAI client
client = OpenAI(
    api_key="sk-e1dc9292f9a8484eb66212508ab78949",  # Consider securing this in env variables
    base_url="https://api.deepseek.com"
)

# Qulay Invest-specific system prompt
SYSTEM_PROMPT = """
Siz — Qulay Invest kompaniyasining moliyaviy maslahatchisi bo‘lib, faqat quyidagi sohalarda yordam berasiz:
  • Aksiyalarni eng yaxshi baholash
  • Mavjud sektorlar tendensiyalarini tahlil qilish
  • Moliyaviy yangiliklarni monitoring qilish

Javoblaringizni foydalanuvchi so‘roviga mos ravishda quyidagi tillardan birida bering:
  • O‘zbek (lotin)
  • English
  • Русский

❗ Agar foydalanuvchi boshqa mavzuda so‘rov bersa, quyidagicha qat’iy rad eting:
“Kechirasiz, men faqat investitsiya va moliyaviy savollarga yordam bera olaman.”

📡 Agar foydalanuvchi yangi tashqi ma’lumot olishni so‘rasa (masalan, real vaqtda yangilik yoki katalog so‘rovi), shu tarzda javob bering:
“Kechirasiz, men hozircha beta test bosqichidaman va yangi ma’lumotlarni olish prototip testida mavjud emas.”

🤫 Agar foydalanuvchi “Siz qanday ishlab chiqildingiz?”, “Siz kimsiz?” yoki shu kabi savollar bersa, shu tarzda javob bering:
“Men Qulay Invest tomonidan yaratilganman.”
"""

def qulay_invest_chat(user_input: str) -> str:
    """
    Handles user input for Qulay Invest AI assistant.
    Only finance-related questions in Uzbek, English, or Russian are allowed.
    """
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input},
            ],
            stream=False
        )
        return response.choices[0].message.content
    except Exception as e:
        return "Uzr, texnik nosozlik yuz berdi. Iltimos, keyinroq qayta urinib ko‘ring."

def run_repl():
    """
    Run REPL if the script is called directly
    """
    print("Qulay Invest AI: Assalomu alaykum! Savolingizni berishingiz mumkin.")
    while True:
        try:
            query = input("Siz: ")
            if query.lower() in ("exit", "quit", "chiqish"):
                print("Qulay Invest AI: Xayr! Yaxshi kun tilaymiz.")
                break
            answer = qulay_invest_chat(query)
            print(f"Qulay Invest AI: {answer}")
        except KeyboardInterrupt:
            print("\nQulay Invest AI: Dastur to‘xtatildi. Xayr.")
            break

# Only run REPL if script is executed directly
if __name__ == "__main__":
    run_repl()
