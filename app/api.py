# app/api.py
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import httpx

router = APIRouter()
templates = Jinja2Templates(directory="./app/templates")

@router.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/convert")
async def convert(btc: float, currency: str):
    try:
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {"ids": "bitcoin", "vs_currencies": currency}
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            data = response.json()
        rate = data["bitcoin"][currency]
        converted = btc * rate
        return {"btc": btc, "currency": currency, "converted_value": converted}
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})
