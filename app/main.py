from fastapi import FastAPI, Query, HTTPException
from datetime import date
from typing import Annotated

from app.core.calculator import calculate_mayan_kin
from app.models.mayan import MayanKinResponse

app = FastAPI(
    title="Maya Astrolojisi API",
    description="Doğum tarihinize göre Maya Kin ve Tzolk'in bilgilerini hesaplar.",
    version="1.0.0"
)

@app.get("/", include_in_schema=False)
async def root():
    return {"mesaj": "Maya Astrolojisi API'sine hoş geldiniz! Dokümantasyon için /docs adresini ziyaret edin."}

@app.get(
    "/kin-hesapla",
    response_model=MayanKinResponse,
    summary="Maya Kin Hesaplama",
    tags=["Astroloji"]
)
async def get_mayan_kin(
    birth_date: Annotated[date, Query(
        ...,
        description="Doğum tarihi (YYYY-MM-DD formatında).",
        example="2000-01-01"
    )]
):
    try:
        mayan_data = calculate_mayan_kin(birth_date)
        return MayanKinResponse(**mayan_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))