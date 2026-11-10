"""AI phrase generation with permanent no-repeat history."""

from __future__ import annotations

import json
import random
import time
from datetime import datetime

import requests

import config
from config import CATEGORIES, CATEGORIES_NATIVE, HISTORY_DIR, MAX_RECENT_CATEGORIES

PHRASE_HISTORY_FILE = HISTORY_DIR / "all_generated_phrases.json"
RECENT_CATEGORIES_FILE = HISTORY_DIR / "recent_categories.json"

PHRASE_KEY = config.LANGUAGE["history_key"]
LANGUAGE_NAME = config.LANGUAGE["name"]
NATIVE_NAME = config.LANGUAGE["native_name"]

# ==== FALLBACK PHRASES START ====
FALLBACK_PHRASES = [
    {"english": "Hello, nice to meet you.", "native": "Bună, mi-a faci cunoștință.", "transliteration": "Buna, mi-a faci cunostinta."},
    {"english": "Thank you very much.", "native": "Mulțumesc foarte mult.", "transliteration": "Multumesc foarte mult."},
    {"english": "Good morning, have a great day.", "native": "Bună dimineața, o zi minunată.", "transliteration": "Buna dimineata, o zi minunata."},
    {"english": "I love learning new languages.", "native": "Îmi place să învăț limbi noi.", "transliteration": "Îmi place sa învăț limbi noi."},
    {"english": "Never give up on your dreams.", "native": "Nu renunța niciodată la visele tale.", "transliteration": "Nu renunța niciodată la visele tale."},
    {"english": "Every day is a fresh start.", "native": "Fiecare zi este un nou început.", "transliteration": "Fiecare zi este un nou început."},
    {"english": "Believe in yourself always.", "native": "Crede în tine întotdeauna.", "transliteration": "Crede în tine întotdeauna."},
    {"english": "Small steps lead to big changes.", "native": "Pașii mici duc la schimbări mari.", "transliteration": "Pașii mici duc la schimbări mari."},
    {"english": "You are stronger than you think.", "native": "Ești mai puternic decât crezi.", "transliteration": "Ești mai puternic decât crezi."},
    {"english": "Happiness is a choice, choose it.", "native": "Fericirea este o alegere, alege-o.", "transliteration": "Fericirea este o alegere, alege-o."},
    {"english": "What time is it please.", "native": "Ce oră este, vă rog.", "transliteration": "Ce oră este, vă rog."},
    {"english": "Where is the train station.", "native": "Unde este gara.", "transliteration": "Unde este gara."},
    {"english": "How much does this cost.", "native": "Cât costă asta.", "transliteration": "Cât costă asta."},
    {"english": "Can you help me please.", "native": "Mă puteți ajuta, vă rog.", "transliteration": "Mă puteți ajuta, vă rog."},
    {"english": "I would like a coffee please.", "native": "Aș dori o cafea, vă rog.", "transliteration": "Aș dori o cafea, vă rog."},
    {"english": "The food is delicious today.", "native": "Mâncarea este delicioasă astăzi.", "transliteration": "Mâncarea este delicioasă astăzi."},
    {"english": "Have a wonderful weekend.", "native": "Un weekend minunat.", "transliteration": "Un weekend minunat."},
    {"english": "Take care of yourself.", "native": "Ai grijă de tine.", "transliteration": "Ai grijă de tine."},
    {"english": "See you tomorrow my friend.", "native": "Pe mâine, prietene.", "transliteration": "Pe mâine, prietene."},
    {"english": "The weather is beautiful outside.", "native": "Vremea este frumoasă afară.", "transliteration": "Vremea este frumoasă afară."},
    {"english": "I am very happy today.", "native": "Sunt foarte fericit astăzi.", "transliteration": "Sunt foarte fericit astăzi."},
    {"english": "Learning a language opens new doors.", "native": "Învățarea unei limbi deschide noi uși.", "transliteration": "Învățarea unei limbi deschide noi uși."},
    {"english": "Keep practicing every single day.", "native": "Continuă să practici în fiecare zi.", "transliteration": "Continuă să practici în fiecare zi."},
    {"english": "You can achieve anything you want.", "native": "Poți realiza orice îți dorești.", "transliteration": "Poți realiza orice îți dorești."},
    {"english": "Rest when you are tired.", "native": "Odihnește-te când ești obosit.", "transliteration": "Odihnește-te când ești obosit."},
    {"english": "Focus on the positive things.", "native": "Concentrează-te pe lucrurile pozitive.", "transliteration": "Concentrează-te pe lucrurile pozitive."},
    {"english": "Learn from your mistakes.", "native": "Învață din greșelile tale.", "transliteration": "Învață din greșelile tale."},
    {"english": "Trust the process completely.", "native": "Ai încredere completă în proces.", "transliteration": "Ai încredere completă în proces."},
    {"english": "Breathe deeply and stay calm.", "native": "Respiră adânc și rămâi calm.", "transliteration": "Respiră adânc și rămâi calm."},
    {"english": "Enjoy the little moments in life.", "native": "Bucură-te de micile momente din viață.", "transliteration": "Bucură-te de micile momente din viață."},
    {"english": "Smile more, worry less.", "native": "Zâmbește mai mult, îngrijorează-te mai puțin.", "transliteration": "Zâmbește mai mult, îngrijorează-te mai puțin."},
    {"english": "Be kind to everyone you meet.", "native": "Fii amabil cu toți pe care îi întâlnești.", "transliteration": "Fii amabil cu toți pe care îi întâlnești."},
    {"english": "Help others without expecting anything back.", "native": "Ajută-i pe alții fără să aștepți nimic înapoi.", "transliteration": "Ajută-i pe alții fără să aștepți nimic înapoi."},
    {"english": "Forgive yourself and move forward.", "native": "Iartă-te și mergi mai departe.", "transliteration": "Iartă-te și mergi mai departe."},
    {"english": "Stay strong in difficult times.", "native": "Rămâi puternic în momente dificile.", "transliteration": "Rămâi puternic în momente dificile."},
    {"english": "Every moment is a new beginning.", "native": "Fiecare moment este un nou început.", "transliteration": "Fiecare moment este un nou început."},
    {"english": "Listen to your heart always.", "native": "Ascultă-ți mereu inima.", "transliteration": "Ascultă-ți mereu inima."},
    {"english": "Do what makes you happy.", "native": "Fă ceea ce te face fericit.", "transliteration": "Fă ceea ce te face fericit."},
    {"english": "Your potential is unlimited.", "native": "Potențialul tău este nelimitat.", "transliteration": "Potențialul tău este nelimitat."},
    {"english": "Be brave and take risks.", "native": "Fii curajos și asumă-ți riscuri.", "transliteration": "Fii curajos și asumă-ți riscuri."},
    {"english": "Celebrate your progress every day.", "native": "Sărbătorește-ți progresul în fiecare zi.", "transliteration": "Sărbătorește-ți progresul în fiecare zi."},
    {"english": "Surround yourself with good people.", "native": "Înconjoară-te de oameni buni.", "transliteration": "Înconjoară-te de oameni buni."},
    {"english": "Read books and grow your mind.", "native": "Citește cărți și-ți dezvoltă mintea.", "transliteration": "Citește cărți și-ți dezvoltă mintea."},
    {"english": "Travel and discover new places.", "native": "Călătorește și descoperă locuri noi.", "transliteration": "Călătorește și descoperă locuri noi."},
    {"english": "Appreciate what you already have.", "native": "Apreciază ceea ce ai deja.", "transliteration": "Apreciază ceea ce ai deja."},
    {"english": "Dance like nobody is watching.", "native": "Dansează ca și cum nimeni nu te-ar vedea.", "transliteration": "Dansează ca și cum nimeni nu te-ar vedea."},
    {"english": "Sing from your heart out loud.", "native": "Cântă din inimă tare.", "transliteration": "Cântă din inimă tare."},
    {"english": "Plant seeds of kindness everywhere.", "native": "Plantează semințe de bunătate peste tot.", "transliteration": "Plantează semințe de bunătate peste tot."},
    {"english": "Let go of what you cannot control.", "native": "Lasă din mână ceea ce nu poți controla.", "transliteration": "Lasă din mână ceea ce nu poți controla."},
    {"english": "Be present in the here and now.", "native": "Fii prezent în aici și acum.", "transliteration": "Fii prezent în aici și acum."},
]
# ==== FALLBACK PHRASES END ====


def _load_json(path, default):
    if path.exists():
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            pass
    return default


def _save_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def load_phrase_history():
    data = _load_json(PHRASE_HISTORY_FILE, {"phrases": [], "last_updated": None})
    data.setdefault("phrases", [])
    return data


def save_phrase_history(data):
    data["last_updated"] = datetime.now().isoformat()
    _save_json(PHRASE_HISTORY_FILE, data)


def is_phrase_used(english):
    english_lower = english.lower().strip()
    for p in load_phrase_history()["phrases"]:
        if p.get("english", "").lower().strip() == english_lower:
            return True
    return False


def _history_native(p):
    for key in (PHRASE_KEY, "vietnamese", "native", "translation", "target"):
        value = p.get(key)
        if value:
            return str(value)
    return ""


def add_phrases_to_history(phrases, category):
    history = load_phrase_history()
    for phrase in phrases:
        history["phrases"].append({
            "english": phrase["english"],
            PHRASE_KEY: phrase["native"],
            "transliteration": phrase.get("transliteration", ""),
            "category": category,
            "generated_at": datetime.now().isoformat(),
        })
    save_phrase_history(history)
    print(f"[content] Saved {len(phrases)} phrases (history total: {len(history['phrases'])})")


def get_available_category():
    data = _load_json(RECENT_CATEGORIES_FILE, {"recent_categories": [], "last_updated": None})
    recent = data.get("recent_categories", [])
    available = [c for c in CATEGORIES if c not in recent]
    if not available:
        recent = recent[-5:]
        available = [c for c in CATEGORIES if c not in recent]
        print("[rotation] Reset recent categories")
    selected = random.choice(available)
    recent.append(selected)
    data["recent_categories"] = recent[-MAX_RECENT_CATEGORIES:]
    data["last_updated"] = datetime.now().isoformat()
    _save_json(RECENT_CATEGORIES_FILE, data)
    print(f"[rotation] Category: {selected} ({len(available)} available)")
    return selected


def _normalize_phrase(item):
    if not isinstance(item, dict):
        return None
    english = str(item.get("english", "")).strip()
    native = str(
        item.get(PHRASE_KEY)
        or item.get("native")
        or item.get("vietnamese")
        or item.get("translation")
        or ""
    ).strip()
    translit = str(item.get("transliteration") or item.get("romanization") or item.get("romaji") or "").strip()
    if not english or not native:
        return None
    if len(english.split()) > 16:
        return None
    if "/" in native or "|" in native:
        native = native.split("/")[0].split("|")[0].strip()
    return {
        "english": english.replace("  ", " ").strip(),
        "native": native.strip(),
        "transliteration": translit.strip().strip("[]"),
    }


def _history_keys(history):
    used_en = set()
    used_nat = set()
    for p in history.get("phrases", []):
        en = str(p.get("english", "")).lower().strip()
        nat = _history_native(p).lower().strip()
        if en:
            used_en.add(en)
        if nat:
            used_nat.add(nat)
    return used_en, used_nat


def generate_phrases(category_english: str, num_phrases: int = 5) -> list:
    category_native = CATEGORIES_NATIVE[category_english]
    history = load_phrase_history()
    used_en, used_nat = _history_keys(history)
    recent_english = [
        p["english"] for p in history["phrases"] if p.get("category") == category_english
    ][-30:]

    models = [config.AI_MODEL]
    if "gemini-fast" not in models:
        models.append("gemini-fast")

    if config.POLLINATIONS_API_KEY:
        for attempt in range(5):
            model = models[0] if attempt < 3 else models[-1]
            try:
                phrases = _request_phrases(category_english, category_native, recent_english, num_phrases, attempt, model)
                unique = []
                for item in phrases:
                    p = _normalize_phrase(item)
                    if not p:
                        continue
                    key_en = p["english"].lower().strip()
                    key_nat = p["native"].lower().strip()
                    if key_en in used_en or key_nat in used_nat:
                        continue
                    if any(key_en == u["english"].lower().strip() for u in unique):
                        continue
                    used_en.add(key_en)
                    used_nat.add(key_nat)
                    unique.append(p)
                    if len(unique) >= num_phrases:
                        break
                if len(unique) >= num_phrases:
                    add_phrases_to_history(unique[:num_phrases], category_english)
                    return unique[:num_phrases]
                print(f"[content] Attempt {attempt + 1}: only {len(unique)} fresh phrases (need {num_phrases})")
            except Exception as exc:  # noqa: BLE001 - network boundary
                print(f"[content] Attempt {attempt + 1} failed ({model}): {exc}")
            time.sleep(1.5 * (attempt + 1))
    else:
        print("[content] No POLLINATIONS_API_KEY, using fallback phrases")

    fresh_fallback = []
    for p in FALLBACK_PHRASES:
        if p["english"].lower().strip() in used_en or p["native"].lower().strip() in used_nat:
            continue
        fresh_fallback.append(p)
    if not fresh_fallback:
        raise RuntimeError("Phrase API unavailable and no unused fallback phrases left; refusing to reuse phrases")
    chosen = fresh_fallback[:num_phrases]
    if len(chosen) < num_phrases:
        print(f"[content] Only {len(chosen)} fresh fallback phrases; building a shorter lesson")
    add_phrases_to_history(chosen, category_english)
    return chosen


def _request_phrases(category_english, category_native, recent_english, num_phrases, attempt, model=None):
    avoid = ""
    if recent_english:
        avoid = "\nDo NOT reuse any of these phrases:\n" + "\n".join(f"- {p}" for p in recent_english)

    prompt = f"""Create {num_phrases * 6} unique {category_english} phrases for English speakers learning {LANGUAGE_NAME}.
{avoid}

Rules:
1. Keep every phrase short and natural (4-11 words in English).
2. Use natural commas for TTS breathing pauses.
3. Each phrase must be speakable in 2-4 seconds.
4. Write clean {LANGUAGE_NAME} in {NATIVE_NAME} with correct accents and orthography. One translation only, no slashes.
5. Transliteration is a friendly Roman-script pronunciation guide for English speakers (not IPA).
6. Vary the sentence patterns and emotions. No duplicates.
7. Phrases must feel like real everyday language, not textbook filler.

Return ONLY a JSON array:
[{{"english": "...", "native": "...", "transliteration": "..."}}]"""

    response = requests.post(
        "https://gen.pollinations.ai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {config.POLLINATIONS_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": model or config.AI_MODEL,
            "messages": [
                {"role": "system", "content": f"You are a {LANGUAGE_NAME} teacher creating short, natural, varied bilingual phrases. Reply with JSON only."},
                {"role": "user", "content": prompt},
            ],
            "temperature": min(0.95 + attempt * 0.02, 1.0),
        },
        timeout=90,
    )
    response.raise_for_status()
    content = response.json()["choices"][0]["message"]["content"].strip()

    if "```json" in content:
        content = content.split("```json", 1)[1].split("```", 1)[0].strip()
    elif "```" in content:
        content = content.split("```", 1)[1].split("```", 1)[0].strip()

    start = content.find("[")
    end = content.rfind("]")
    if start >= 0 and end > start:
        content = content[start:end + 1]

    data = json.loads(content)
    if not isinstance(data, list):
        raise ValueError("AI did not return a JSON array")
    return data
