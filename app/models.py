from pydantic import BaseModel, Field

# Request model
class TranslationRequest(BaseModel):
    input_str: str = Field(..., description="The English text to translate", example="Hello, how are you?")

# Response model
class TranslationResponse(BaseModel):
    translated_text: str = Field(..., description="The translated text in French", example="Bonjour, comment ça va?")
