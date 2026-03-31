from fastapi import APIRouter
from app.services.rag_service import answer_question

router = APIRouter()


@router.post("/simplify")
def simplify(data: dict):
    query = data.get("text")
    return {"data": answer_question(query)}