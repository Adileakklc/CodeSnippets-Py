import tkinter as tk
from tkinter import messagebox

# Görevleri yönetmek için fonksiyonlar
def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task to delete.")

def clear_tasks():
    if messagebox.askyesno("Clear All", "Do you really want to clear all tasks?"):
        listbox_tasks.delete(0, tk.END)

# Arayüz oluşturma
window = tk.Tk() #e0a6d9
window.title("To-Do List")
window.config(bg="#E0A6D9")

# Görev ekleme bölümü
frame_task = tk.Frame(window)
frame_task.pack(pady=10)

entry_task = tk.Entry(frame_task, width=30, font=("Helvetica", 14) )
entry_task.pack(side=tk.LEFT, padx=10)

button_add_task = tk.Button(frame_task, text="Add Task", width=10, command=add_task ,bg="#B2109F", fg="#FFFFFF")
button_add_task.pack(side=tk.LEFT)

# Görev listesi
listbox_tasks = tk.Listbox(window, width=50, height=15, font=("Helvetica", 14 , "bold") , bg="#B2109F", fg="#FFFFFF" )
listbox_tasks.pack(pady=20)

# Düğmeler
button_delete_task = tk.Button(window, text="Delete Task", width=10,font=("Helvetica", 10), bg="#B2109F", fg="#FFFFFF" ,command=delete_task)
button_delete_task.pack(side=tk.LEFT, padx=10)

button_clear_tasks = tk.Button(window, text="Clear All", width=10,font=("Helvetica", 10), bg="#B2109F", fg="#FFFFFF", command=clear_tasks)
button_clear_tasks.pack(side=tk.RIGHT, padx=10)

# Pencereyi başlat
window.mainloop()
