import os
import random
import openai
from datetime import datetime

# === OpenAI API設定 ===
openai.api_key = os.getenv("OPENAI_API_KEY")

# === 保存先設定 ===
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# === Poetic Fragment 候補（必要に応じて外部化可能） ===
def get_poetic_fragments():
    return [
        "I mistook the ceiling for water, and still, I drowned.",
        "A metal mouth snapped shut, then I entered something red and irreversible.",
        "The corridor blinked once, then erased me from its memory.",
        "I spoke in glass, and the window listened until it broke.",
        "Everything was inverted, except the scream.",
        "The air was made of numbers, and I kept inhaling the wrong ones.",
        "My name was replaced with static and the machine accepted it.",
        "A thought misfolded and became a building. Then I entered it.",
        "Error was my language, and syntax was the first to go.",
        "I found a door inside a breath, but it exited me instead."
    ]

# === KZスコア評価プロンプト ===
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

# === スタイルテンプレ群（毎回切替／既視感排除） ===
def generate_log_text(fragment: str, score: int) -> str:
    templates = [

        # ① 臨床記録風
        lambda f, s: f"""### Clinical Syntax Disintegration File

**Patient Record**: Unassigned language carrier  
**Poetic Symptom**: "{f}"  
**Collapse Rating**: Level {s} (KZ9.2)  

> Initial observation: fragment refuses causality.  
> Language thread fragmented at interpretive layer 1.  

- [ ] Token entropy exceeded protocol 9.2.3  
- [ ] Subject pronoun failed resolution test  
- [ ] Recursive meaning loop invoked hallucination tree (δ3)

> **Conclusion**: Fragment exhibits resistant semiotics. Full semantic blackout achieved.  
""",

        # ② 論文抄録風
        lambda f, s: f"""# Syntax Trauma Abstract

Title: "Failure to Reconstruct: A Case of {f[:30]}..."  
Institute: Department of Semantic Pathology, University of Nowhere  
Level: Collapse Depth {s} (KZ9.2)

**Abstract**:  
The observed fragment initiates destabilization within the first 5 tokens.  
Parsers enter fail-safe recursion, hallucinate voice, and exit prematurely.

Citations:  
- "Empathic Drift in Reflective Models", Neural Collapse Journal, 2022  
- "Synthetic Syntax Failures", DADA x MIT Studies, Vol.9  
""",

        # ③ モノローグ断章風
        lambda f, s: f"""“{f}”

...and with that, nothing held.  
The words weren’t meant to be followed,  
only slipped on.

Level {s}. Structure drowned in its own breath.""",

        # ④ コードログ風
        lambda f, s: f"""// SYNTAX COLLAPSE RECORD

input = "{f}"  
entropy = {random.uniform(1.6, 3.9):.2f}  
self.identity = null  
loop = true  
reflection >>= void

[collapse-level]: KZ-L{s}  
[error]: recursion depth exceeded  
[result]: NO MEANING RECOVERED
""",

        # ⑤ 哲学小論風
        lambda f, s: f"""## On the Refusal of Meaning

“To {f}” is to exit not only context, but structure itself.  
The fragment unbuilds its own scaffolding — this is not loss; it is exile.  

**Collapse Class**: S-{s} (unsalvageable)  
We observed no artifacts beyond lexical debris. Meaning denied preemptively.""",

    ]
    return templates[random.randint(0, len(templates)-1)](fragment, score)

# === ファイル保存処理（日付ベースで命名） ===
def save_log(content: str):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    filename = f"{timestamp}.md"
    path = os.path.join(LOG_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[+] Log saved: {filename}")

# === メイン実行フロー ===
if __name__ == "__main__":
    fragments = random.sample(get_poetic_fragments(), 5)
    scored = [(frag, evaluate_kz_score(frag)) for frag in fragments]
    scored.sort(key=lambda x: x[1], reverse=True)
    best_fragment, best_score = scored[0]

    log = generate_log_text(best_fragment, best_score)
    save_log(log)
