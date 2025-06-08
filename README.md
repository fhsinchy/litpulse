# LitPulse – AI-Generated Literary Quote Image Bot

**LitPulse** is a fully automated Python application that generates quote images from classic literature using a local LLM, and prepares them for social media publishing.

It uses:
- `mistral:instruct` (via [Ollama](https://ollama.com)) for quote generation
- `Pillow` for image rendering
- `FastAPI` for an on-demand API
- `SQLite` to cache past quotes and prevent duplication

---

## 🚀 Features

- 🧠 **LLM-powered quote generation** with author and book name
- 🖼️ **Image creation** with elegant typography using Libre Baskerville
- 🔄 **Scheduler** generates a new quote image every 24 hours
- 🧪 **Manual API endpoint** to trigger generation on demand
- 📂 **Caching with SQLite** to avoid quote repetition
- 📜 **Debug mode** with full raw LLM output logging

---

## 📁 Project Structure

```
litpulse/
├── app/                # FastAPI and scheduler
├── utils/              # LLM, image, database helpers
├── media/              # Output images (git-ignored)
├── logs/               # Generation logs & raw LLM responses (git-ignored)
├── quote_cache.db      # SQLite cache (git-ignored)
├── LibreBaskerville.ttf
├── requirements.txt
└── README.md
```

---

## 🧑‍💻 Usage

### 1. Clone the repo and install dependencies

```bash
git clone https://github.com/yourname/litpulse.git
cd litpulse

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Download the required model via Ollama

```bash
ollama pull mistral:instruct
```

### 3. Run the app

```bash
uvicorn app.main:app --reload
```

This will:
- Start a FastAPI server
- Trigger quote generation immediately
- Run a background job every 24 hours

---

## 📲 Manual API Trigger

You can manually trigger generation via:

```bash
curl -X POST http://localhost:8000/generate-now
```

Returns:

```json
{
  "message": "Quote generated",
  "image_path": "media/quote_YYYYMMDD_HHMMSS.png"
}
```

---

## 🧠 Customization

- Change font: Replace `LibreBaskerville.ttf`
- Adjust background/font size in `utils/image.py`
- Use different models by updating `utils/llm.py`
- Add hashtags/captions/video output in future versions

---

## 📂 Git-ignored Assets

These are excluded from version control:

- `media/` – Generated images
- `logs/` – Output logs and raw LLM dumps
- `quote_cache.db` – Local SQLite cache

---

## 🛡️ License

This project uses only **free and commercially usable fonts** and LLMs. If using quotes for monetization or publication, ensure proper attribution is maintained.

---

## 📌 Coming Soon

- Special-day and theme-aware quote generation
- Video support (reel creation)
- Auto-posting to Instagram/Facebook via Meta API
- Dashboard for quote history and performance

---

## 👤 Author

Developed by Farhan Hasin Chowdhury as an AI experiment for creative automation, monetization, and skill-building.
