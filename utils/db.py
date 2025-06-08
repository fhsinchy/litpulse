import sqlite3
from pathlib import Path

DB_PATH = Path("quote_cache.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS quotes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            quote TEXT UNIQUE,
            author TEXT,
            book TEXT
        )
    """)
    conn.commit()
    conn.close()

def quote_exists(quote: str) -> bool:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM quotes WHERE quote = ?", (quote,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def save_quote(quote: str, author: str, book: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO quotes (quote, author, book) VALUES (?, ?, ?)", (quote, author, book))
    conn.commit()
    conn.close()
