from fastapi import APIRouter
from app.schemas.legal import LegalTextRequest
from app.services.legal_service import simplify_text

router = APIRouter()

@router.post("/simplify")
def simplify(request: LegalTextRequest):
    return simplify_text(request.text)