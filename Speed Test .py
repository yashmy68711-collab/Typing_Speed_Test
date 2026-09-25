import tkinter as tk
from tkinter import messagebox
import time

sentence = "Python is a powerful programming language."

start_time = 0

# Start Test
def start_test():
    global start_time
    start_time = time.time()

# Check Result
def check_result():
    typed = entry.get()

    end_time = time.time()

    total_time = end_time - start_time

    words = len(typed.split())

    speed = round((words / total_time) * 60, 2)

    # Accuracy
    correct_chars = 0

    for i in range(min(len(typed), len(sentence))):
        if typed[i] == sentence[i]:
            correct_chars += 1

    accuracy = round(
        (correct_chars / len(sentence)) * 100,
        2
    )

    messagebox.showinfo(
        "Result",
        f"Typing Speed: {speed} WPM\nAccuracy: {accuracy}%"
    )

# Window
window = tk.Tk()
window.title("Typing Speed Test")
window.geometry("500x300")

# Title
title = tk.Label(
    window,
    text="Typing Speed Test",
    font=("Arial", 16, "bold")
)

title.pack(pady=10)

# Sentence
sentence_label = tk.Label(
    window,
    text=sentence,
    font=("Arial", 12),
    wraplength=450
)

sentence_label.pack(pady=20)

# Entry
entry = tk.Entry(window, width=50)
entry.pack(pady=10)

# Start Button
start_btn = tk.Button(
    window,
    text="Start",
    command=start_test
)

start_btn.pack(pady=5)

# Submit Button
