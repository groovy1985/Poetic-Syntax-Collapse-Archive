import os
from datetime import datetime, timedelta

LOG_DIR = "."
OUTPUT_FILE = "zine_summary.md"
DAYS_BACK = 30

def extract_valid_logs():
    files = [f for f in os.listdir(LOG_DIR) if f.startswith("log") and f.endswith(".md")]
    files.sort()
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

def generate_zine_md(logs):
    title = f"# 📘 Monthly ZINE Export｜Collapse Anthology\n\n" \
            f"Fragments selected from last 30 days.\n" \
            f"Date: {datetime.now().strftime('%Y-%m-%d')}\n\n"

    body = "\n\n".join([
        f"---\n\n## {fname.replace('.md','')}\n\n{content}"
        for fname, content in logs
    ])
    return title + body

if __name__ == "__main__":
    logs = extract_valid_logs()
    if logs:
        result = generate_zine_md(logs)
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(result)
        print(f"[+] zine_summary.md created with {len(logs)} logs.")
    else:
        print("[!] No logs found in past 30 days.")
