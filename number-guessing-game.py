import tkinter as tk
import random

# Arayüz oluşturma
def number_guessing_game():
    def check_guess():
        try:
            guess = int(entry.get())
            if guess < 0 or guess > 50:
                result_label.config(text="Hey, I picked a number between 0 and 50! 😊", fg="#FFD700")
            elif guess < number_to_guess:
                result_label.config(text="Hmmm... You can go a higher! 🚀", fg="#FF10F0")
            elif guess > number_to_guess:
                result_label.config(text="Ooo, you're flying too high! 🌥", fg="#FF10F0")
            else:
                result_label.config(text=f"Bingo! {number_to_guess} was the number I picked! 🎉", fg="#39FF14")
        except ValueError:
            result_label.config(text="I'm waiting for you to enter a number, let the digits do the talking! 🔢", fg="#FF10F0")

    # Pencere ayarları
    window = tk.Tk()
    window.title("Number Guessing Game")
    window.geometry("700x300")
    window.config(bg="#2A2A2A")

    # Başlık
    title_label = tk.Label(window, text="Number Guessing Game", font=("Helvetica", 18), bg="#8D3DAF", fg="#FFFFFF")
    title_label.pack(pady=20)

    # Tahmin girişi
    entry_label = tk.Label(window, text="Enter your guess (0-50):", font=("Helvetica", 14), bg="#2A2A2A", fg="#FFFFFF")
    entry_label.pack(pady=10)

    entry = tk.Entry(window, font=("Helvetica", 14), bg="#FFFFFF", fg="#2A2A2A")
    entry.pack(pady=10)

    # Kontrol butonu
    check_button = tk.Button(window, text="Check", font=("Helvetica", 14), bg="#8D3DAF", fg="#2A2A2A", command=check_guess)
    check_button.pack(pady=10)

    # Sonuç etiketi
    result_label = tk.Label(window, text="", font=("Helvetica", 14), bg="#2A2A2A", fg="#FFFFFF")
    result_label.pack(pady=10)

    # Rastgele sayı
    number_to_guess = random.randint(0, 50)

    window.mainloop()

# Oyunu başlat
number_guessing_game()
