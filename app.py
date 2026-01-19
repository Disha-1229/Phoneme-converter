import tkinter as tk
from tkinter import scrolledtext

PHONEME_MAP = {
    "ð": "th", "θ": "th", "ʃ": "sh", "ʒ": "zh",
    "tʃ": "ch", "dʒ": "j", "ŋ": "ng", "æ": "a",
    "ə": "a", "ɜ": "er", "ɪ": "i", "iː": "ee",
    "ɑː": "a", "ɔː": "o", "ʊ": "u", "uː": "oo",
    "eɪ": "ay", "aɪ": "i", "oʊ": "o", "aʊ": "ow",
    "ɔɪ": "oy", "ɒ": "o"
}

IPA_SYMBOLS = list(PHONEME_MAP.keys())
IPA_SYMBOLS.sort(key=len, reverse=True)

def ipa_to_english(text: str) -> str:
    text = text.strip()
    result = []
    i = 0
    n = len(text)
    while i < n:
        if text[i] == "ː":
            i += 1
            continue
        matched = False
        for symbol in IPA_SYMBOLS:
            if text.startswith(symbol, i):
                result.append(PHONEME_MAP[symbol])
                i += len(symbol)
                matched = True
                break
        if not matched:
            result.append(text[i])
            i += 1
    return "".join(result)

def insert_symbol(symbol: str):
    input_box.insert(tk.END, symbol)

def convert():
    ipa = input_box.get("1.0", tk.END)
    output = ipa_to_english(ipa)
    result_box.config(state=tk.NORMAL)
    result_box.delete("1.0", tk.END)
    result_box.insert("1.0", output)
    result_box.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Phoneme Converter")

tk.Label(root, text="Enter IPA:", font=("Arial", 12)).pack(pady=3)
input_box = scrolledtext.ScrolledText(root, width=40, height=4, font=("Arial", 14))
input_box.pack(pady=5)
keyboard_frame = tk.Frame(root)
keyboard_frame.pack(pady=10)

for sym in PHONEME_MAP:
    tk.Button(keyboard_frame, text=sym, width=3, command=lambda s=sym: insert_symbol(s)).pack(side=tk.LEFT, padx=2)

tk.Button(root, text="Convert", width=15, command=convert).pack(pady=10)
tk.Label(root, text="Output:", font=("Arial", 12)).pack()
result_box = scrolledtext.ScrolledText(root, width=40, height=4, font=("Arial", 14), state=tk.DISABLED)
result_box.pack(pady=5)

root.mainloop()
