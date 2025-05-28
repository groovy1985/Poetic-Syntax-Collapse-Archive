import os
from datetime import datetime, timedelta

LOG_DIR = "logs"
OUTPUT_DIR = "note_weekly"

def collect_week_logs():
    now = datetime.now()
    week_ago = now - timedelta(days=7)
    logs = []

    files = [
        f for f in os.listdir(LOG_DIR)
        if f.endswith(".md")
    ]
    files.sort(key=lambda f: os.path.getmtime(os.path.join(LOG_DIR, f)), reverse=True)

    for fname in files:
        fpath = os.path.join(LOG_DIR, fname)
        ftime = datetime.fromtimestamp(os.path.getmtime(fpath))
        if ftime >= week_ago:
            with open(fpath, "r", encoding="utf-8") as f:
                logs.append(f.read())

    return logs

def save_note_summary(logs):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d")
    path = os.path.join(OUTPUT_DIR, f"note-{date_str}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("# Weekly Syntax Collapse Digest\n\n")
        f.write("_Generated from collapse logs collected over the past 7 days._\n\n")
        f.write("---\n\n")
