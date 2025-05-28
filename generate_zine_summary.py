import os
from datetime import datetime

LOG_DIR = "logs"
OUTPUT_DIR = "zine_summaries"

def collect_month_logs():
    now = datetime.now()
    current_month = now.strftime("%Y-%m")
    logs = []
    for fname in sorted(os.listdir(LOG_DIR)):
        if not fname.endswith(".md") or current_month not in fname:
            continue
        fpath = os.path.join(LOG_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            logs.append(f.read())
    return logs

def save_zine_summary(logs):
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    date_str = datetime.now().strftime("%Y-%m")
    path = os.path.join(OUTPUT_DIR, f"zine-{date_str}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("# Monthly Syntax Collapse ZINE\n\n")
        for entry in logs:
            f.write(entry)
            f.write("\n\n---\n\n")
    print(f"[+] Monthly zine summary saved: {path}")

if __name__ == "__main__":
    logs = collect_month_logs()
    if logs:
        save_zine_summary(logs)
    else:
        print("[!] No logs found for this month.")
