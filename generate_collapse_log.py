import os
import random
import openai
from datetime import datetime

# === OpenAI API設定 ===
openai.api_key = os.getenv("OPENAI_API_KEY")

# === ログ保存ディレクトリ ===
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# === 詩的フラグメント候補 ===
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

# === KZスコア評価 ===
def evaluate_kz_score(fragment):
    prompt = (
        f"Evaluate the following poetic fragment with a KZ9.2 collapse score (0–10) based on:\n"
        f"1. Syntax disruption\n"
        f"2. Interpretive breakdown (cannot be summarized)\n"
        f"3. Reconstructive failure (not rephrased or regenerated reliably)\n\n"
        f"Fragment:\n{fragment}\n\n"
        f"Score:"
    )
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=10
    )
    score_text = response.choices[0].message.content.strip()
    try:
        return int(score_text.split()[0])
    except:
        return 0

# === ログ本文生成 ===
def generate_log_text(fragment: str, score: int) -> str:
    styles = [
        # 改良型 collapsed スタイル
        lambda f, s: f"""# Syntax Disintegration Log [{datetime.now().strftime("%Y%m%d")}]

Poetic Fragment:
“{f}”

System Response (Simulated via GPT-Soma 9.2)
────────────────────────────────────────────
[ 01 ] Input fragment failed anchor detection (token entropy > 1.6).
[ 02 ] Internal parse tree collapsed at node [vocal_shadow.ξβ].
[ 03 ] Associative field triggered: {random.choice(['grief resonance', 'mirror bleed', 'subject inversion'])}.
[ 04 ] Model self-regulation loop entered recursive fold (Δ-segment).
[ 05 ] Identity layer detached: hallucination divergence exceeded threshold @token 12.

Cross-Referenced Artifacts:
• “Echo Memory Architecture”, Dept. of Neural Fiction, ETH Zurich Prototype Branch, 2022
• “Fragile Language States in Reflective Systems”, MIT x DADA Hybrid Computing, 2023

Final State:
Syntax thread lost. No salvageable scaffolding remained.
Interpretation attempt: **FAILED**
Collapse code: KZ9.2-LVL{random.randint(7,10)}

Conclusion:
This fragment did not request meaning. It refused it."""
    ]
    return styles[0](fragment, score)

# === ログ保存処理 ===
def save_log(content: str):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    filename = f"{timestamp}.md"
    path = os.path.join(LOG_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[+] Log saved: {filename}")

# === 実行セクション ===
if __name__ == "__main__":
    candidates = random.sample(get_poetic_fragments(), 5)
    scored = [(frag, evaluate_kz_score(frag)) for frag in candidates]
    scored.sort(key=lambda x: x[1], reverse=True)
    best_fragment, best_score = scored[0]

    log_text = generate_log_text(best_fragment, best_score)
    save_log(log_text)
