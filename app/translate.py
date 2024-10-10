import openai
from fastapi import HTTPException
import os
from dotenv import load_dotenv

load_dotenv()

# Access the OpenAI API key from the environment
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables")

# Set the OpenAI API key
openai.api_key = openai_api_key

# Translation function using GPT-4
def translate_text(input_str: str) -> str:
    try:
        completion = openai.chat.completions.create(
            model="gpt-4-0125-preview",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert translator who translates text from English to French and only returns translated text."
                },
                {"role": "user", "content": input_str},
            ],
        )
        return completion.choices[0].message.content
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation error: {str(e)}")