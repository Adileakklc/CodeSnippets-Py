import tkinter as tk
from tkinter import ttk
import random

window = tk.Tk()
window.title("Taş, Kağıt, Makas Oyunu")
window.geometry("450x400")
window.configure(bg="#f0e4f7")

style = ttk.Style()
style.configure("TButton", font=("Arial", 12, "bold"), foreground="#ffffff", background="#c084f5", padding=10)
style.map("TButton", background=[("active", "#a653f5")])  # Etkin buton renkleri
style.configure("Score.TLabel", font=("Arial", 10, "italic"), foreground="#6a0dad")
style.configure("Result.TLabel", font=("Arial", 14, "bold"), foreground="#8b5f9a")

user_score = 0
computer_score = 0
target_score = 5

computer_choice_label = tk.Label(window, text="Bilgisayarın Seçimi: ", font=("Arial", 12), bg="#f0e4f7", fg="#663399")
computer_choice_label.pack(pady=10)

score_label = ttk.Label(window, text="Skor - Siz: 0 | Bilgisayar: 0", style="Score.TLabel")
score_label.pack(pady=10)

result_label = ttk.Label(window, text="Sonuç: ", style="Result.TLabel")
result_label.pack(pady=10)

def play(user_choice):
    global user_score, computer_score
    choices = ["Taş", "Kağıt", "Makas"]
    computer_choice = random.choice(choices)
    computer_choice_label.config(text=f"Bilgisayarın Seçimi: {computer_choice}")

    if user_choice == computer_choice:
        result = "Berabere!"
    elif (user_choice == "Taş" and computer_choice == "Makas") or \
         (user_choice == "Kağıt" and computer_choice == "Taş") or \
         (user_choice == "Makas" and computer_choice == "Kağıt"):
        result = "Kazandınız! Tebrikler 🎉"
        user_score += 1
    else:
        result = "Kaybettiniz! Bilgisayar kazandı 💻"
        computer_score += 1

    result_label.config(text=f"Sonuç: {result}")
    score_label.config(text=f"Skor - Siz: {user_score} | Bilgisayar: {computer_score}")

    if user_score == target_score:
        result_label.config(text="Oyun Bitti! Kazanan Sizsiniz 🎉")
        disable_buttons()
    elif computer_score == target_score:
        result_label.config(text="Oyun Bitti! Bilgisayar Kazandı 💻")
        disable_buttons()

def disable_buttons():
    rock_button.config(state="disabled")
    paper_button.config(state="disabled")
    scissors_button.config(state="disabled")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="Sonuç: ")
    score_label.config(text="Skor - Siz: 0 | Bilgisayar: 0")
    computer_choice_label.config(text="Bilgisayarın Seçimi: ")
    enable_buttons()  # Butonları tekrar etkinleştir

def enable_buttons():
    rock_button.config(state="normal")
    paper_button.config(state="normal")
    scissors_button.config(state="normal")


button_frame = tk.Frame(window, bg="#f0e4f7")
button_frame.pack(pady=20)

rock_button = ttk.Button(button_frame, text="Taş 🪨", style="TButton", command=lambda: play("Taş"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = ttk.Button(button_frame, text="Kağıt 📄", style="TButton", command=lambda: play("Kağıt"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = ttk.Button(button_frame, text="Makas ✂️", style="TButton", command=lambda: play("Makas"))
scissors_button.grid(row=0, column=2, padx=10)

reset_button = ttk.Button(window, text="Oyunu Sıfırla", style="TButton", command=reset_game)
reset_button.pack(pady=20)

window.mainloop()
