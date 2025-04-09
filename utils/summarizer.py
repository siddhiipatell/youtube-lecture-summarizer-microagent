import os
from llm_utils import call_ollama_api
from dotenv import load_dotenv

load_dotenv()

def summarize_transcript(transcript_text):
    prompt = f"""
    Summarize the following YouTube lecture transcript into clear, organized lecture notes. Use appropriate headers and bullet points to break down the content.

    - Keep the language concise, professional, and easy to understand.
    - Group related points together under relevant headers.
    - Highlight key concepts, definitions, examples, and any important takeaways.
    - Avoid unnecessary filler or repetition from the transcript.
    
    Transcript:
    {transcript_text}

    Structure your response with the following format:
        
    Title: <title of the lecture>
    Main Topics: <main topics of the lecture>

    Summary:
    <summary of the lecture>

    """
    
    response = call_ollama_api(
        model=os.getenv("OLLAMA_MODEL"),
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
    )
    
    return response
