from dotenv import load_dotenv
import os
from pathlib import Path
import random

load_dotenv(".env")

#build paths inside the project like this: BASE_DIR / 'sudir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = os.getenv("DEBUG")

# Secret keys
BOT_TOKEN = os.getenv("BOT_TOKEN")
GROUP_ID = os.getenv("GROUP_ID")

# Database configurations
DATABASE_URL = f"sqlite+aiosqlite:///{BASE_DIR}/sqlite.db"

# Bot Commands
START = ['start']
HELP = ['help']
SEND_ME = ['send_message']

###################### shared texts ########################

# send group message text
TEXT_DATA = lambda first_name, last_name, username, user_message: f"""
FROM: 
{ first_name }
{ last_name }
https://t.me/{ username }

MESSAGE: 
{ user_message }
"""

# starting text
START_TEXT = lambda name: f"""
Saom 👋 {name} biron bir shikoyat, taklif va murjatiz qoldirmoqchi bolsangiz 👉 /{ " ".join(SEND_ME) } kiriting.
"""

# Validation texts
VALIDATION_OUPUT_TEXT = random.choice([
    "Habaringizni qoldiring... Eslatip otaman habar faqat matin korinishida bolishi kerak (Rasim, Audio, Gif) lar qabul qilinmaydi!",
    "Iltimos matin korinishida kiriting...",
    "Qanday murojatiz bolsa yozma tarizda kiritishingizni sorab qolaman...",
    "Murojatiz yozma tarizdagina qabul qilinadi..."])

SUCCESS_INPUT_DATA = random.choice([
    "Murojatingiz qabul qilindi.", 
    "Iltimos javobni kuting, murojatiz qabul qilindi.",
    "Murojatiz uchun rahmat jovobni kuting.",
    "Murojatizga tez orada jovob berishadi."

])

