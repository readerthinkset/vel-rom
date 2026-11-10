"""VELOCITY ROMANIAN - language pack, brand and motion design constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OUTPUT_DIR = BASE_DIR / "output"
LESSONS_DIR = OUTPUT_DIR / "lessons"
HISTORY_DIR = OUTPUT_DIR / "history"
SCENE_DIR = BASE_DIR / "scene"

VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
FPS = 30

# ---------------------------------------------------------------- brand

BRAND = "VELOCITY ROMANIAN"
BRAND_LOCKUP_TOP = "VELOCITY"
BRAND_LOCKUP_BOTTOM = "ROMANIAN"
HANDLE = "@velocityromanian"
MASCOT_NAME = "Velo"

# ==== LANGUAGE PACK START ====
LANGUAGE = {
    "code": "ro",
    "name": "Romanian",
    "native_name": "Română",
    "history_key": "romanian",
    "english_voice": "en-US-AvaNeural",
    "english_fallback_voice": "en-US-GuyNeural",
    "native_voice": "ro-RO-EmilNeural",
    "native_fallback_voice": "ro-RO-AlinaNeural",
    "native_engine": "edge",
    "native_lang_code": "ro",
    "english_rate": "-2%",
    "native_rate": "-6%",
    "english_pitch": "+0Hz",
    "native_pitch": "+0Hz",
    "native_label": "ROMÂNĂ",
    "translit_label": "SAY IT LIKE",
    "greeting": "Bună!",
    "encouragement": "Minunat!",
    "rtl": False,
    "char_tiles": False,
    "script_font": "",
}
# ==== LANGUAGE PACK END ====

AI_MODEL = os.getenv("AI_MODEL", "gemini-fast")
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "")

# ---------------------------------------------------------------- timing (seconds)

INTRO_DURATION = 4.0
OUTRO_DURATION = 5.2
EN_CARD_IN = 0.55
GAP_EN_NATIVE = 0.5
NATIVE_CARD_LEAD = 0.35
GAP_BEFORE_REPEAT = 0.8
TAIL_HOLD = 1.4
MAX_REEL_DURATION = 88.0

# ---------------------------------------------------------------- palette

INK = "#3C3C3C"
MUTED = "#8A8A8A"
CREAM = "#FFF8E7"
GREEN = "#58CC02"
GREEN_DARK = "#46A302"
GREEN_DEEP = "#3D8F00"
BLUE = "#1CB0F6"
PURPLE = "#A560E8"
ORANGE = "#FF7A00"
RED = "#FF4B4B"
YELLOW = "#F5A700"
TEAL = "#00A889"
PINK = "#E056A0"

PALETTE = [GREEN, BLUE, PURPLE, ORANGE, RED, YELLOW, TEAL, PINK]

# ---------------------------------------------------------------- categories
# (english, native, icon, accent)

# ==== CATEGORY TABLE START ====
CATEGORY_TABLE = [
    ("Greetings", "Salutări", "hand", "#1CB0F6"),
    ("Basic Phrases", "Expresii de Bază", "chat", "#58CC02"),
    ("Common Expressions", "Expresii Comune", "chat", "#1CB0F6"),
    ("Travel", "Călătorie", "plane", "#1CB0F6"),
    ("Restaurant", "Restaurant", "fork", "#FF7A00"),
    ("Shopping", "Cumpărături", "bag", "#E056A0"),
    ("Emergency", "Urgență", "siren", "#FF4B4B"),
    ("Family Terms", "Termeni de Familie", "heart", "#E056A0"),
    ("Numbers", "Numere", "hash", "#A560E8"),
    ("Time", "Timp", "clock", "#00A889"),
    ("Motivation", "Motivație", "rocket", "#A560E8"),
    ("Love", "Dragoste", "heart", "#FF4B4B"),
    ("Success", "Succes", "trophy", "#F5A700"),
    ("Wisdom", "Înțelepciune", "book", "#A560E8"),
    ("Happiness", "Fericire", "smile", "#F5A700"),
    ("Self Improvement", "Auto-Îmbunătățire", "leaf", "#58CC02"),
    ("Gratitude", "Recunoștință", "heart", "#FF7A00"),
    ("Friendship", "Prietenie", "users", "#00A889"),
    ("Hope", "Speranță", "sun", "#FF7A00"),
    ("Creativity", "Creativitate", "palette", "#E056A0"),
    ("Inner Peace", "Pace Interioară", "lotus", "#00A889"),
    ("Confidence", "Încredere", "shield", "#1CB0F6"),
    ("Perseverance", "Perseverență", "mountain", "#FF7A00"),
    ("Inspiration", "Inspirație", "sparkles", "#A560E8"),
    ("Positive Life", "Viață Pozitivă", "sun", "#58CC02"),
    ("Courage", "Curaj", "shield", "#FF4B4B"),
    ("Kindness", "Bunătate", "heart", "#E056A0"),
    ("Patience", "Răbdare", "hourglass", "#00A889"),
    ("Forgiveness", "Iertare", "hands", "#FF7A00"),
    ("Strength", "Forță", "dumbbell", "#FF4B4B"),
    ("Joy", "Bucurie", "smile", "#F5A700"),
    ("Balance", "Echilibru", "scale", "#00A889"),
    ("Growth", "Creștere", "sprout", "#58CC02"),
    ("Purpose", "Scop", "target", "#A560E8"),
    ("Mindfulness", "Mindfulness", "lotus", "#00A889"),
    ("Daily Routine", "Rutina zilnică", "calendar", "#1CB0F6"),
    ("Weather", "Vreme", "cloud", "#1CB0F6"),
    ("Feelings", "Sentimente", "smile", "#E056A0"),
    ("Food", "Mâncare", "fork", "#FF7A00"),
    ("Health", "Sănătate", "heart", "#58CC02"),
    ("Work", "Muncă", "briefcase", "#1CB0F6"),
    ("Technology", "Tehnologie", "chip", "#A560E8"),
    ("Nature", "Natură", "leaf", "#58CC02"),
    ("Animals", "Animale", "paw", "#FF7A00"),
    ("Colors", "Culori", "palette", "#E056A0"),
    ("Directions", "Direcții", "compass", "#1CB0F6"),
    ("Body Parts", "Părți ale corpului", "hand", "#00A889"),
    ("Clothes", "Haine", "shirt", "#E056A0"),
    ("Music", "Muzică", "music", "#A560E8"),
    ("Sports", "Sport", "ball", "#FF7A00"),
    ("Holidays", "Sărbători", "gift", "#FF4B4B"),
    ("Education", "Educație", "book", "#1CB0F6"),
    ("Culture", "Cultură", "globe", "#00A889"),
    ("Finance", "Finanțe", "coin", "#58CC02"),
    ("Relationships", "Relații", "users", "#E056A0"),
]
# ==== CATEGORY TABLE END ====

CATEGORIES = [c[0] for c in CATEGORY_TABLE]
CATEGORIES_NATIVE = {c[0]: c[1] for c in CATEGORY_TABLE}
CATEGORY_META = {c[0]: {"native": c[1], "icon": c[2], "accent": c[3]} for c in CATEGORY_TABLE}
MAX_RECENT_CATEGORIES = 25

# ==== HASHTAGS START ====
HASHTAGS = [
    "#learnromanian",
    "#romanianlessons",
    "#romanianforbeginners",
    "#languagelearning",
    "#romanianvocabulary",
    "#velocityromanian",
    "#dailyromanian",
    "#romanian",
    "#learnlanguages",
    "#speakromanian",
    "#bilingual",
    "#languagetips",
]
# ==== HASHTAGS END ====
