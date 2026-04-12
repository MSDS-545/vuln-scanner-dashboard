from fastapi import APIRouter
from ..services.report_service import generate_json_report

router = APIRouter(prefix="/report")

@router.get("/")
def report():

    return generate_json_report()