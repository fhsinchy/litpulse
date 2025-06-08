import subprocess
import json
import re
from time import sleep
from utils.db import quote_exists, save_quote

def extract_first_json_block(text: str) -> str:
    match = re.search(r"\{.*?\}", text, re.DOTALL)
    return match.group(0) if match else None

def generate_quote(max_retries=5, debug=False):
    prompt_base = (
        "You are a helpful assistant trained on classic literature. Respond only in valid JSON. "
        "Generate a short, meaningful quote from a classic book. Include the quote, the full author's name, and the book title. "
        "Do not add commentary. Format:\n"
        "{\n  \"quote\": \"...\", \n  \"author\": \"...\", \n  \"book\": \"...\" \n}"
    )


    for attempt in range(max_retries):
        try:
            prompt = f"{prompt_base}\nAttempt: {attempt+1}"
            result = subprocess.run(
                ["ollama", "run", "mistral:instruct"],
                input=prompt.encode(),
                capture_output=True,
                timeout=30
            )

            output = result.stdout.decode().strip()

            # Remove markdown-style code fences
            if output.startswith("```json"):
                output = output.removeprefix("```json").strip()
            if output.endswith("```"):
                output = output.removesuffix("```").strip()

            # Extract the first JSON object
            first_json = extract_first_json_block(output)
            if not first_json:
                raise ValueError("No valid JSON block found.")

            quote_obj = json.loads(first_json)
            quote = quote_obj.get("quote", "").strip()
            author = quote_obj.get("author", "").strip()
            book = quote_obj.get("book", "").strip()

            if quote_exists(quote):
                print(f"[Cache] Skipping duplicate quote: {quote}")
                sleep(1)
                continue

            save_quote(quote, author, book)
            return quote, author, book, output if debug else None

        except Exception as e:
            print("LLM error:", e)
            print("Raw output:", result.stdout.decode().strip())
            sleep(1)

    return "To love is to act.", "Victor Hugo", "Les Misérables", None

