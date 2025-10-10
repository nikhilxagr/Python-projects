import os
import threading
import queue
import yt_dlp
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class YTDLGui:
    def __init__(self, root):
        self.root = root
        root.title("Simple YouTube Downloader")
        root.geometry("600x350")
        root.resizable(False, False)

        # Queue for safe thread → GUI communication
        self.queue = queue.Queue()

        # Tkinter variables
        self.url_var = tk.StringVar()
        self.save_var = tk.StringVar(value=os.path.join(os.path.expanduser("~"), "Downloads"))
        self.format_var = tk.StringVar(value="mp4")  # mp4, mp3, best

        # Build the GUI
        self.build_ui()

        # Start checking the queue every 200ms
        self.root.after(200, self.process_queue)

    def build_ui(self):
        """Create the layout of the GUI"""
        pad = 8
        frm = ttk.Frame(self.root, padding=pad)
        frm.pack(fill='both', expand=True)

        # URL row
        ttk.Label(frm, text="YouTube URL:").pack(anchor='w')
        ttk.Entry(frm, textvariable=self.url_var, width=70).pack(fill='x', pady=(0,6))

        # Save folder row
        row = ttk.Frame(frm)
        row.pack(fill='x', pady=(0,6))
        ttk.Label(row, text="Save to:").pack(side='left')
        ttk.Entry(row, textvariable=self.save_var, width=50).pack(side='left', padx=(6,0))
        ttk.Button(row, text="Browse", command=self.browse_folder).pack(side='left', padx=(6,0))

        # Format dropdown
        ttk.Label(frm, text="Format:").pack(anchor='w')
        ttk.OptionMenu(frm, self.format_var, "mp4", "mp4", "mp3", "best").pack(anchor='w', pady=(0,6))

        # Buttons
        ttk.Button(frm, text="Download", command=self.start_download).pack(pady=(0,6))
        ttk.Button(frm, text="Clear log", command=self.clear_log).pack()

        # Progress bar
        self.progress = ttk.Progressbar(frm, orient='horizontal', length=400, mode='determinate', maximum=100)
        self.progress.pack(fill='x', pady=(6,0))

        # Log area
        self.log_text = tk.Text(frm, wrap='word', height=10, state='disabled')
        self.log_text.pack(fill='both', expand=True, pady=(8,0))

    def browse_folder(self):
        """Open folder picker"""
        d = filedialog.askdirectory(initialdir=self.save_var.get())
        if d:
            self.save_var.set(d)

    def append_log(self, text):
        """Write a line into the log box"""
        self.log_text.configure(state='normal')
        self.log_text.insert('end', text + '\n')
        self.log_text.see('end')
        self.log_text.configure(state='disabled')

    def clear_log(self):
        """Clear the log box"""
        self.log_text.configure(state='normal')
        self.log_text.delete('1.0', 'end')
        self.log_text.configure(state='disabled')

    def start_download(self):
        """Start download in a separate thread"""
        url = self.url_var.get().strip()
        if not url:
            messagebox.showerror("Error", "Please enter a URL.")
            return

        save_to = self.save_var.get().strip()
        if not os.path.isdir(save_to):
            os.makedirs(save_to, exist_ok=True)

        self.clear_log()
        self.append_log(f"Queued: {url}")
        self.progress['value'] = 0

 # Run yt-dlp in a background thread
        t = threading.Thread(target=self._download_thread, args=(url, save_to), daemon=True)
        t.start()

    def _download_thread(self, url, save_to):
        """Download logic running in background thread"""
        outtmpl = os.path.join(save_to, "%(title)s.%(ext)s")
        fmt_choice = self.format_var.get()

        # yt-dlp options
        ydl_opts = {
            'outtmpl': outtmpl,
            'progress_hooks': [self.progress_hook],
            'quiet': True,
            'no_warnings': True,
        }

        if fmt_choice == 'mp4':
            ydl_opts['format'] = "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4"
        elif fmt_choice == 'mp3':
            ydl_opts['format'] = "bestaudio/best"
            ydl_opts['postprocessors'] = [
                {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}
            ]
        else:  # best
            ydl_opts['format'] = "best"

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                self.queue.put(('log', "Starting download..."))
                ydl.download([url])
                self.queue.put(('done', "Download finished successfully."))
        except Exception as e:
            self.queue.put(('error', str(e)))

    def progress_hook(self, d):
        """Callback from yt-dlp for progress updates"""
        if d['status'] == 'downloading':
            total = d.get('total_bytes') or d.get('total_bytes_estimate')
            downloaded = d.get('downloaded_bytes', 0)
            if total:
                percent = int(downloaded * 100 / total)
                self.queue.put(('progress', percent))
        elif d['status'] == 'finished':
            self.queue.put(('progress', 100))
            self.queue.put(('log', "Finished download (post-processing...)"))

    def process_queue(self):
        """Process messages from download thread"""
        try:
            while True:
                typ, val = self.queue.get_nowait()
                if typ == 'log':
                    self.append_log(val)
                elif typ == 'progress':
                    self.progress['value'] = val
                elif typ == 'done':
                    self.append_log(val)
                    messagebox.showinfo("Done", val)
                elif typ == 'error':
                    self.append_log("ERROR: " + val)
                    messagebox.showerror("Error", val)
        except queue.Empty:
            pass
        finally:
            self.root.after(200, self.process_queue)


if __name__ == "__main__":
    root = tk.Tk()
    app = YTDLGui(root)
    root.mainloop()