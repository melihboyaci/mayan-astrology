from pydantic import BaseModel, Field
from datetime import date

class MayanKinResponse(BaseModel):
    kin_number: int = Field(..., ge=1, le=260, description="Maya Kin numarası (1-260)")
    day_sign: str = Field(..., description="Maya gün burcu (Nahual)")
    tone: int = Field(..., ge=1, le=13, description="Galaktik Ton (1-13)")
    day_sign_description: str = Field(..., description="Gün burcunun detaylı açıklaması")
    tone_description: str = Field(..., description="Galaktik Tonun detaylı açıklaması")
    gregorian_date: str = Field(..., description="Hesaplamanın yapıldığı Gregoryen tarih")
    ai_interpretation: str = Field(..., description="Yapay zeka tabanlı kişisel yorum ve yaşam önerileri")

    class Config:
        from_attributes = True