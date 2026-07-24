from pathlib import Path
from tkinter import Button, Entry, Frame, Label, StringVar, Tk, filedialog, messagebox
from urllib.parse import urlencode

import qrcode
from PIL import Image, ImageTk


APP_TITLE = "UPI QR Code Generator"
DEFAULT_FILE_NAME = "upi_qr.png"


class UpiQrApp:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.geometry("460x560")
        self.root.minsize(420, 520)
        self.root.configure(bg="#f6f7fb")

        self.upi_id = StringVar()
        self.status = StringVar(value="Paste your UPI ID and generate a QR code.")
        self.qr_image = None
        self.qr_photo = None
        self.qr_data = ""

        self._build_ui()

    def _build_ui(self):
        container = Frame(self.root, bg="#f6f7fb", padx=24, pady=24)
        container.pack(fill="both", expand=True)

        Label(
            container,
            text=APP_TITLE,
            bg="#f6f7fb",
            fg="#111827",
            font=("Segoe UI", 18, "bold"),
        ).pack(anchor="w")

        Label(
            container,
            text="UPI ID",
            bg="#f6f7fb",
            fg="#374151",
            font=("Segoe UI", 11, "bold"),
        ).pack(anchor="w", pady=(26, 6))

        input_row = Frame(container, bg="#f6f7fb")
        input_row.pack(fill="x")

        self.upi_entry = Entry(
            input_row,
            textvariable=self.upi_id,
            font=("Segoe UI", 12),
            relief="solid",
            bd=1,
        )
        self.upi_entry.pack(side="left", fill="x", expand=True, ipady=8)
        self.upi_entry.focus()

        Button(
            input_row,
            text="Paste",
            command=self.paste_from_clipboard,
            font=("Segoe UI", 10),
            bg="#e5e7eb",
            fg="#111827",
            relief="flat",
            padx=14,
            pady=8,
        ).pack(side="left", padx=(8, 0))

        Button(
            container,
            text="Generate QR Code",
            command=self.generate_qr,
            font=("Segoe UI", 11, "bold"),
            bg="#2563eb",
            fg="#ffffff",
            activebackground="#1d4ed8",
            activeforeground="#ffffff",
            relief="flat",
            pady=10,
        ).pack(fill="x", pady=(16, 20))

        preview_frame = Frame(container, bg="#ffffff", relief="solid", bd=1)
        preview_frame.pack(fill="both", expand=True)

        self.preview_label = Label(
            preview_frame,
            text="QR preview",
            bg="#ffffff",
            fg="#6b7280",
            font=("Segoe UI", 13),
        )
        self.preview_label.pack(expand=True)

        action_row = Frame(container, bg="#f6f7fb")
        action_row.pack(fill="x", pady=(18, 0))

        self.save_button = Button(
            action_row,
            text="Save PNG",
            command=self.save_qr,
            state="disabled",
            font=("Segoe UI", 10, "bold"),
            bg="#10b981",
            fg="#ffffff",
            activebackground="#059669",
            activeforeground="#ffffff",
            relief="flat",
            padx=16,
            pady=8,
        )
        self.save_button.pack(side="left")

        Label(
            action_row,
            textvariable=self.status,
            bg="#f6f7fb",
            fg="#4b5563",
            font=("Segoe UI", 9),
            wraplength=270,
            justify="left",
        ).pack(side="left", padx=(12, 0), fill="x", expand=True)

        self.root.bind("<Return>", lambda _event: self.generate_qr())

    def paste_from_clipboard(self):
        try:
            value = self.root.clipboard_get().strip()
        except Exception:
            messagebox.showwarning(APP_TITLE, "Clipboard does not contain text.")
            return

        self.upi_id.set(value)
        self.upi_entry.icursor("end")

    def generate_qr(self):
        upi_id = self.upi_id.get().strip()
        if not self._is_valid_upi_id(upi_id):
            messagebox.showerror(APP_TITLE, "Enter a valid UPI ID, for example name@bank.")
            return

        params = urlencode({"pa": upi_id, "pn": "Recipient Name", "cu": "INR"})
        self.qr_data = f"upi://pay?{params}"

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4,
        )
        qr.add_data(self.qr_data)
        qr.make(fit=True)

        self.qr_image = qr.make_image(fill_color="black", back_color="white").convert("RGB")
        preview = self.qr_image.resize((300, 300), Image.Resampling.LANCZOS)
        self.qr_photo = ImageTk.PhotoImage(preview)

        self.preview_label.configure(image=self.qr_photo, text="")
        self.save_button.configure(state="normal")
        self.status.set("QR code generated. Scan it with any UPI app.")

    def save_qr(self):
        if self.qr_image is None:
            return

        default_path = Path.cwd() / DEFAULT_FILE_NAME
        file_path = filedialog.asksaveasfilename(
            title="Save QR Code",
            initialdir=default_path.parent,
            initialfile=default_path.name,
            defaultextension=".png",
            filetypes=[("PNG image", "*.png")],
        )
        if not file_path:
            return

        self.qr_image.save(file_path)
        self.status.set(f"Saved to {Path(file_path).name}.")

    @staticmethod
    def _is_valid_upi_id(value):
        if " " in value or "@" not in value:
            return False

        user_name, bank_handle = value.rsplit("@", 1)
        return bool(user_name) and bool(bank_handle)


if __name__ == "__main__":
    window = Tk()
    app = UpiQrApp(window)
    window.mainloop()
