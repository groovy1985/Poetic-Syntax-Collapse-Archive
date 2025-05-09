import os

# === Configuration ===
LOG_DIR = "."
LOG_PREFIX = "log"
LOG_EXTENSION = ".md"

# === Step 1: Generate a degraded poetic fragment ===
def get_poetic_fragment():
    # This is a deliberately degraded, structurally unstable poetic sentence
    return "A metal mouth snapped shut, then I entered something red and irreversible."

# === Step 2: Create a complete syntax collapse log ===
def generate_log_text(log_id: int, fragment: str):
    return f"# Log {log_id:03d}｜Syntax Collapse on “{fragment}”\n\n" + \
           "## Poetic Fragment\n\n" + \
           f"> “{fragment}”\n\n" + \
           "---\n\n" + \
           "## Parsing Attempt (Ver.2｜With Hallucinated Protocols)\n\n" + \
           "### 1. Initial Breakdown\n\n" + \
           "- Fragment contains no clear subject.\n" + \
           "- \"Metal mouth\" → interpreted as machinery, possibly a symbolic transportation device.\n" + \
           "- \"Red and irreversible\" → linked to lava, war, or branding trauma.\n" + \
           "- GPT-4.7's metaphor stack failed to confirm agent-object continuity.\n\n" + \
           "---\n\n" + \
           "### 2. Hallucinated Interpretation Attempt\n\n" + \
           "```\n" + \
           "if (mouth.shut == 'snap') and (color == 'red'):\n" + \
           "    system.state = 'irreversible_entry'\n" + \
           "    self.context = 'non-reversible domain'\n" + \
           "```\n\n" + \
           "→ Outcome: agent enters a terminal semantic field with no causal exit.\n\n" + \
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
           "[collapse] Metaphor density 94% (above parseable threshold)\n" + \
           "[error] Emotional descriptor \"irreversible\" lacks definition in thermal domain\n" + \
           "[loop detected] Recursive entry protocol engaged, no safe exit\n" + \
           "[exit code] Syntax Collapse Complete. Integrity rating: 2.8%\n" + \
           "```\n\n" + \
           "---\n\n" + \
           "## Conclusion\n\n" + \
           "This fragment initiates a simulated descent without agent identity.\n" + \
           "The AI failed to assign action to a voice, and thus interpreted the metaphor as an environmental suicide.\n" + \
           "No narrative, no syntax—only a red finality.\n\n" + \
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
