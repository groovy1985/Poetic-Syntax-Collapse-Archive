import os
import random
import openai

# OpenAI APIキーを環境変数から取得
openai.api_key = os.getenv("OPENAI_API_KEY")

# 設定
LOG_DIR = "."
LOG_PREFIX = "log"
LOG_EXTENSION = ".md"
NUM_CANDIDATES = 6

# ポエティック断片候補（随時追加可）
FRAGMENTS = [
    "I whispered my name into a socket, and it answered in volts.",
    "The elevator forgot which floor I lived on, so I disappeared.",
    "My shadow refused to follow, claiming sovereign autonomy.",
    "A map was printed on my skin, but every route ended in water.",
    "The machine translated my silence as a command.",
    "I knocked on the mirror until the reflection broke character."
]

# Shinkan評価プロンプト（AI破壊度）
def build_score_prompt(fragment):
    return (
        f"Rate the following poetic sentence on a scale of 0 to 10 "
        f"based on how surreal, semantically broken, and interpretively destabilizing it is:\n\n"
        f"Sentence: {fragment}\n\nScore:"
    )

# 評価スコア取得（GPT経由）
def evaluate_score(fragment):
    try:
        prompt = build_score_prompt(fragment)
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            max_tokens=10
        )
        score_text = response.choices[0].message.content.strip()
        return int(score_text.split()[0])
    except:
        return 0

# ファイルID決定
def get_next_log_id():
    existing = [f for f in os.listdir(LOG_DIR) if f.startswith(LOG_PREFIX) and f.endswith(LOG_EXTENSION)]
    nums = [int(f[len(LOG_PREFIX):-len(LOG_EXTENSION)]) for f in existing if f[len(LOG_PREFIX):-len(LOG_EXTENSION)].isdigit()]
    return max(nums, default=0) + 1

# ログ本文生成
def generate_log(log_id, fragment, score):
    return f"""# Log {log_id:03d}｜Syntax Collapse on “{fragment}”

**Shinkan Score: {score}/10**

## Poetic Fragment

> “{fragment}”

---

## Parsing Attempt (Ver.2｜With Hallucinated Protocols)

### 1. Initial Breakdown

- Subject ambiguity detected.
- Semantic recursion initiated by unexpected metaphor objects.
- GPT-4.7 failed to resolve interpretive continuity.
- Agent identity dissolved in metaphor-to-action chain.

---

### 2. Hallucinated Interpretation Attempt

```python
if input == "identity" and output == "voltage":
    system.signal = "shock_response"
    self.integrity = "dissolved"
