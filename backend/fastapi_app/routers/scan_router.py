from fastapi import APIRouter, UploadFile, File
from ..services.scanner_service import run_scan
from ..services.file_validator import validate_file

router = APIRouter(prefix="/scan")

@router.post("/")
async def scan_file(file: UploadFile = File(...)):

    validate_file(file.filename)

    content = await file.read()

    result = run_scan(content.decode())

    return {"issues": result}