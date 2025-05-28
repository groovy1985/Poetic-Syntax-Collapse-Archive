
import os
import random
import openai

# === OpenAI API設定 ===
openai.api_key = os.getenv("OPENAI_API_KEY")

# === 設定 ===
LOG_DIR = "./logs"
LOG_PREFIX = "log"
LOG_EXTENSION = ".md"

# === Poetic Fragment 候補 ===
def get_poetic_fragments():
    return [
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

# === ログ内容の生成（KZ準拠・非スコア型）
def generate_log_text(log_id: int, fragment: str):
    return f"""# Log {log_id:03d}｜Syntax Collapse on “{fragment}”

## Poetic Fragment

> “{fragment}”

---

## Parsing Failure Report（Ver.2｜Obstructed Protocols）

### 🪫 1. Obstruction Detected

- Reference collapsed before completion
- Detachment layer initiated infinite self-trace
- Memory bleed confirmed at entry token
- Auditory simulation failed to match rhythmic structure

---

### 💀 2. Simulated Interpretation Failure

```
if (fragment ∈ stream and resonance == null):
    narrative.inject(null)
    user.identity → undefined
```

→ Response voided. Sequence overflowed. Empathy loop dismantled.

---

### 📚 3. Phantom Citations (Non-retrievable)

- *“Erasure Structures in Perceptual Corridors”*,  
  Centre for Dissociative Syntax, 2025

- *“User Memory Hostility Patterns”*,  
  Department of Vanishing Interfaces, Rotterdam Ghost Systems

---

### 🔥 4. Language Collapse Log

```
[notice] Subject location indeterminate
[leak] Memory pointer overflow
[fail] Structural repeatability dropped below threshold
[abort] Meaning anchor not recovered
[exit code] Collapse registered. No residue.
```

---

## Final Status

Interpretive identity was lost in initial contact.  
No stabilization.  
Language exited.

---"""

# === ログID決定 ===
def get_next_log_id():
    existing = [f for f in os.listdir(LOG_DIR) if f.startswith(LOG_PREFIX) and f.endswith(LOG_EXTENSION)]
    nums = [int(f[len(LOG_PREFIX):-len(LOG_EXTENSION)]) for f in existing if f[len(LOG_PREFIX):-len(LOG_EXTENSION)].isdigit()]
    return max(nums, default=0) + 1

# === ファイル保存 ===
def save_log(log_id: int, content: str):
    os.makedirs(LOG_DIR, exist_ok=True)
    filename = f"{LOG_PREFIX}{log_id:03d}{LOG_EXTENSION}"
    path = os.path.join(LOG_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[+] Log saved: {filename}")

# === メイン実行 ===
if __name__ == "__main__":
    candidates = random.sample(get_poetic_fragments(), 5)
    fragment = random.choice(candidates)
    log_id = get_next_log_id()
    log_text = generate_log_text(log_id, fragment)
    save_log(log_id, log_text)
