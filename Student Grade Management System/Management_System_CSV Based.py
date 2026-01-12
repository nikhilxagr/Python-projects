import tkinter as tk
from tkinter import ttk, messagebox
import csv


# Grade Calculation

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"


# Add Student

def add_student():
    name = entry_name.get()
    try:
        m1 = float(entry_m1.get())
        m2 = float(entry_m2.get())
        m3 = float(entry_m3.get())
    except ValueError:
        messagebox.showerror("Error", "Enter valid marks")
        return

    avg = (m1 + m2 + m3) / 3
    grade = calculate_grade(avg)

    table.insert("", "end", values=(name, m1, m2, m3, f"{avg:.2f}", grade))
    clear_entries()


# Select Record

def select_record(event):
    selected = table.focus()
    if not selected:
        return

    values = table.item(selected, "values")
    clear_entries()

    entry_name.insert(0, values[0])
    entry_m1.insert(0, values[1])
    entry_m2.insert(0, values[2])
    entry_m3.insert(0, values[3])


# Update Record

def update_record():
    selected = table.focus()
    if not selected:
        messagebox.showwarning("Warning", "Select a record first")
        return

    name = entry_name.get()
    m1 = float(entry_m1.get())
    m2 = float(entry_m2.get())
    m3 = float(entry_m3.get())

    avg = (m1 + m2 + m3) / 3
    grade = calculate_grade(avg)

    table.item(selected, values=(name, m1, m2, m3, f"{avg:.2f}", grade))
    clear_entries()


# Delete Record

def delete_record():
    selected = table.focus()
    if not selected:
        messagebox.showwarning("Warning", "Select a record first")
        return

    table.delete(selected)
    clear_entries()

# Save to CSV

def save_to_csv():
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Mark1", "Mark2", "Mark3", "Average", "Grade"])

        for row in table.get_children():
            writer.writerow(table.item(row)["values"])

    messagebox.showinfo("Saved", "Data saved to students.csv")

# Clear Entry Fields

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_m1.delete(0, tk.END)
    entry_m2.delete(0, tk.END)
    entry_m3.delete(0, tk.END)

# GUI Window

root = tk.Tk()
root.title("Student Grade Management System")
root.geometry("800x500")
root.resizable(False, False)


# Input Frame

frame = tk.LabelFrame(root, text="Student Details")
frame.pack(fill="x", padx=20, pady=10)

tk.Label(frame, text="Name").grid(row=0, column=0, padx=5)
entry_name = tk.Entry(frame)
entry_name.grid(row=0, column=1)

tk.Label(frame, text="Mark 1").grid(row=0, column=2)
entry_m1 = tk.Entry(frame, width=10)
entry_m1.grid(row=0, column=3)

tk.Label(frame, text="Mark 2").grid(row=0, column=4)
entry_m2 = tk.Entry(frame, width=10)
entry_m2.grid(row=0, column=5)

tk.Label(frame, text="Mark 3").grid(row=0, column=6)
entry_m3 = tk.Entry(frame, width=10)
entry_m3.grid(row=0, column=7)

# Buttons
tk.Button(frame, text="Add", command=add_student).grid(row=1, column=1, pady=5)
tk.Button(frame, text="Update", command=update_record).grid(row=1, column=3)
tk.Button(frame, text="Delete", command=delete_record).grid(row=1, column=5)
tk.Button(frame, text="Save to CSV", command=save_to_csv).grid(row=1, column=7)


# Table

columns = ("Name", "Mark 1", "Mark 2", "Mark 3", "Average", "Grade")
table = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    table.heading(col, text=col)
    table.column(col, anchor="center")

table.pack(fill="both", expand=True, padx=20, pady=10)
table.bind("<ButtonRelease-1>", select_record)

root.mainloop()
