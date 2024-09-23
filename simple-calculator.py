import tkinter as tk
import math

# Pastel renkler tanımlama
BG_COLOR = "#FFE5EC"  # Pembe arka plan rengi
BTN_COLOR_1 = "#FFD1DC"  # Açık pembe buton rengi
BTN_COLOR_2 = "#FFB7C5"  # Daha koyu pembe
BTN_COLOR_3 = "#A7E7E8"  # Soft mavi
BTN_COLOR_4 = "#FEE9B2"  # Soft sarı
BTN_COLOR_5 = "#B3D9D9"  # Soft yeşil
BTN_EQUAL_COLOR = "#C4C8E8"  # Pastel mavi
BTN_CLEAR_COLOR = "#FF9AA2"  # Açık kırmızı

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def button_operation(operator):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + operator)

def button_dot():
    current = entry.get()
    if '.' not in current:
        entry.insert(tk.END, '.')

def button_percentage():
    current = entry.get()
    try:
        result = eval(current) / 100
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def button_sqrt():
    current = entry.get()
    try:
        result = math.sqrt(float(current))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def button_negate():
    current = entry.get()
    try:
        if current:
            if current[0] == '-':
                entry.delete(0, tk.END)
                entry.insert(0, current[1:])
            else:
                entry.delete(0, tk.END)
                entry.insert(0, '-' + current)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Pencereyi oluştur
root = tk.Tk()
root.title("Hesap Makinesi")
root.configure(bg=BG_COLOR)

# Giriş alanı (düzenlenmiş)
entry = tk.Entry(root, width=40, borderwidth=5, font=('Arial', 18), bg=BTN_COLOR_3, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Butonları tanımla
button_1 = tk.Button(root, text="1", bg=BTN_COLOR_5, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", bg=BTN_COLOR_5, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", bg=BTN_COLOR_5, command=lambda: button_click(3))

button_4 = tk.Button(root, text="4", bg=BTN_COLOR_4, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", bg=BTN_COLOR_4, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", bg=BTN_COLOR_4, command=lambda: button_click(6))

button_7 = tk.Button(root, text="7", bg=BTN_COLOR_3, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", bg=BTN_COLOR_3, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", bg=BTN_COLOR_3, command=lambda: button_click(9))

button_0 = tk.Button(root, text="0", bg=BTN_COLOR_5, command=lambda: button_click(0))
button_dot = tk.Button(root, text=".", bg=BTN_COLOR_5, command=button_dot)

button_add = tk.Button(root, text="+", bg=BTN_COLOR_2, command=lambda: button_operation("+"))
button_subtract = tk.Button(root, text="-", bg=BTN_COLOR_2, command=lambda: button_operation("-"))
button_multiply = tk.Button(root, text="*", bg=BTN_COLOR_2, command=lambda: button_operation("*"))
button_divide = tk.Button(root, text="/", bg=BTN_COLOR_2, command=lambda: button_operation("/"))

button_equal = tk.Button(root, text="=", bg=BTN_EQUAL_COLOR, command=button_equal)
button_clear = tk.Button(root, text="C", bg=BTN_CLEAR_COLOR, command=button_clear)

button_percentage = tk.Button(root, text="%", bg=BTN_COLOR_1, command=button_percentage)
button_sqrt = tk.Button(root, text="√", bg=BTN_COLOR_1, command=button_sqrt)
button_negate = tk.Button(root, text="+/-", bg=BTN_COLOR_1, command=button_negate)

# Butonları yerleştir
button_clear.grid(row=1, column=0, columnspan=2, sticky="nsew")
button_negate.grid(row=1, column=2, sticky="nsew")
button_divide.grid(row=1, column=3, sticky="nsew")

button_7.grid(row=2, column=0, sticky="nsew")
button_8.grid(row=2, column=1, sticky="nsew")
button_9.grid(row=2, column=2, sticky="nsew")
button_multiply.grid(row=2, column=3, sticky="nsew")

button_4.grid(row=3, column=0, sticky="nsew")
button_5.grid(row=3, column=1, sticky="nsew")
button_6.grid(row=3, column=2, sticky="nsew")
button_subtract.grid(row=3, column=3, sticky="nsew")

button_1.grid(row=4, column=0, sticky="nsew")
button_2.grid(row=4, column=1, sticky="nsew")
button_3.grid(row=4, column=2, sticky="nsew")
button_add.grid(row=4, column=3, sticky="nsew")

button_0.grid(row=5, column=0, sticky="nsew")
button_dot.grid(row=5, column=1, sticky="nsew")
button_percentage.grid(row=5, column=2, sticky="nsew")
button_equal.grid(row=5, column=3, sticky="nsew")

button_sqrt.grid(row=6, column=0, sticky="nsew")

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
