from llm_utils import call_ollama_api
import os
from dotenv import load_dotenv
load_dotenv()

def generate_quiz(transcript_text):
    prompt = f"""Generate 3 multiple choice questions and 2 true/false questions based on the following lecture:\n\n{transcript_text}"""

    response_format = {
        "type": "json_object",
        "json_schema": {
            "name": "quiz",
            "schema": {
                "type": "object",
                "properties": {
                    "questions": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "question": {"type": "string"},
                                "options": {"type": "array", "items": {"type": "string"}},
                                "answer": {"type": "string"}
                            }
                        }
                    }
                }
            }
        }
    }

    response = call_ollama_api(
        model=os.getenv("OLLAMA_MODEL"),
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        # format_schema=response_format["json_schema"]["schema"]
    )
    
    return response
