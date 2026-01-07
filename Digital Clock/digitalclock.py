import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

def time():
    string = strftime('%H:%M:%S  %p \n %d, %Y')
    label.config(text=string)
    label.after(1000, time)
    
label = tk.Label(root, font=('ds-digital', 80), background='black', foreground='cyan')
label.pack(anchor='center')
time()
root.mainloop()    