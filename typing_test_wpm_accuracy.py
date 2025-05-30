import tkinter as tk
import time, random

sentences = [
    "A journey of a thousand miles, begins with a single step.",
    "Typing fast is a useful skill.",
    "She sells seashells by the seashore, surely her success is soaring.",
    "Practice makes perfect.",
    "The expansive galaxy, with its myriad stars, holds countless mysteries."
]

start_time = 0

def start():
    global start_time
    text.set(random.choice(sentences))
    entry.delete(0, tk.END)
    result.config(text="")
    start_time = time.time()

def done():
    t = time.time() - start_time
    typed, target = entry.get(), text.get()
    wpm = len(typed.split()) / (t / 60)
    acc = sum(a==b for a, b in zip(typed, target)) / len(target) * 100
    result.config(text=f"WPM: {wpm:.1f} | Accuracy: {acc:.1f}%")

root = tk.Tk()
root.title("Typing Speed Test")

text = tk.StringVar(value="Click Start to begin.")
tk.Label(root, textvariable=text, font=("", 14), wraplength=400).pack(pady=10)

entry = tk.Entry(root, width=60, font=("", 12))
entry.pack(pady=10)

tk.Button(root, text="Start", command=start).pack()
tk.Button(root, text="Done", command=done).pack()

result = tk.Label(root, text="", font=("", 12))
result.pack(pady=10)

root.mainloop()
