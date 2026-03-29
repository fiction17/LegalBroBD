from pydantic import BaseModel

class LegalTextRequest(BaseModel):
    text: str