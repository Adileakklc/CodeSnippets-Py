import random
import tkinter as tk
from tkinter import messagebox

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.configure(bg='#F5E1FD')
        
        self.words = ['python', 'tkinter', 'hangman', 'programming', 'developer', 'pycharm', 'eclipse', 'idle',
                      'jupyter', 'spyder', 'wing', 'thonny', 'syntax', 'commenting']
        self.word = random.choice(self.words)
        self.guessed_word = ["_"] * len(self.word)
        self.guesses_left = 6
        self.guessed_letters = []
        
        self.create_widgets()

    def create_widgets(self):
        # Title label
        self.title_label = tk.Label(self.root, text="Hangman Game", font=("Helvetica", 20, 'bold'), bg='#F5E1FD', fg='#5D3FD3')
        self.title_label.pack(pady=20)
        
        # Word display
        self.word_label = tk.Label(self.root, text=" ".join(self.guessed_word), font=("Helvetica", 18), bg='#F5E1FD', fg='#5D3FD3')
        self.word_label.pack(pady=10)
        
        # Input entry
        self.entry = tk.Entry(self.root, font=("Helvetica", 16))
        self.entry.pack(pady=10)
        
        # Guess button
        self.guess_button = tk.Button(self.root, text="Guess", command=self.make_guess, font=("Helvetica", 14), bg="blue", fg="white")
        self.guess_button.pack(pady=10)
        
        # Guesses left label
        self.guesses_left_label = tk.Label(self.root, text=f"Guesses left: {self.guesses_left}", font=("Helvetica", 16), bg='#F5E1FD', fg='#5D3FD3')
        self.guesses_left_label.pack(pady=10)
        
        # Guessed letters label
        self.guessed_letters_label = tk.Label(self.root, text=f"Guessed letters: {', '.join(self.guessed_letters)}", font=("Helvetica", 16), bg='#F5E1FD', fg='#5D3FD3')
        self.guessed_letters_label.pack(pady=10)

        # Exit button
        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.destroy, font=("Helvetica", 14), bg="red", fg="white")
        self.exit_button.pack(pady=10)

    def make_guess(self):
        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)
        
        if not guess or len(guess) != 1 or not guess.isalpha():
            messagebox.showerror("Invalid Input", "Please enter a single letter.")
            return
        
        if guess in self.guessed_letters:
            messagebox.showinfo("Already Guessed", "You have already guessed that letter.")
            return
        
        self.guessed_letters.append(guess)
        
        if guess in self.word:
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.guessed_word[i] = guess
        else:
            self.guesses_left -= 1
        
        self.update_display()
        self.check_game_over()

    def update_display(self):
        self.word_label.config(text=" ".join(self.guessed_word))
        self.guesses_left_label.config(text=f"Guesses left: {self.guesses_left}")
        self.guessed_letters_label.config(text=f"Guessed letters: {', '.join(self.guessed_letters)}")
    
    def check_game_over(self):
        if "_" not in self.guessed_word:
            messagebox.showinfo("Congratulations!", "You have won the game!")
            self.root.destroy()
        elif self.guesses_left == 0:
            messagebox.showinfo("Game Over", f"You have lost. The word was '{self.word}'.")
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
