from ollama import Client
import os
import re
import os
from dotenv import load_dotenv

load_dotenv()

def call_ollama_api(model, messages, temperature, format_schema=None, stream=False):
    """
    Call the ollama api and return the response.
    """
    BASE_URL=os.getenv("BASE_URL")
    
    client = Client(BASE_URL)

    response = client.chat(
        model=model,
        messages=messages,
        format=format_schema,
        stream=stream,
        options={
            "temperature": temperature
        }
    )

    if stream:
        def stream_generator():
            for chunk in response:
                if isinstance(chunk, str):
                    yield chunk
                elif isinstance(chunk, dict) and "message" in chunk:
                    yield chunk["message"].get("content", "")
        return stream_generator()

    response_content = response['message']['content']
    if model == "deepseek-r1:14b":
        response_content = re.sub(r"<think>.*?</think>", "", response_content, flags=re.DOTALL)
    return response_content