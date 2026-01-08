from pydoc import text
import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    text.delete(1.0, tk.END)
    
def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            text.delete(1.0, tk.END)
            text.insert(tk.END, content) 
            
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            content = text.get(1.0, tk.END)
            file.write(content)               
            messagebox.showinfo("Save File", "File saved successfully!")
         
root = tk.Tk()
root.title("Text Editor App")
root.geometry("800x600")

menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)

menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

text = tk.Text(root , wrap = tk.WORD , font =("Times New Roman" , 12) , fg ="blue" )
text.pack(expand=tk.YES, fill=tk.BOTH)

root.mainloop()