"""Tkinter desktop visual GUI for CodeCoach JS."""
from __future__ import annotations

import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser

from coach import analyze_js
from report import format_report

SAMPLE_CODE = """// Paste your JavaScript code here to get kid-friendly tips!
var score = 10;
if (score = 20) {
    console.log "Level complete";
}

while (true) {
    score = score + 1;
}
"""

class CodeCoachJSGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CodeCoach JavaScript - Kid-Friendly Coding Companion")
        self.geometry("900x650")
        self.configure(bg="#0F172A")

        self._build_ui()

    def _build_ui(self):
        # Header banner
        header = tk.Frame(self, bg="#1E293B", padx=16, pady=12)
        header.pack(fill=tk.X)

        title = tk.Label(
            header,
            text="🚀 CodeCoach JavaScript (JS)",
            font=("Segoe UI", 16, "bold"),
            fg="#F8FAFC",
            bg="#1E293B"
        )
        title.pack(side=tk.LEFT)

        btn_discord = tk.Button(
            header,
            text="💎 Join Discord (First 100 Badge)",
            font=("Segoe UI", 9, "bold"),
            bg="#38BDF8",
            fg="#0F172A",
            padx=10,
            pady=4,
            relief=tk.FLAT,
            cursor="hand2",
            command=lambda: webbrowser.open("https://discord.gg/QtyBucygQ6")
        )
        btn_discord.pack(side=tk.RIGHT)

        # Main splitter (Code input vs Feedback)
        paned = tk.PanedWindow(self, orient=tk.HORIZONTAL, bg="#0F172A", sashwidth=4)
        paned.pack(fill=tk.BOTH, expand=True, padx=16, pady=12)

        # Left Frame: Editor
        left_frame = tk.Frame(paned, bg="#1E293B", padx=8, pady=8)
        paned.add(left_frame, minsize=400)

        lbl_editor = tk.Label(left_frame, text="📝 Your JavaScript Code:", font=("Segoe UI", 10, "bold"), fg="#94A3B8", bg="#1E293B")
        lbl_editor.pack(anchor="w", pady=(0, 4))

        self.text_editor = tk.Text(
            left_frame,
            font=("Consolas", 10),
            bg="#0B0F19",
            fg="#F1F5F9",
            insertbackground="#38BDF8",
            padx=8,
            pady=8,
            relief=tk.FLAT
        )
        self.text_editor.pack(fill=tk.BOTH, expand=True)
        self.text_editor.insert(tk.END, SAMPLE_CODE)

        # Right Frame: Coach Report
        right_frame = tk.Frame(paned, bg="#1E293B", padx=8, pady=8)
        paned.add(right_frame, minsize=400)

        lbl_feedback = tk.Label(right_frame, text="💡 Coach Advice & Hints:", font=("Segoe UI", 10, "bold"), fg="#94A3B8", bg="#1E293B")
        lbl_feedback.pack(anchor="w", pady=(0, 4))

        self.text_feedback = tk.Text(
            right_frame,
            font=("Consolas", 10),
            bg="#0B0F19",
            fg="#38BDF8",
            padx=8,
            pady=8,
            relief=tk.FLAT,
            wrap=tk.WORD
        )
        self.text_feedback.pack(fill=tk.BOTH, expand=True)

        # Bottom Controls
        footer = tk.Frame(self, bg="#0F172A", pady=8)
        footer.pack(fill=tk.X, padx=16)

        btn_analyze = tk.Button(
            footer,
            text="🔍 Coach My JavaScript!",
            font=("Segoe UI", 11, "bold"),
            bg="#22C55E",
            fg="#0F172A",
            padx=16,
            pady=6,
            relief=tk.FLAT,
            cursor="hand2",
            command=self._on_analyze
        )
        btn_analyze.pack(side=tk.LEFT)

        btn_clear = tk.Button(
            footer,
            text="🧹 Clear Editor",
            font=("Segoe UI", 10),
            bg="#334155",
            fg="#F8FAFC",
            padx=12,
            pady=6,
            relief=tk.FLAT,
            cursor="hand2",
            command=lambda: self.text_editor.delete("1.0", tk.END)
        )
        btn_clear.pack(side=tk.LEFT, padx=8)

        # Run initial review
        self._on_analyze()

    def _on_analyze(self):
        code = self.text_editor.get("1.0", tk.END)
        rep = format_report(code, for_parents=False)
        self.text_feedback.delete("1.0", tk.END)
        self.text_feedback.insert(tk.END, rep)

if __name__ == "__main__":
    app = CodeCoachJSGUI()
    app.mainloop()
