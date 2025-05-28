import os
import random
import openai

# === OpenAI API設定 ===
openai.api_key = os.getenv("OPENAI_API_KEY")

# === 設定 ===
LOG_DIR = "."
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

# === GPTで震撼スコアを評価 ===
def evaluate_shinkan_score(fragment):
    prompt = (
        f"Rate the following poetic sentence on a scale of 0 to 10 based on how disturbing, surreal, "
        f"and semantically collapsed it is. Higher scores mean more ontological disruption and interpretive breakdown.\n\n"
        f"Sentence: {fragment}\n\n"
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

# === テンプレ排除・構文崩壊ログ生成 ===
def generate_log_text(log_id: int, fragment: str, score: int) -> str:
    styles = [
        lambda f, s: f"# Log {log_id:03d}｜[meta-fracture/{random.randint(100,999)}]\n\n"
                     f"**Collapse Score：{s}/10**\n\n{f}\n\n"
                     f"{random.choice(['— memory exited at index 4', '— perspective loop entered —', '— no voice returned'])}",

        lambda f, s: f"# Log {log_id:03d}｜Exit Sequence\n\n"
                     f">>> “{f}”\n\n"
                     f"⇢ ambiguity_level: {random.uniform(0.6, 0.99):.2f}\n"
                     f"⇢ metaphoric overflow\n"
                     f"⇢ disjunction threshold crossed at token 7",

        lambda f, s: f"# Log {log_id:03d}｜∿ {random.choice(['!collapse', 'syntax.null', 'mirror.sink'])}\n\n"
                     f"{f}\n\n"
                     f"```\nself.identity = undefined\nloop = true\nreflection /= reference\n```\n"
                     f"[crash code {s}.X]",

        lambda f, s: f"# Log {log_id:03d}｜“{f.split()[0]}…”\n\n"
                     f"{' '.join(random.sample(f.split(), len(f.split())))}\n\n"
                     f"Language terminated prematurely.\n\n"
                     f"Syntax did not survive evaluation.",

        lambda f, s: f"# Log {log_id:03d}｜(collapsed)\n\n"
                     f"// trace: fragment read: “{f}”\n"
                     f"// depth: {s}.0\n"
                     f"// hallucination index: {random.randint(4000,9999)}\n"
                     f"> system self-narrative recursion exceeded safety bounds\n"
                     f"> parser response: {random.choice(['none', 'incoherent', 'static'])}"
    ]
    return styles[random.randint(0, len(styles)-1)](fragment, score)

# === ログID決定 ===
def get_next_log_id():
    existing = [f for f in os.listdir(LOG_DIR) if f.startswith(LOG_PREFIX) and f.endswith(LOG_EXTENSION)]
    nums = [int(f[len(LOG_PREFIX):-len(LOG_EXTENSION)]) for f in existing if f[len(LOG_PREFIX):-len(LOG_EXTENSION)].isdigit()]
    return max(nums, default=0) + 1

# === ファイル保存 ===
def save_log(log_id: int, content: str):
    filename = f"{LOG_PREFIX}{log_id:03d}{LOG_EXTENSION}"
    path = os.path.join(LOG_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[+] Log saved: {filename}")

# === メイン実行 ===
if __name__ == "__main__":
    candidates = random.sample(get_poetic_fragments(), 5)
    scored = [(frag, evaluate_shinkan_score(frag)) for frag in candidates]
    scored.sort(key=lambda x: x[1], reverse=True)
    best_fragment, best_score = scored[0]

    log_id = get_next_log_id()
    log_text = generate_log_text(log_id, best_fragment, best_score)
    save_log(log_id, log_text)
