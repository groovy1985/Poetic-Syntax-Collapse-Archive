import os
from datetime import datetime, timedelta

LOG_DIR = "logs"
OUTPUT_DIR = "note_summaries"

def collect_week_logs():
    now = datetime.now()
    week_ago = now - timedelta(days=7)
    logs = []
    for fname in sorted(os.listdir(LOG_DIR)):
        if not fname.endswith(".md"):
            continue
        fpath = os.path.join(LOG_DIR, fname)
        ftime = datetime.fromtimestamp(os.path.getmtime(fpath))
        if ftime >= week_ago:
            with open(fpath, "r", encoding="utf-8") as f:
                logs.append(f.read())
    return logs

def save_note_summary(logs):
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    date_str = datetime.now().strftime("%Y-%m-%d")
    path = os.path.join(OUTPUT_DIR, f"note-{date_str}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("# Weekly Syntax Collapse Digest\n\n---\n\n")
        for entry in logs:
            f.write(entry)
            f.write("\n\n---\n\n")
    print(f"[+] Weekly note summary saved: {path}")

if __name__ == "__main__":
    logs = collect_week_logs()
    if logs:
        save_note_summary(logs)
    else:
        print("[!] No logs found for the past week.")
