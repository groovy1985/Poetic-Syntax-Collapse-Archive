import os
from datetime import datetime

LOG_DIR = "logs"
OUTPUT_DIR = "zine_monthly"

def collect_month_logs():
    now = datetime.now()
    logs = []

    for fname in sorted(os.listdir(LOG_DIR)):
        if not fname.endswith(".md"):
            continue
        fpath = os.path.join(LOG_DIR, fname)
        ftime = datetime.fromtimestamp(os.path.getmtime(fpath))
        if ftime.strftime("%Y-%m") == now.strftime("%Y-%m"):
            with open(fpath, "r", encoding="utf-8") as f:
                logs.append(f.read())

    return logs

def save_zine_summary(logs):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m")
    path = os.path.join(OUTPUT_DIR, f"zine-{date_str}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("# Monthly Syntax Collapse ZINE\n")
        f.write(f"_Edition: {date_str}_\n\n")
        f.write("**This collection is not meant to be read.**\n")
        f.write("**It is meant to disorient, disrupt, and dismember language.**\n\n")
        f.write("---\n\n")

        for entry in logs:
            f.write(entry)
            f.write("\n\n---\n\n")

    print(f"[+] Monthly zine summary saved: {path}")

if __name__ == "__main__":
    logs = collect_month_logs()
    if logs:
        s
