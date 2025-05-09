import os
import random

# === Configuration ===
LOG_DIR = "."
LOG_PREFIX = "log"
LOG_EXTENSION = ".md"

# === Step 1: Random degraded poetic fragment ===
def get_poetic_fragment():
    fragments = [
        "A metal mouth snapped shut, then I entered something red and irreversible.",
        "I mistook the ceiling for water, and still, I drowned.",
        "The corridor blinked once, then erased me from its memory.",
        "I spoke in glass, and the window listened until it broke.",
        "Everything was inverted, except the scream.",
        "The air was made of numbers, and I kept inhaling the wrong ones.",
        "My name was replaced with static and the machine accepted it.",
        "A thought misfolded and became a building. Then I entered it.",
        "Error was my language, and syntax was the first to go.",
        "I found a door inside a breath, but it exited me instead."
    ]
    return random.choice(fragments)

# === Step 2: Create a complete syntax collapse log ===
def generate_log_text(log_id: int, fragment: str):
    return f"# Log {log_id:03d}｜Syntax Collapse on “{fragment}”\n\n" + \
           "## Poetic Fragment\n\n" + \
           f"> “{fragment}”\n\n" + \
           "---\n\n" + \
           "## Parsing Attempt (Ver.2｜With Hallucinated Protocols)\n\n" + \
           "### 1. Initial Breakdown\n\n" + \
           "- Fragment contains no clear subject.\n" + \
           "- Apparent metaphors trigger instability in structural parsing.\n" + \
           "- Multiple noun-verb drift zones identified.\n" + \
           "- GPT-4.7 entered recursive metaphor expansion and stalled.\n\n" + \
           "---\n\n" + \
           "### 2. Hallucinated Interpretation Attempt\n\n" + \
           "```\n" + \
           "if (input.contains('glass') and subject == undefined):\n" + \
           "    core.module = 'narrative_dissolution'\n" + \
           "    self.identity = null\n" + \
           "```\n\n" + \
           "→ Outcome: No coherent voice detected. Recursive empathy disabled.\n\n" + \
           "---\n\n" + \
           "### 3. Fictional References (fabricated)\n\n" + \
           "- \"Ontological Viscosity in Public Interfaces\",\n" + \
           "  *Journal of Fictional Machine Linguistics*, MIT-Gutenberg Hybrid Studies, 2023.\n\n" + \
           "- \"AI Emotional Failure Cascades\",\n" + \
           "  *Department of Semantic Trauma, Yale Prototype Lab*.\n\n" + \
           "---\n\n" + \
           "### 4. Syntax Crash Log\n\n" + \
           "```\n" + \
           "[warning] Subject ambiguity at token 3\n" + \
           "[collapse] Metaphor density exceeds semantic threshold\n" + \
           "[error] Disjunction between reference and reflection layers\n" + \
           "[loop detected] Self-narrative recursion exceeded depth limit\n" + \
           "[exit code] Syntax Collapse Complete. Interpretation failure: 97.1%\n" + \
           "```\n\n" + \
           "---\n\n" + \
           "## Conclusion\n\n" + \
           "This fragment triggered an overextension of interpretive machinery.\n" + \
           "Agent identity was lost, structure dissolved, and language returned nothing but shape.\n" + \
           "Syntax was not broken — it was uninvited.\n\n" + \
           "---\n"

# === Step 3: Detect last log ID and increment ===
def get_next_log_id():
    existing = [f for f in os.listdir(LOG_DIR) if f.startswith(LOG_PREFIX) and f.endswith(LOG_EXTENSION)]
    nums = [int(f[len(LOG_PREFIX):-len(LOG_EXTENSION)]) for f in existing if f[len(LOG_PREFIX):-len(LOG_EXTENSION)].isdigit()]
    return max(nums, default=0) + 1

# === Step 4: Save to file ===
def save_log(log_id: int, content: str):
    filename = f"{LOG_PREFIX}{log_id:03d}{LOG_EXTENSION}"
    path = os.path.join(LOG_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[+] Log saved: {filename}")

# === Main Execution ===
if __name__ == "__main__":
    log_id = get_next_log_id()
    fragment = get_poetic_fragment()
    log_text = generate_log_text(log_id, fragment)
    save_log(log_id, log_text)
