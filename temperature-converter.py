import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Dönüştürme işlemleri
def convert_temperature():
    try:
        temp = float(entry_temperature.get())
        from_unit = from_unit_var.get()
        to_unit = to_unit_var.get()

        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                result = (temp * 9 / 5) + 32
            elif to_unit == "Kelvin":
                result = temp + 273.15
            else:
                result = temp
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                result = (temp - 32) * 5 / 9
            elif to_unit == "Kelvin":
                result = (temp - 32) * 5 / 9 + 273.15
            else:
                result = temp
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                result = temp - 273.15
            elif to_unit == "Fahrenheit":
                result = (temp - 273.15) * 9 / 5 + 32
            else:
                result = temp

        label_result.config(text=f"{temp} {from_unit} = {result:.2f} {to_unit}", fg="#FFA726")
    except ValueError:
        label_result.config(text="Geçerli bir sıcaklık değeri girin!", fg="#EF5350")


# Ana pencere
root = tk.Tk()
root.title("Sıcaklık Dönüştürücü")
root.geometry("500x300")

image_path = "C:/Users/user/PycharmProjects/pythonProject1/background.webp"
bg_image = Image.open(image_path)
bg_image = bg_image.resize((500, 300), Image.Resampling.LANCZOS)  # Pillow'un güncel Resampling özelliği kullanıldı
bg_photo = ImageTk.PhotoImage(bg_image)

# Canvas üzerinde resmi gösterme
canvas = tk.Canvas(root, width=500, height=300)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

label_font = ('Helvetica', 12, 'bold')
entry_font = ('Helvetica', 12)
button_font = ('Helvetica', 12, 'bold')

canvas.create_text(70, 50, text="Sıcaklık:", font=label_font, fill='#964B00', anchor="w")
entry_temperature = tk.Entry(root, font=entry_font, width=15, bd=2, relief='flat', highlightthickness=2,
                             highlightbackground="#FFCC80")
entry_window = canvas.create_window(375, 50, window=entry_temperature)

# Kaynak sıcaklık birimi seçimi
canvas.create_text(70, 100, text="Dönüştürülecek Birim:", font=label_font, fill='#964B00', anchor="w")
from_unit_var = tk.StringVar()
from_unit_menu = ttk.Combobox(root, textvariable=from_unit_var, values=['Celsius', 'Fahrenheit', 'Kelvin'],
                              font=entry_font, width=12)
from_unit_menu.current(0)
from_unit_window = canvas.create_window(375, 100, window=from_unit_menu)

# Hedef sıcaklık birimi seçimi
canvas.create_text(70, 150, text="Dönüştürmek İstediğiniz Birim:", font=label_font, fill='#964B00', anchor="w")
to_unit_var = tk.StringVar()
to_unit_menu = ttk.Combobox(root, textvariable=to_unit_var, values=['Celsius', 'Fahrenheit', 'Kelvin'], font=entry_font,
                            width=12)
to_unit_menu.current(1)
to_unit_window = canvas.create_window(375, 150, window=to_unit_menu)

# Dönüştür butonu
convert_button = tk.Button(root, text="Dönüştür", command=convert_temperature, font=button_font, bg='#FFCC80',
                           fg='white', width=12, height=1, bd=0, relief='flat', activebackground='#FF004D',
                           activeforeground='white')
convert_button_window = canvas.create_window(250, 200, window=convert_button)

# Sonuç etiketi
label_result = tk.Label(root, text="", font=button_font, bg='#FFF3E0', fg='#FFCC80')
label_result_window = canvas.create_window(200, 250, window=label_result)

# Pencereyi çalıştır
root.mainloop()
