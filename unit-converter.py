import tkinter as tk
from tkinter import ttk

def convert_length(value, from_unit, to_unit):
    length_units = {
        'Meter': 1,
        'Kilometer': 0.001,
        'Mile': 0.000621371,
        'Centimeter': 100,
        'Inch': 39.3701
    }
    
    return value * (length_units[to_unit] / length_units[from_unit])

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        'Kilogram': 1,
        'Gram': 1000,
        'Pound': 2.20462
    }
    
    return value * (weight_units[to_unit] / weight_units[from_unit])

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'Celsius':
        if to_unit == 'Fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'Kelvin':
            return value + 273.15
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            return (value - 32) * 5/9
        elif to_unit == 'Kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            return value - 273.15
        elif to_unit == 'Fahrenheit':
            return (value - 273.15) * 9/5 + 32

def convert_volume(value, from_unit, to_unit):
    volume_units = {
        'Litre': 1,
        'Millilitre': 1000,
        'Gallon': 0.264172
    }
    
    return value * (volume_units[to_unit] / volume_units[from_unit])

def perform_conversion():
    value = float(entry_value.get())
    from_unit = from_var.get()
    to_unit = to_var.get()
    unit_type = unit_type_var.get()

    if unit_type == 'Length':
        result = convert_length(value, from_unit, to_unit)
    elif unit_type == 'Weight':
        result = convert_weight(value, from_unit, to_unit)
    elif unit_type == 'Temperature':
        result = convert_temperature(value, from_unit, to_unit)
    elif unit_type == 'Volume':
        result = convert_volume(value, from_unit, to_unit)

    label_result.config(text=f"Result: {result:.4f}")

# Arayüz oluşturma
root = tk.Tk()
root.title("Unit Converter")

# Arayüz Renkleri
bg_color = "#D8BFD8"  # Soft mor arka plan rengi
button_color = "#9370DB"  # Buton rengi

root.configure(bg=bg_color)

# Başlık
label_title = tk.Label(root, text="Unit Converter", font=("Arial", 16, "bold"), bg=bg_color)
label_title.grid(row=0, column=0, columnspan=2, pady=10)

# Değer girişi
label_value = tk.Label(root, text="Value:", bg=bg_color)
label_value.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_value = tk.Entry(root)
entry_value.grid(row=1, column=1, padx=10, pady=5)

# Birim türü seçimi
label_unit_type = tk.Label(root, text="Unit Type:", bg=bg_color)
label_unit_type.grid(row=2, column=0, padx=10, pady=5, sticky="e")
unit_type_var = tk.StringVar(value="Length")
combo_unit_type = ttk.Combobox(root, textvariable=unit_type_var, values=["Length", "Weight", "Temperature", "Volume"])
combo_unit_type.grid(row=2, column=1, padx=10, pady=5)

# Dönüştürülecek birim seçimi
label_from = tk.Label(root, text="From Unit:", bg=bg_color)
label_from.grid(row=3, column=0, padx=10, pady=5, sticky="e")
from_var = tk.StringVar()
combo_from = ttk.Combobox(root, textvariable=from_var)
combo_from.grid(row=3, column=1, padx=10, pady=5)

# Dönüştürülmek istenen birim seçimi
label_to = tk.Label(root, text="To Unit:", bg=bg_color)
label_to.grid(row=4, column=0, padx=10, pady=5, sticky="e")
to_var = tk.StringVar()
combo_to = ttk.Combobox(root, textvariable=to_var)
combo_to.grid(row=4, column=1, padx=10, pady=5)

# Dönüşüm türüne göre birim seçeneklerini güncelle
def update_units(*args):
    unit_type = unit_type_var.get()
    if unit_type == "Length":
        units = ["Meter", "Kilometer", "Mile", "Centimeter", "Inch"]
    elif unit_type == "Weight":
        units = ["Kilogram", "Gram", "Pound"]
    elif unit_type == "Temperature":
        units = ["Celsius", "Fahrenheit", "Kelvin"]
    elif unit_type == "Volume":
        units = ["Litre", "Millilitre", "Gallon"]
    
    combo_from.config(values=units)
    combo_to.config(values=units)
    from_var.set(units[0])
    to_var.set(units[1])

unit_type_var.trace('w', update_units)
update_units()

# Sonuç
label_result = tk.Label(root, text="Result:", font=("Arial", 12), bg=bg_color)
label_result.grid(row=5, column=0, columnspan=2, pady=10)

# Dönüştürme Butonu
button_convert = tk.Button(root, text="Convert", command=perform_conversion, bg=button_color, fg="white", font=("Arial", 12))
button_convert.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
