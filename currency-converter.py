import tkinter as tk
from tkinter import ttk
import requests

# Döviz kurunu almak için API'yi çağırıyoruz
def get_exchange_rate(from_currency, to_currency):
    try:
        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(url)
        data = response.json()

        if 'rates' in data:
            if to_currency in data['rates']:
                return data['rates'][to_currency]
            else:
                return None
        else:
            print("API yanıtında 'rates' anahtarı bulunamadı.")
            return None
    except Exception as e:
        print(f"API çağrısı başarısız: {e}")
        return None

# Çevirme işlemi
def convert():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()

        exchange_rate = get_exchange_rate(from_currency, to_currency)
        if exchange_rate:
            converted_amount = amount * exchange_rate
            result_label.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}", fg="#1abc9c")
        else:
            result_label.config(text="Kur bulunamadı!", fg="#e74c3c")
    except ValueError:
        result_label.config(text="Geçerli bir miktar girin!", fg="#e74c3c")

# Ana pencere
root = tk.Tk()
root.title("Döviz Çevirici")
root.geometry("480x420")
root.configure(bg='#1e272e')

# Gradient arka plan efekti vermek için Canvas kullanımı
canvas = tk.Canvas(root, width=480, height=420, bg='#1e272e', highlightthickness=0)
canvas.create_rectangle(0, 0, 480, 420, fill='#2f3640', outline='')
canvas.place(x=0, y=0)

# Yazı tipleri ve stil ayarları
label_font = ('Helvetica', 12, 'bold')  # Helvetica gibi modern bir font seçtik
entry_font = ('Helvetica', 12)
button_font = ('Helvetica', 12, 'bold')
result_font = ('Helvetica', 14, 'italic')

# Miktar giriş alanı
tk.Label(root, text="Çevrilecek Miktar:", font=label_font, bg='#2f3640', fg='white').grid(column=0, row=0, padx=20, pady=20, sticky='W')
amount_entry = tk.Entry(root, font=entry_font, width=15, bd=2, relief='flat', highlightthickness=2, highlightbackground="#1abc9c")
amount_entry.grid(column=1, row=0, padx=20, pady=20)

# Kaynak para birimi seçimi
tk.Label(root, text="Kaynak Para Birimi:", font=label_font, bg='#2f3640', fg='white').grid(column=0, row=1, padx=20, pady=10, sticky='W')
from_currency_var = tk.StringVar()
from_currency_menu = ttk.Combobox(root, textvariable=from_currency_var, values=['USD', 'EUR', 'GBP', 'TRY', 'JPY', 'CAD', 'AUD'], font=entry_font, width=12)
from_currency_menu.grid(column=1, row=1, padx=20, pady=10)
from_currency_menu.current(0)

# Hedef para birimi seçimi
tk.Label(root, text="Hedef Para Birimi:", font=label_font, bg='#2f3640', fg='white').grid(column=0, row=2, padx=20, pady=10, sticky='W')
to_currency_var = tk.StringVar()
to_currency_menu = ttk.Combobox(root, textvariable=to_currency_var, values=['USD', 'EUR', 'GBP', 'TRY', 'JPY', 'CAD', 'AUD'], font=entry_font, width=12)
to_currency_menu.grid(column=1, row=2, padx=20, pady=10)
to_currency_menu.current(1)

# Çevir butonu
convert_button = tk.Button(root, text="Çevir", command=convert, font=button_font, bg='#1abc9c', fg='white', width=12, height=1, bd=0, relief='flat', activebackground='#16a085', activeforeground='white')
convert_button.grid(column=0, row=3, columnspan=2, padx=20, pady=30)

# Sonuç etiketi
result_label = tk.Label(root, text="", font=result_font, bg='#1e272e', fg='white')
result_label.grid(column=0, row=4, columnspan=2, padx=20, pady=10)

# Pencereyi çalıştır
root.mainloop()
