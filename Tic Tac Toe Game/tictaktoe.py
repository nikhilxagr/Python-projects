import tkinter as tk
from tkinter import messagebox


WINDOW_BG = "#f3f4f6"
PANEL_BG = "#ffffff"
TEXT_DARK = "#111827"
TEXT_MUTED = "#6b7280"
GRID_BG = "#d1d5db"
EMPTY_BG = "#f9fafb"
HOVER_BG = "#eef2ff"
X_COLOR = "#2563eb"
O_COLOR = "#dc2626"
WIN_BG = "#bbf7d0"


class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("430x610")
        self.root.minsize(400, 590)
        self.root.resizable(False, False)
        self.root.configure(bg=WINDOW_BG)

        self.current_player = "X"
        self.game_over = False
        self.scores = {"X": 0, "O": 0, "Draw": 0}
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.score_labels = {}
        self.status_text = tk.StringVar(value="Player X starts")

        self._build_ui()

    def _build_ui(self):
        shell = tk.Frame(self.root, bg=WINDOW_BG, padx=22, pady=18)
        shell.pack(fill="both", expand=True)

        header = tk.Frame(shell, bg=WINDOW_BG)
        header.pack(fill="x")

        tk.Label(
            header,
            text="Tic Tac Toe",
            bg=WINDOW_BG,
            fg=TEXT_DARK,
            font=("Segoe UI", 22, "bold"),
        ).pack(anchor="w")

        tk.Label(
            header,
            textvariable=self.status_text,
            bg=WINDOW_BG,
            fg=TEXT_MUTED,
            font=("Segoe UI", 11),
        ).pack(anchor="w", pady=(4, 0))

        score_panel = tk.Frame(shell, bg=WINDOW_BG)
        score_panel.pack(fill="x", pady=(16, 14))

        self._add_score_card(score_panel, "Player X", "X", X_COLOR)
        self._add_score_card(score_panel, "Draws", "Draw", "#7c3aed")
        self._add_score_card(score_panel, "Player O", "O", O_COLOR)

        board_outer = tk.Frame(shell, bg=GRID_BG, padx=6, pady=6)
        board_outer.pack(pady=(2, 16))

        for row in range(3):
            for col in range(3):
                cell = tk.Frame(board_outer, width=106, height=106, bg=GRID_BG)
                cell.grid(row=row, column=col, padx=4, pady=4)
                cell.grid_propagate(False)

                button = tk.Button(
                    cell,
                    text="",
                    bg=EMPTY_BG,
                    fg=TEXT_DARK,
                    activebackground=HOVER_BG,
                    activeforeground=TEXT_DARK,
                    relief="flat",
                    bd=0,
                    font=("Segoe UI", 34, "bold"),
                    command=lambda r=row, c=col: self.play_move(r, c),
                )
                button.pack(fill="both", expand=True)
                button.bind("<Enter>", lambda event, b=button: self._set_hover(b, True))
                button.bind("<Leave>", lambda event, b=button: self._set_hover(b, False))
                self.buttons[row][col] = button

        controls = tk.Frame(shell, bg=WINDOW_BG)
        controls.pack(fill="x")

        tk.Button(
            controls,
            text="New Round",
            command=self.reset_round,
            bg="#111827",
            fg="#ffffff",
            activebackground="#374151",
            activeforeground="#ffffff",
            relief="flat",
            font=("Segoe UI", 10, "bold"),
            padx=16,
            pady=10,
        ).pack(side="left", fill="x", expand=True, padx=(0, 6))

        tk.Button(
            controls,
            text="Reset Score",
            command=self.reset_score,
            bg="#e5e7eb",
            fg=TEXT_DARK,
            activebackground="#d1d5db",
            activeforeground=TEXT_DARK,
            relief="flat",
            font=("Segoe UI", 10, "bold"),
            padx=16,
            pady=10,
        ).pack(side="left", fill="x", expand=True, padx=(6, 0))

    def _add_score_card(self, parent, title, key, accent):
        card = tk.Frame(parent, bg=PANEL_BG, padx=10, pady=8, highlightthickness=1, highlightbackground="#e5e7eb")
        card.pack(side="left", fill="x", expand=True, padx=4)

        tk.Label(
            card,
            text=title,
            bg=PANEL_BG,
            fg=TEXT_MUTED,
            font=("Segoe UI", 9, "bold"),
        ).pack()

        value = tk.Label(
            card,
            text=str(self.scores[key]),
            bg=PANEL_BG,
            fg=accent,
            font=("Segoe UI", 18, "bold"),
        )
        value.pack(pady=(2, 0))
        self.score_labels[key] = value

    def _set_hover(self, button, is_hovering):
        if self.game_over or button["text"]:
            return

        button.configure(bg=HOVER_BG if is_hovering else EMPTY_BG)

    def play_move(self, row, col):
        if self.game_over or self.buttons[row][col]["text"]:
            return

        button = self.buttons[row][col]
        button.configure(
            text=self.current_player,
            fg=X_COLOR if self.current_player == "X" else O_COLOR,
            bg=PANEL_BG,
            activebackground=PANEL_BG,
        )

        winning_cells = self.get_winning_cells()
        if winning_cells:
            self.finish_game(winning_cells)
            return

        if self.is_draw():
            self.scores["Draw"] += 1
            self.update_scoreboard()
            self.game_over = True
            self.status_text.set("Round ended in a draw")
            messagebox.showinfo("Game Over", "It's a draw!")
            return

        self.current_player = "O" if self.current_player == "X" else "X"
        self.status_text.set(f"Player {self.current_player}'s turn")

    def get_winning_cells(self):
        lines = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)],
        ]

        for line in lines:
            values = [self.buttons[row][col]["text"] for row, col in line]
            if values[0] and values[0] == values[1] == values[2]:
                return line

        return []

    def finish_game(self, winning_cells):
        self.game_over = True
        self.scores[self.current_player] += 1
        self.update_scoreboard()
        self.status_text.set(f"Player {self.current_player} wins")

        for row, col in winning_cells:
            self.buttons[row][col].configure(bg=WIN_BG, activebackground=WIN_BG)

        messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")

    def is_draw(self):
        return all(button["text"] for row in self.buttons for button in row)

    def reset_round(self):
        self.current_player = "X"
        self.game_over = False
        self.status_text.set("Player X starts")

        for row in self.buttons:
            for button in row:
                button.configure(
                    text="",
                    bg=EMPTY_BG,
                    fg=TEXT_DARK,
                    activebackground=HOVER_BG,
                )

    def reset_score(self):
        self.scores = {"X": 0, "O": 0, "Draw": 0}
        self.update_scoreboard()
        self.reset_round()

    def update_scoreboard(self):
        for key, label in self.score_labels.items():
            label.configure(text=str(self.scores[key]))


if __name__ == "__main__":
    window = tk.Tk()
    app = TicTacToeApp(window)
    window.mainloop()
