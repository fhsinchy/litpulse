from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from utils.llm import generate_quote
from utils.image import create_image
import os

def generate_and_save(debug=False):
    quote, author, book, theme_info, raw_output = generate_quote(debug=debug)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join("media", f"quote_{timestamp}.png")

    create_image(quote, author, book, output_path)

    # Logging
    os.makedirs("logs/raw", exist_ok=True)
    with open("logs/quotes.log", "a") as log:
        log.write(f"{timestamp} | {quote} — {author} ({book}) | Theme: {theme_info}\n")

    if debug and raw_output:
        with open(f"logs/raw/{timestamp}.txt", "w") as debug_file:
            debug_file.write(raw_output)

    print(f"[{timestamp}] Generated image: {output_path}")
    return output_path

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(generate_and_save, "interval", hours=24)
    scheduler.start()

    # Run immediately on startup
    generate_and_save()
