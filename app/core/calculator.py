from datetime import date
import json
from pathlib import Path
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Google AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

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

async def generate_ai_interpretation(birth_date: date, kin_number: int, day_sign: str, tone: int, day_sign_description: str, tone_description: str) -> str:
    """Generate AI-powered interpretation of Mayan astrology data."""
    
    prompt = f"""
    Sen bilge ve anlayışlı bir Maya astrolojisi uzmanısın. Sana verilen Maya astrolojisi verilerini kullanarak kişiye özel, derinlikli ve pozitif bir dille bir yorum oluştur. Bu yorumda Maya kültürünün bilgeliğini modern yaşamla harmanlayarak pratik öneriler de ver. Yorumun yaklaşık 150-200 kelime uzunluğunda olsun.

    Kişi Bilgileri:
    - Doğum Tarihi: {birth_date}
    - Kin Numarası: {kin_number} (260 günlük Tzolk'in döngüsündeki konumu)
    
    Maya Astrolojisi Verileri:
    - Gün Burcu (Nahual): {day_sign}
    - Gün Burcu Anlamı: "{day_sign_description}"
    
    - Galaktik Ton: {tone}
    - Galaktik Ton Anlamı: "{tone_description}"

    Lütfen bu verileri kullanarak:
    1. Kişinin ruhsal özelliklerini ve potansiyelini açıkla
    2. Maya bilgeliği ışığında yaşam amacını yorumla
    3. Gün burcu ve galaktik tonun nasıl birbirini desteklediğini anlat
    4. Modern yaşamda nasıl kullanabileceği pratik öneriler ver
    
    Yorumunu sıcak, destekleyici ve ilham verici bir dille yaz.
    """
    
    try:
        model = genai.GenerativeModel('gemini-2.0-flash-exp')
        response = await model.generate_content_async(prompt)
        return response.text
    except Exception as e:
        print(f"AI service error: {e}")
        # Fallback interpretation if AI service fails
        return generate_fallback_interpretation(kin_number, day_sign, tone, day_sign_description, tone_description)

def generate_fallback_interpretation(kin_number: int, day_sign: str, tone: int, day_sign_description: str, tone_description: str) -> str:
    """Fallback interpretation when AI service is unavailable."""
    
    # Kin numarası aralıklarına göre genel yorumlar
    kin_ranges = {
        (1, 65): "Başlangıç ve keşif döngüsündesiniz. Yeni deneyimlere açık olun.",
        (66, 130): "Gelişim ve büyüme döngüsündesiniz. Potansiyelinizi keşfedin.",
        (131, 195): "Dönüşüm ve değişim döngüsündesiniz. İç gücünüze güvenin.",
        (196, 260): "Ustalık ve tamamlanma döngüsündesiniz. Bilgeliğinizi paylaşın."
    }
    
    kin_interpretation = ""
    for range_tuple, interpretation in kin_ranges.items():
        if range_tuple[0] <= kin_number <= range_tuple[1]:
            kin_interpretation = interpretation
            break
    
    # Ton bazlı karakteristik yorumlar
    tone_characteristics = {
        1: "Manyetik enerjiniz sizi doğal bir lider yapar. Amaçlarınızı net belirleme yeteneğiniz güçlüdür.",
        2: "Lunar enerjiniz ile denge arayışındasınız. Zorluklarla karşılaştığınızda daha güçlü çıkarsınız.",
        3: "Elektrik enerjiniz sizi hizmet etmeye yöneltir. Başkalarına ilham verme gücünüz vardır.",
        4: "Kendi kendine var olan enerjiniz ile yapısal düşünürsünüz. Sağlam temeller oluşturmada başarılısınız.",
        5: "Merkez enerjiniz sizi güçlendirir. Komuta etme ve yönlendirme yeteneğiniz öne çıkar.",
        6: "Ritmik enerjiniz ile eşitlik yaratırsınız. Denge ve adalet duygunuz gelişmiştir.",
        7: "Rezonans enerjiniz sizi uyumlu kılar. İlham verici ve yaratıcı bir doğanız vardır.",
        8: "Galaktik enerjiniz ile bütünlük yaratırsınız. Örnek olma ve model alma yeteneğiniz güçlüdür.",
        9: "Solar enerjiniz ile niyetlerinizi gerçekleştirirsiniz. Hedeflerinize ulaşmada kararlısınız.",
        10: "Gezegensel enerjiniz ile mükemmelleştirirsiniz. Detaylara dikkat etme yeteneğiniz gelişmiştir.",
        11: "Spektral enerjiniz ile serbest bırakırsınız. Eski kalıpları kırma cesaretiniz vardır.",
        12: "Kristal enerjiniz ile iş birliği yaparsınız. Evrensel bakış açınız gelişmiştir.",
        13: "Kozmik enerjiniz ile aşarsınız. Sınırları zorlama ve ötesine geçme gücünüz vardır."
    }
    
    tone_interpretation = tone_characteristics.get(tone, "Özel bir galaktik enerjiye sahipsiniz.")
    
    # Gün burcu bazlı yaşam önerileri
    day_sign_advice = {
        "Imix": "Yaratıcı projelerinize odaklanın. Besleyici enerjinizle çevrenizdekilere destek olun.",
        "Ik": "İletişim yeteneğinizi kullanarak köprüler kurun. Ruhinizi besleyen aktivitelere zaman ayırın.",
        "Akbal": "İç sesinizi dinleyin ve sezgilerinize güvenin. Gizem dolu yolculuklar sizi bekliyor.",
        "Kan": "Potansiyelinizi keşfetmeye devam edin. Büyüme için gerekli değişimlere açık olun.",
        "Chicchan": "Yaşam gücünüzü pozitif dönüşümler için kullanın. İçsel gücünüze güvenin.",
        "Cimi": "Eski döngüleri sonlandırarak yeni başlangıçlara yer açın. Dönüşüm korkutucu değil, doğaldır.",
        "Manik": "Liderlik özelliklerinizi geliştirin. Zarafetinizle örnek olun.",
        "Lamat": "Bolluk ve şans enerjinizi paylaşın. Pozitif yaklaşımınızla çevrenizi etkileyin.",
        "Muluk": "Duygusal zekanızı kullanın. Su gibi akıcı ve uyumlu olun.",
        "Oc": "Sadakat ve dostluk bağlarınızı güçlendirin. Güvenilir yapınız size kapılar açar.",
        "Chuen": "Sanatsal yaratıcılığınızı ifade edin. Oyunbaz enerjinizle hayata renk katın.",
        "Eb": "Yaşam yolunuzda kararlılıkla ilerleyin. Kaderinizi şekillendirme gücünüz vardır.",
        "Ben": "Bilgeliğinizi ve otoritenizi sorumlu biçimde kullanın. Rehberlik yeteneğiniz gelişmiştir.",
        "Ix": "Şaman enerjinizle derin bilgilere ulaşın. Sihirli dokunuşunuzla iyileştirin.",
        "Men": "Vizyonunuzla yüksek perspektifler keşfedin. Özgürlük arayışınızı destekleyin.",
        "Cib": "Bilgeliğinizle arınma süreçlerine rehberlik edin. Derin kavrayışınız size güç verir.",
        "Caban": "Toprak enerjinizle evrimsel değişimlere destek olun. Köklü dönüşümler yaratın.",
        "Etznab": "Gerçeği görme yeteneğinizle netlik getirin. Keskin zekânızı yapıcı biçimde kullanın.",
        "Cauac": "Fırtına enerjinizle yenilenme yaratın. Değişim gücünüz çevrenizi etkiler.",
        "Ahau": "Aydınlanma enerjinizle çevrenizi aydınlatın. Ustalık yolunda ilerleyin."
    }
    
    day_advice = day_sign_advice.get(day_sign, "Özgün enerjinizle kendine has bir yol çizin.")
    
    # Genel yaşam yorumu
    life_guidance = f"""🌟 Kişisel Maya Profil Analizi:

Kin {kin_number} enerjisi taşıyorsunuz - bu size özel bir kozmik imza verir. {kin_interpretation}

{day_sign} gün burcunuzun getirdiği özellikler: {day_advice}

Galaktik Ton {tone} ile: {tone_interpretation}

🔮 Yaşam Önerisi: Maya takvimine göre, şu an evrensel enerjilerle uyum içinde yaşayabileceğiniz özel bir dönemdeysiniz. Doğal yeteneklerinizi keşfederken, spiritüel gelişiminize de odaklanın. Hem bireysel hem de toplumsal dönüşümlerde rol oynama potansiyeliniz yüksektir."""
    
    return life_guidance

async def calculate_mayan_kin(birth_date: date) -> dict:
    """Calculate Mayan Kin information for a given birth date."""
    
    # 1. Adım: Verilen tarih ile referans tarihi arasındaki toplam gün farkını bul.
    delta_days = (birth_date - REFERENCE_DATE).days

    # 2. Adım: Galaktik Tonu Hesapla (1-13 arası)
    tone = (delta_days + REFERENCE_TONE - 1) % 13 + 1

    # 3. Adım: Gün Burcunu (Nahual) Hesapla (20 tane)
    sign_index = (delta_days + REFERENCE_SIGN_INDEX) % 20
    day_sign_name = TZOLKIN_DAY_SIGNS[sign_index]

    # 4. Adım: Kin numarasını hesapla
    kin_number = (delta_days + REFERENCE_KIN - 1) % 260 + 1

    # 5. Adım: Açıklamaları yükle
    descriptions = load_descriptions()
    day_sign_description = descriptions.get("day_signs", {}).get(day_sign_name, "Açıklama bulunamadı.")
    tone_description = descriptions.get("tones", {}).get(str(tone), "Açıklama bulunamadı.")

    # 6. Adım: AI yorumu oluştur
    ai_interpretation = await generate_ai_interpretation(
        birth_date, kin_number, day_sign_name, tone, 
        day_sign_description, tone_description
    )

    return {
        "kin_number": kin_number,
        "day_sign": day_sign_name,
        "tone": tone,
        "day_sign_description": day_sign_description,
        "tone_description": tone_description,
        "ai_interpretation": ai_interpretation,
        "gregorian_date": birth_date.isoformat()
    }