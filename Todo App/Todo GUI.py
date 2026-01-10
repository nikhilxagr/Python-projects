import tkinter as tk
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("Todo App")
root.geometry("400x400")

tasks = []

# Functions
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task")

def update_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        new_task = task_entry.get()
        if new_task:
            tasks[index] = new_task
            listbox.delete(index)
            listbox.insert(index, new_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Enter new task name")
    else:
        messagebox.showwarning("Warning", "Select a task to update")

def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        listbox.delete(index)
        tasks.pop(index)
    else:
        messagebox.showwarning("Warning", "Select a task to delete")

# UI Elements
title = tk.Label(root, text="Todo App", font=("Arial", 16))
title.pack(pady=10)

task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=5)

add_btn = tk.Button(root, text="Add Task", width=15, command=add_task)
add_btn.pack(pady=5)

update_btn = tk.Button(root, text="Update Task", width=15, command=update_task)
update_btn.pack(pady=5)

delete_btn = tk.Button(root, text="Delete Task", width=15, command=delete_task)
delete_btn.pack(pady=5)

listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=10)

# Run app
root.mainloop()
