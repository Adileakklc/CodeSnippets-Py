import tkinter as tk
from tkinter import ttk, messagebox
import time
import threading

class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")
        self.root.geometry("400x300")
        self.root.configure(bg='#F5E1FD')
        
        # Create a style for the widgets
        style = ttk.Style()
        style.configure('TLabel', font=('Helvetica', 14), background='#F5E1FD', foreground='#5D3FD3')
        style.configure('TEntry', font=('Helvetica', 14))
        style.configure('TButton', font=('Helvetica', 14), padding=10)
        
        # Title label
        self.title_label = ttk.Label(self.root, text="Set Alarm Time (HH:MM:SS):")
        self.title_label.pack(pady=20)
        
        # Time entry
        self.time_entry = ttk.Entry(self.root, width=20)
        self.time_entry.pack(pady=10)
        
        # Set alarm button
        self.set_button = ttk.Button(self.root, text="Set Alarm", command=self.set_alarm, style='TButton')
        self.set_button.pack(pady=10)
        
        # Stop alarm button
        self.stop_button = ttk.Button(self.root, text="Stop Alarm", command=self.stop_alarm, style='TButton')
        self.stop_button.pack(pady=10)
        
        self.alarm_set = False
        self.alarm_thread = None
    
    def set_alarm(self):
        alarm_time = self.time_entry.get()
        try:
            time.strptime(alarm_time, '%H:%M:%S')
            self.alarm_set = True
            self.alarm_thread = threading.Thread(target=self.check_alarm, args=(alarm_time,))
            self.alarm_thread.start()
            messagebox.showinfo("Alarm Set", f"Alarm is set for {alarm_time}")
        except ValueError:
            messagebox.showerror("Invalid Time", "Please enter a valid time in HH:MM:SS format")
    
    def check_alarm(self, alarm_time):
        while self.alarm_set:
            current_time = time.strftime('%H:%M:%S')
            if current_time == alarm_time:
                self.alarm_set = False
                messagebox.showinfo("Alarm", "Time to Wake Up!")
                break
            time.sleep(1)
    
    def stop_alarm(self):
        if self.alarm_set:
            self.alarm_set = False
            messagebox.showinfo("Alarm Stopped", "Alarm has been stopped")
        else:
            messagebox.showinfo("No Alarm", "No alarm is set")

if __name__ == "__main__":
    root = tk.Tk()
    alarm_clock = AlarmClock(root)
    root.mainloop()
