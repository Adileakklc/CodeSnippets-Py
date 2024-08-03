import random
import tkinter as tk
from tkinter import ttk

class DiceSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Simulator")
        
        # Set the root background color
        self.root.configure(bg='#F5E1FD')
        
        # Create a style for the buttons
        style = ttk.Style()
        style.configure('TButton', font=('Helvetica', 14), padding=10)
        
        # Welcome label
        self.label = tk.Label(root, text="Welcome to the Dice Simulator!", font=("Helvetica", 20, 'bold'), bg='#F5E1FD', fg='#5D3FD3')
        self.label.pack(pady=20)
        
        # Roll button
        self.roll_button = ttk.Button(root, text="Roll the Dice", command=self.roll_dice, style='TButton')
        self.roll_button.pack(pady=10)
        
        # Result label
        self.result_label = tk.Label(root, text="", font=("Helvetica", 18), bg='#F5E1FD', fg='#5D3FD3')
        self.result_label.pack(pady=20)
        
        # Exit button
        self.exit_button = ttk.Button(root, text="Exit", command=self.exit_program, style='TButton')
        self.exit_button.pack(pady=10)
    
    def roll_dice(self):
        result = random.randint(1, 6)
        self.result_label.config(text=f"You rolled a {result}!")
    
    def exit_program(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = DiceSimulator(root)
    root.mainloop()
