import os
from datetime import datetime, timedelta

LOG_DIR = "."
OUTPUT_FILE = "note_summary.md"
DAYS_BACK = 7

def extract_valid_logs():
    files = [f for f in os.listdir(LOG_DIR) if f.startswith("log") and f.endswith(".md")]
    files.sort(reverse=True)
    recent_logs = []

    cutoff = datetime.now() - timedelta(days=DAYS_BACK)
    for fname in files:
        path = os.path.join(LOG_DIR, fname)
        mtime = datetime.fromtimestamp(os.path.getmtime(path))
        if mtime >= cutoff:
            with open(path, encoding="utf-8") as f:
                content = f.read().strip()
            if content:
                recent_logs.append((fname, content))

    return recent_logs

def generate_summary_md(logs):
    header = f"# 🗂 Weekly Syntax Collapse Digest\n\n" \
             f"Poetic fragments that evaded structure and survived interpretation.\n" \
             f"Generated: {datetime.now().strftime('%Y-%m-%d')}\n\n" \
             f"---\n\n"

    body = "\n---\n\n".join([f"## {fname.replace('.md','')}\n\n{content}" for fname, content in logs])
    return header + body

if __name__ == "__main__":
    logs = extract_valid_logs()
    if logs:
        result = generate_summary_md(logs)
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(result)
        print(f"[+] note_summary.md created with {len(logs)} logs.")
    else:
        print("[!] No logs found in past 7 days.")
