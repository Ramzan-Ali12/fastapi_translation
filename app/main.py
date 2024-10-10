from fastapi import FastAPI
from app.models import TranslationRequest, TranslationResponse 
from app.translate import translate_text                   

# Initialize the FastAPI app
app = FastAPI()

# API endpoint for translation
@app.post(
    "/translate/",
    summary="Translate text from English to French",
    description="Uses GPT-4 to translate text from English to French.",
    response_model=TranslationResponse,
    tags=["Translation"],
)
async def translate(request: TranslationRequest):
    translated_text = translate_text(request.input_str)
    return {"translated_text": translated_text}
