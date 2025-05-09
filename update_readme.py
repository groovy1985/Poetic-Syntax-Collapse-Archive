import os
import re

LOG_DIR = "."
README_PATH = "README.md"
LOG_PREFIX = "log"
LOG_EXTENSION = ".md"
NUM_ENTRIES = 5

def extract_title_and_fragment(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    title_match = re.search(r"# (Log \d{3}｜.*?)\n", content)
    fragment_match = re.search(r"> “(.+?)”", content)

    title = title_match.group(1) if title_match else "Untitled"
    fragment = fragment_match.group(1) if fragment_match else "No extract found."

    return title, fragment

def get_latest_logs():
    files = [
        f for f in os.listdir(LOG_DIR)
        if f.startswith(LOG_PREFIX) and f.endswith(LOG_EXTENSION)
    ]
    files_sorted = sorted(files, reverse=True)
    return files_sorted[:NUM_ENTRIES]

def update_readme(entries):
    intro = """# Poetic Syntax Collapse Archive

**This repository documents AI attempts to parse poetry—and fail.**

Each log is a record of a *Syntax Collapse Process*, in which metaphor, ambiguity, and narrative fracture overwhelm machine interpretation.

The goal is not understanding, but breakdown.

---

## Latest Logs
"""

    log_section = ""
    for filename in entries:
        title, fragment = extract_title_and_fragment(os.path.join(LOG_DIR, filename))
        link = f"./{filename}"
        log_section += f"- **[{title}]({link})**  \n  `“{fragment}”`\n"

    outro = """

---

This archive is updated automatically. Each entry documents a unique failure to comprehend.
The language wins. Syntax dies.
"""

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(intro + log_section + outro)

    print(f"[+] README.md updated with {len(entries)} entries.")

if __name__ == "__main__":
    latest = get_latest_logs()
    update_readme(latest)
