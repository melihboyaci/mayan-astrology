from fastapi import FastAPI, Query, HTTPException
from datetime import date
from typing import Annotated
from pydantic import BaseModel

from app.core.calculator import calculate_mayan_kin
from app.models.mayan import MayanKinResponse

app = FastAPI(
    title="Maya Astrolojisi API",
    description="Doğum tarihinize göre Maya Kin ve Tzolk'in bilgilerini hesaplar ve yapay zeka destekli yorumlar sunar.",
    version="1.1.0"
)

class BirthDateRequest(BaseModel):
    birth_date: date

@app.get("/", include_in_schema=False)
async def root():
    return {"mesaj": "Maya Astrolojisi API'sine hoş geldiniz! Dokümantasyon için /docs adresini ziyaret edin."}

@app.get(
    "/kin-hesapla",
    response_model=MayanKinResponse,
    summary="Maya Kin Hesaplama (GET)",
    tags=["Astroloji"]
)
async def get_mayan_kin_get(
    birth_date: Annotated[date, Query(
        ...,
        description="Doğum tarihi (YYYY-MM-DD formatında).",
        example="2000-01-01"
    )]
):
    try:
        mayan_data = await calculate_mayan_kin(birth_date)
        return MayanKinResponse(**mayan_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post(
    "/kin-hesapla",
    response_model=MayanKinResponse,
    summary="Maya Kin Hesaplama (POST)",
    tags=["Astroloji"]
)
async def get_mayan_kin_post(request: BirthDateRequest):
    try:
        mayan_data = await calculate_mayan_kin(request.birth_date)
        return MayanKinResponse(**mayan_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))