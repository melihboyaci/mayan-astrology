# Maya Astrolojisi API

Bu proje, doğum tarihinize göre Maya takvimindeki Kin numaranızı, gün burcunuzu (Nahual) ve Galaktik Tonunuzu hesaplayan bir FastAPI uygulamasıdır.

## 🌟 Özellikler

- Gregoryen takvim tarihini Maya Tzolk'in takvimine dönüştürme
- 260 günlük Maya döngüsündeki Kin numarası hesaplama
- 20 Maya gün burcu (Nahual) belirleme
- 13 Galaktik Ton hesaplama
- Detaylı Türkçe açıklamalar
- RESTful API yapısı
- Otomatik API dokümantasyonu

## 📋 Gereksinimler

- Python 3.8+
- FastAPI
- Pydantic
- Uvicorn

## 🚀 Kurulum

1. Projeyi klonlayın:

```bash
git clone <repository-url>
cd mayan-astrology
```

2. Sanal ortam oluşturun:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# veya
venv\Scripts\activate     # Windows
```

3. Gerekli paketleri yükleyin:

```bash
pip install fastapi uvicorn pydantic
```

4. Uygulamayı çalıştırın:

```bash
uvicorn app.main:app --reload
```

5. Tarayıcınızda `http://localhost:8000/docs` adresine giderek API dokümantasyonunu görüntüleyin.

## 📖 API Kullanımı

### Endpoint: `/kin-hesapla`

**Metod:** GET

**Açıklama:** Verilen doğum tarihine göre Maya Kin bilgilerini hesaplar.

#### Request Parametreleri

| Parametre  | Tip  | Zorunlu | Açıklama                             |
| ---------- | ---- | ------- | ------------------------------------ |
| birth_date | date | Evet    | Doğum tarihi (YYYY-MM-DD formatında) |

#### Request Örneği

```bash
curl -X GET "http://localhost:8000/kin-hesapla?birth_date=2000-01-01"
```

```python
import requests

response = requests.get("http://localhost:8000/kin-hesapla",
                       params={"birth_date": "2000-01-01"})
print(response.json())
```

#### Response Örneği

```json
{
  "kin_number": 260,
  "day_sign": "Ahau",
  "tone": 11,
  "day_sign_description": "Işık (veya Güneş): Aydınlanma, bütünlük, tanrısal sevgi ve ustalığın sembolüdür. Sanatsal, sevgi dolu ve evrensel bilinçle bağlantılıdır.",
  "tone_description": "Spektral Ton (On bir): Serbest bırakma, çözülme ve özgürleşmenin enerjisidir. Eskiyi bırakıp yeniliğe yer açmayı simgeler.",
  "gregorian_date": "2000-01-01"
}
```

#### Başka Bir Örnek

**Request:**

```bash
curl -X GET "http://localhost:8000/kin-hesapla?birth_date=1990-05-15"
```

**Response:**

```json
{
  "kin_number": 125,
  "day_sign": "Chicchan",
  "tone": 8,
  "day_sign_description": "Yılan: Yaşam gücü, içgüdü, hayatta kalma ve dönüşümün sembolüdür. Güçlü, karizmatik ve tutkulu bir enerjiye sahiptir.",
  "tone_description": "Galaktik Ton (Sekiz): Uyum, bütünlük ve modellemenin enerjisidir. İnançları ve eylemleri bütünleştirerek örnek olmayı temsil eder.",
  "gregorian_date": "1990-05-15"
}
```

## 🔍 Response Alanları Açıklaması

| Alan                   | Tip     | Açıklama                                                |
| ---------------------- | ------- | ------------------------------------------------------- |
| `kin_number`           | integer | 1-260 arası Kin numarası (Tzolk'in döngüsündeki gün)    |
| `day_sign`             | string  | Maya gün burcu adı (20 farklı nahual)                   |
| `tone`                 | integer | 1-13 arası Galaktik Ton                                 |
| `day_sign_description` | string  | Gün burcunun detaylı Türkçe açıklaması                  |
| `tone_description`     | string  | Galaktik Tonun detaylı Türkçe açıklaması                |
| `gregorian_date`       | string  | Hesaplamanın yapıldığı Gregoryen tarih (ISO formatında) |

## 🎯 Maya Gün Burçları (20 Nahual)

1. **Imix** - Timsah (Başlangıçlar, yaratıcılık)
2. **Ik** - Rüzgar (İletişim, ruh)
3. **Akbal** - Gece (Gizem, rüyalar)
4. **Kan** - Kertenkele (Büyüme, potansiyel)
5. **Chicchan** - Yılan (Yaşam gücü, dönüşüm)
6. **Cimi** - Ölüm (Bitişler, yeniden doğuş)
7. **Manik** - Geyik (Liderlik, zarafet)
8. **Lamat** - Tavşan (Bolluk, şans)
9. **Muluk** - Su (Duygular, sezgi)
10. **Oc** - Köpek (Sadakat, dostluk)
11. **Chuen** - Maymun (Sanat, yaratıcılık)
12. **Eb** - Yol (Yaşam yolu, kader)
13. **Ben** - Kamış (Otorite, bilgelik)
14. **Ix** - Jaguar (Şamanizm, sihir)
15. **Men** - Kartal (Vizyon, özgürlük)
16. **Cib** - Akbaba (Bilgelik, arınma)
17. **Caban** - Toprak (Dünya enerjisi, evrim)
18. **Etznab** - Bıçak (Gerçek, netlik)
19. **Cauac** - Fırtına (Değişim, yenilenme)
20. **Ahau** - Işık (Aydınlanma, ustalık)

## ⚡ 13 Galaktik Ton

1. **Manyetik** - Amaç, çekim
2. **Lunar** - Denge, meydan okuma
3. **Elektrik** - Aktivasyon, hizmet
4. **Kendi Kendine Var Olan** - Form, yapı
5. **Merkez** - Güçlendirme, komuta
6. **Ritmik** - Eşitlik, denge
7. **Rezonans** - Uyumlanma, ilham
8. **Galaktik** - Uyum, bütünlük
9. **Solar** - Niyet, gerçekleştirme
10. **Gezegensel** - Mükemmelleştirme, tezahür
11. **Spektral** - Serbest bırakma, çözülme
12. **Kristal** - İş birliği, evrenselleşme
13. **Kozmik** - Varlık, aşma

## 🛠️ Proje Yapısı

```
mayan-astrology/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI uygulaması
│   ├── models/
│   │   └── mayan.py           # Pydantic modelleri
│   ├── core/
│   │   └── calculator.py      # Maya hesaplama mantığı
│   └── data/
│       └── descriptions.json  # Türkçe açıklamalar
├── README.md
└── requirements.txt
```

## 🔧 Geliştirme

API'yi geliştirmek için:

1. Kodu değiştirin
2. `--reload` parametresi ile uvicorn otomatik olarak yeniden başlayacaktır
3. `http://localhost:8000/docs` adresinde değişiklikleri test edin

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## 🤝 Katkıda Bulunma

1. Fork'layın
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Değişikliklerinizi commit'leyin (`git commit -m 'Add some AmazingFeature'`)
4. Branch'inizi push'layın (`git push origin feature/AmazingFeature`)
5. Pull Request oluşturun

## 📞 İletişim

Sorularınız için issue açabilir veya projeyi geliştiren ekiple iletişime geçebilirsiniz.
