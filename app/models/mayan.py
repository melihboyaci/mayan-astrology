from pydantic import BaseModel, Field
from datetime import date

class MayanKinResponse(BaseModel):
    kin_number: int = Field(..., example=1, description="260 günlük Tzolk'in takvimindeki Kin numarası.")
    day_sign: str = Field(..., example="Imix", description="Maya gün burcu (Nahual).")
    tone: int = Field(..., example=1, ge=1, le=13, description="Yaratılışın 13 Galaktik Tonundan biri.")
    day_sign_description: str = Field(..., example="Timsah. Başlangıçlar, yaratıcılık ve beslenme enerjisi.")
    tone_description: str = Field(..., example="Manyetik Ton. Birlik, amaç ve çekim.")
    ai_interpretation: str = Field(..., description="Yapay zeka destekli kişiselleştirilmiş Maya astrolojisi yorumu.")
    gregorian_date: date = Field(..., description="Hesaplamanın yapıldığı Gregoryen takvim tarihi.")

    class Config:
        from_attributes = True