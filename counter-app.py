import tkinter as tk
from tkinter import ttk

class CounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Counter App")
        self.root.geometry("300x300")
        self.root.configure(bg='#F5E1FD')
        
        # Initialize counter
        self.counter = 0
        
        # Create a style for the widgets
        style = ttk.Style()
        style.configure('TLabel', font=('Helvetica', 20), background='#F5E1FD', foreground='#5D3FD3')
        style.configure('TButton', font=('Helvetica', 14), padding=10)
        
        # Counter label
        self.counter_label = ttk.Label(self.root, text=str(self.counter), style='TLabel')
        self.counter_label.pack(pady=20)
        
        # Increment button
        self.increment_button = ttk.Button(self.root, text="Increment", command=self.increment, style='TButton')
        self.increment_button.pack(pady=5)
        
        # Decrement button
        self.decrement_button = ttk.Button(self.root, text="Decrement", command=self.decrement, style='TButton')
        self.decrement_button.pack(pady=5)
        
        # Reset button
        self.reset_button = ttk.Button(self.root, text="Reset", command=self.reset, style='TButton')
        self.reset_button.pack(pady=5)
    
    def increment(self):
        self.counter += 1
        self.update_counter_label()
    
    def decrement(self):
        self.counter -= 1
        self.update_counter_label()
    
    def reset(self):
        self.counter = 0
        self.update_counter_label()
    
    def update_counter_label(self):
        self.counter_label.config(text=str(self.counter))

if __name__ == "__main__":
    root = tk.Tk()
    app = CounterApp(root)
    root.mainloop()
