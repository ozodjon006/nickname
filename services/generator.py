# services/generator.py

import random

def fancy_text(text: str) -> str:
    fancy_map = {
        'a': 'ⓐ', 'b': 'ⓑ', 'c': 'ⓒ', 'd': 'ⓓ', 'e': 'ⓔ', 'f': 'ⓕ',
        'g': 'ⓖ', 'h': 'ⓗ', 'i': 'ⓘ', 'j': 'ⓙ', 'k': 'ⓚ', 'l': 'ⓛ',
        'm': 'ⓜ', 'n': 'ⓝ', 'o': 'ⓞ', 'p': 'ⓟ', 'q': 'ⓠ', 'r': 'ⓡ',
        's': 'ⓢ', 't': 'ⓣ', 'u': 'ⓤ', 'v': 'ⓥ', 'w': 'ⓦ', 'x': 'ⓧ',
        'y': 'ⓨ', 'z': 'ⓩ',
        'A': 'Ⓐ', 'B': 'Ⓑ', 'C': 'Ⓒ', 'D': 'Ⓓ', 'E': 'Ⓔ', 'F': 'Ⓕ',
        'G': 'Ⓖ', 'H': 'Ⓗ', 'I': 'Ⓘ', 'J': 'Ⓙ', 'K': 'Ⓚ', 'L': 'Ⓛ',
        'M': 'Ⓜ', 'N': 'Ⓝ', 'O': 'Ⓞ', 'P': 'Ⓟ', 'Q': 'Ⓠ', 'R': 'Ⓡ',
        'S': 'Ⓢ', 'T': 'Ⓣ', 'U': 'Ⓤ', 'V': 'Ⓥ', 'W': 'Ⓦ', 'X': 'Ⓧ',
        'Y': 'Ⓨ', 'Z': 'Ⓩ',
    }
    return ''.join(fancy_map.get(c, c) for c in text)


def generate_variants(base_word: str, style: str) -> list:
    base_word = base_word.capitalize()
    fancy = fancy_text(base_word)

    decorations = []

    if style == "male":
        frames = ["꧁༒ {} ༒꧂", "♛ {} ♛", "⚡️ {} ⚡️", "꧁༺ {} ༻꧂"]
        suffixes = ["_Vor", "_Zakon", "_Boss", "_Don", "_Gang", "_Family", "_Crew"]
        specials = ["__", "×", "~", "•", "⚔️"]
        emojis = ["💀", "🔥", "💣", "⚔️", "👑"]

        for _ in range(5):
            frame = random.choice(frames)
            suffix1 = random.choice(suffixes)
            suffix2 = random.choice(suffixes)
            emoji_seq = "".join(random.choices(emojis, k=random.randint(1, 2)))
            special = random.choice(specials)
            variant = frame.format(f"{emoji_seq}{special}{fancy}{suffix1}{suffix2}{special}{emoji_seq}")
            decorations.append(variant)

    elif style == "female":
        frames = ["꧁༺ {} ༻꧂", "♡ {} ♡", "✿ {} ✿", "♚ {} ♚"]
        suffixes = ["_Queen", "_Angel", "_Fairy", "_Gozal", "_Butterfly", "_Princess", "_Doll"]
        specials = ["__", "×", "~", "•", "✧"]
        emojis = ["👑", "💋", "✨", "🌸", "🦋", "💖"]

        for _ in range(5):
            frame = random.choice(frames)
            suffix = random.choice(suffixes)
            emoji_seq = "".join(random.choices(emojis, k=random.randint(1, 3)))
            special = random.choice(specials)
            variant = frame.format(f"{emoji_seq}{special}{fancy}{suffix}{special}{emoji_seq}")
            decorations.append(variant)

    elif style == "kids":
        frames = ["🌈 {} 🌈", "꧁༺ {} ༻꧂", "🐣 {} 🐣", "✨ {} ✨"]
        suffixes = ["_Kid", "_Junior", "_Baby", "_Little", "_Cute", "_Chibi", "_Rainbow", "_Tiny"]
        specials = ["__", "×", "~", "•", "★"]
        emojis = ["🐣", "🧸", "✨", "👶", "🌈", "🦄", "🐥"]

        for _ in range(5):
            frame = random.choice(frames)
            suffix = random.choice(suffixes)
            emoji_seq = "".join(random.choices(emojis, k=random.randint(1, 2)))
            special = random.choice(specials)
            variant = frame.format(f"{emoji_seq}{special}{fancy}{suffix}{special}{emoji_seq}")
            decorations.append(variant)

    random.shuffle(decorations)
    return decorations[:5]
