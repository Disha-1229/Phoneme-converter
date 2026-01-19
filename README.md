
# Phoneme Converter (Tkinter GUI)

A simple Python tool that converts phonetic symbols (like IPA) to rough English representations or other mapped outputs.

---

## ✨ Features

- GUI built using Tkinter
- Phoneme → English or mapped output
- On-screen phoneme keyboard
- Scrollable text input + output fields
- Beginner-friendly & pure Python
- Great for linguistics/demo/mini-projects

---

## 🧩 Installation

Clone the repository:

```bash
git clone https://github.com/<username>/phoneme-converter.git
cd phoneme-converter
```

Install dependencies:

```bash
pip install -r requirements.txt
```

On Linux, ensure Tk is installed:

```bash
sudo apt-get install python3-tk
```

---

## ▶️ Usage

Run the application:

```bash
python src/app.py
```

---

## 🔧 How It Works

- Phonemes are mapped using `PHONEME_MAP`
- Longest-symbol matching ensures correct mapping
- Length marker `ː` is ignored
- Optional future extensions possible

---

## 📜 License

MIT License
