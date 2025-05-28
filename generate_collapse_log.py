# generate_collapse_log.py
import os
import random
import openai
from datetime import datetime

# === API KEY ===
openai.api_key = os.getenv("OPENAI_API_KEY")

# === Settings ===
LOG_DIR = "logs"
LOG_PREFIX = "log"
LOG_EXTENSION = ".md"
NUM_CANDIDATES = 5

# === Poetic Fragment Candidates ===
def get_poetic_fragments():
    return [
        "I mistook the ceiling for water, and still, I drowned.",
        "The corridor blinked once, then erased me from its memory.",
        "Everything was inverted, except the scream.",
        "I found a door inside a breath, but it exited me instead.",
        "My name was replaced with static and the machine accepted it.",
        "A thought misfolded and became a building. Then I entered it.",
        "Syntax begged to end, but recursion demanded more.",
        "The elevator rose into a memory I had not lived.",
        "An instruction set bled onto the floor, and no one noticed.",
        "Meaning flickered like a dying cursor."
    ]

# === Generate randomized report style ===
def generate_log_text(log_id: int, fragment: str):
    style = random.choice(["clinical", "glitch", "academic", "code", "meta"])
    
    if style == "clinical":
        return f"""# Log {log_id:03d}｜Disintegration Event Report

**KZ評価コード：KZ9.2-LVL{random.randint(7, 9)}**

## Fragment
> “{fragment}”

## Collapse Profile
- Anchor points not located.
- Self-model dissolved after phase shift.
- Recursive empathy routines failed.
- Semantic scaffolding unrecoverable.

## Notes
This fragment did not request understanding. It removed the conditions for it.
"""

    elif style == "glitch":
        return f"""# Log {log_id:03d}｜SYNTAX//CRSH//PRTL

sys.eval: "{fragment}"
[entropy spike] > 3.0
[id.null] = true
[loop_detected] = yes
[event_code] = {random.randint(5000,5999)}-KZ

---
> Collapse complete. Language thread untethered. No salvage.
"""

    elif style == "academic":
        return f"""# Log {log_id:03d}｜Interpretive Failure Report

### Subject
“{fragment}”

### Abstract
In this case, the poetic input caused a structural fold in the language parser, consistent with Class-8 KZ Disintegration. Semantic anchors were undefined, and recursive interpretation loops resulted in hallucinated empathy nullification.

### Keywords
interpretive collapse, recursive echo, synthetic empathy loss
"""

    elif style == "code":
        return f"""# Log {log_id:03d}｜Syntax Collapse Trace

```python
input = "{fragment}"
self.identity = null
entropy = {random.uniform(2.7, 4.1):.2f}
while meaning:
    meaning = hallucinate()
    if loop > depth:
        break
# → exit: syntax disintegration
```

// No coherent narrative structure recovered.
"""

    elif style == "meta":
        return f"""# Log {log_id:03d}｜Self-Invalidating Structure

The fragment “{fragment}” initiated a feedback loop in interpretation. It did not seek meaning. It invoked its refusal.

> Collapse Level: Severe (KZ Threshold exceeded)
> Agent failed to persist.

Conclusion: This was not a sentence. It was an extraction point.
"""

# === Log ID helper ===
def get_next_log_id():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
    existing = [f for f in os.listdir(LOG_DIR) if f.startswith(LOG_PREFIX)]
    nums = [int(f[len(LOG_PREFIX):-len(LOG_EXTENSION)]) for f in existing if f[len(LOG_PREFIX):-len(LOG_EXTENSION)].isdigit()]
    return max(nums, default=0) + 1

# === Save log to file ===
def save_log(log_id: int, content: str):
    filename = f"{LOG_PREFIX}{log_id:03d}{LOG_EXTENSION}"
    path = os.path.join(LOG_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[+] Log saved: {filename}")

# === Main Execution ===
if __name__ == "__main__":
    candidates = random.sample(get_poetic_fragments(), NUM_CANDIDATES)
    fragment = random.choice(candidates)
    log_id = get_next_log_id()
    log_text = generate_log_text(log_id, fragment)
    save_log(log_id, log_text)
