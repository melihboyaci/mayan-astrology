from datetime import date
import json
from pathlib import Path


# Bu sıra standarttır ve hesaplama için kritiktir.    
TZOLKIN_DAY_SIGNS = [
    "Imix", "Ik", "Akbal", "Kan", "Chicchan", "Cimi", "Manik", "Lamat", "Muluk", "Oc", 
    "Chuen", "Eb", "Ben", "Ix", "Men", "Cib", "Caban", "Etznab", "Cauac", "Ahau"
]

# 1 Ocak 2000, Gregoryen takvimdeki başlangıç tarihi olarak kabul edilir.
# Bu tarih, Mayan takvimindeki 11. ton ve 19. işaret
REFERENCE_DATE = date(2000, 1, 1)
REFERENCE_TONE = 11
REFERENCE_SIGN_INDEX = 19
REFERENCE_KIN = 260 # 11 Ahau, 260 günlük döngünün son günüdür.

DATA_PATH = Path(__file__).parent.parent / 'data' / 'descriptions.json'

def load_descriptions():
    try:
        with open(DATA_PATH, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"day_signs": {}, "tones": {}}



def calculate_mayan_kin(birth_date: date) -> dict:
    # Args: birth_date (date): Kullanıcının doğum tarihi.
    # Returns: dict: Mayan Kin bilgisi içeren sözlük.
    
    # 1. Adım: Verilen tarih ile referans tarihi arasındaki toplam gün farkını bul.
    delta_days = (birth_date - REFERENCE_DATE).days

    # 2. Adım: Galaktik Tonu Hesapla (1-13 arası)
    # Sonuca 1 ekleriz çünkü tonlar 1-13 arasıdır, indeksler 0-12 değil.
    tone = (delta_days + REFERENCE_TONE - 1) % 13 + 1

    # 3. Adım: Gün Burcunu (Nahual) Hesapla (20 tane)
    sign_index = (delta_days + REFERENCE_SIGN_INDEX) % 20
    day_sign_name = TZOLKIN_DAY_SIGNS[sign_index]

    kin_number = (delta_days + REFERENCE_KIN - 1) % 260 + 1

    descriptions = load_descriptions()
    day_sign_description = descriptions.get("day_signs", {}).get(day_sign_name, "Açıklama bulunamadı.")
    tone_description = descriptions.get("tones", {}).get(str(tone), "Açıklama bulunamadı.")

    return {
        "kin_number": kin_number,
        "day_sign": day_sign_name,
        "tone": tone,
        "day_sign_description": day_sign_description,
        "tone_description": tone_description,
        "gregorian_date": birth_date.isoformat()
    }