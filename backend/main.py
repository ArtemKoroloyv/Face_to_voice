from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pathlib import Path
import uuid

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = Path(__file__).resolve().parent
IMAGES_DIR = BASE_DIR / "storage" / "images"
TEXTS_DIR = BASE_DIR / "storage" / "texts"

IMAGES_DIR.mkdir(parents=True, exist_ok=True)
TEXTS_DIR.mkdir(parents=True, exist_ok=True)

MAX_TEXT_LEN = 5000
MAX_FILE_SIZE = 25 * 1024 * 1024  # 25 МБ
ALLOWED_CONTENT_TYPES = {"image/jpeg", "image/png"}


@app.post("/submit")
async def submit(
    text: str = Form(...),
    image: UploadFile = File(...),
):
    if not text.strip():
        raise HTTPException(status_code=400, detail="Текст обязателен")
    if len(text) > MAX_TEXT_LEN:
        raise HTTPException(status_code=400, detail="Текст слишком длинный")

    if image.content_type not in ALLOWED_CONTENT_TYPES:
        raise HTTPException(status_code=400, detail="Допустимы только JPG и PNG")

    file_bytes = await image.read()
    if len(file_bytes) > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="Файл слишком большой (макс 25 МБ)")

    submission_id = uuid.uuid4().hex

    if image.content_type == "image/png":
        ext = ".png"
    else:
        ext = ".jpg"

    image_path = IMAGES_DIR / f"{submission_id}{ext}"
    text_path = TEXTS_DIR / f"{submission_id}.txt"

    image_path.write_bytes(file_bytes)
    text_path.write_text(text, encoding="utf-8")

    await image.close()

    return JSONResponse(
        {
            "status": "ok",
            "id": submission_id,
            "message": "Данные сохранены",
        }
    )
