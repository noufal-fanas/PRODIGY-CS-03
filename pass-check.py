import customtkinter as ctk
import re

# --- Visual Theme Config ---
BG_COLOR = "#0D0D0D"      
INPUT_BG = "#1A1A1A"      
CYBER_GREEN = "#00E676"  
RED_ALERT = "#FF5252"     
AMBER_WARN = "#FFAB40"    

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

class PassCheckApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # --- Window Config ---
        self.title("PassCheck v4.4 | Identity Analyzer")
        self.geometry("600x620")
        self.configure(fg_color=BG_COLOR)
        
        # Ensure the main window column stretches
        self.grid_columnconfigure(0, weight=1)

        # 1. Main Header Title
        self.header_label = ctk.CTkLabel(self, text="PASSCHECK", 
                                       font=("Segoe UI Semibold", 48), 
                                       text_color=CYBER_GREEN)
        self.header_label.grid(row=0, column=0, pady=(40, 5))

        # 2. Central Symbol Container (Forces perfect horizontal centering)
        self.icon_container = ctk.CTkFrame(self, fg_color="transparent")
        self.icon_container.grid(row=1, column=0, sticky="ew", pady=(10, 20))
        self.icon_container.grid_columnconfigure(0, weight=1) 

        # The Shield Symbol (Unicode)
        self.symbol_label = ctk.CTkLabel(self.icon_container, text="🛡", 
                                        font=("Arial", 80), text_color=CYBER_GREEN)
        self.symbol_label.grid(row=0, column=0) # Default grid behavior is centered

        # 3. Input Section
        self.password_var = ctk.StringVar()
        self.password_var.trace_add("write", self.advanced_check)

        self.entry = ctk.CTkEntry(self, textvariable=self.password_var, show="●", 
                                 width=450, height=55, placeholder_text="Input secret for analysis...",
                                 font=("Segoe UI", 16), fg_color=INPUT_BG, 
                                 border_color="#333", corner_radius=15, justify="center")
        self.entry.grid(row=2, column=0, pady=(10, 20))

        # 4. Feedback Display Area
        self.status_label = ctk.CTkLabel(self, text="READY", 
                                        font=("Courier New", 24, "bold"), text_color="#444")
        self.status_label.grid(row=3, column=0, pady=5)

        self.progress = ctk.CTkProgressBar(self, width=450, height=18, corner_radius=15)
        self.progress.set(0)
        self.progress.grid(row=4, column=0, pady=25)

        self.tips_label = ctk.CTkLabel(self, text="Awaiting input for heuristic analysis...", 
                                      font=("Segoe UI", 13), text_color="#666")
        self.tips_label.grid(row=5, column=0, pady=5)

        # 5. Footer Branding
        self.footer = ctk.CTkLabel(self, text="Developed by NOUFAL N S ", 
                                  font=("Courier New", 10, "bold"), text_color="#666")
        self.footer.grid(row=6, column=0, pady=(40, 20), sticky="s")

    # --- Logic: Advanced Heuristic Strength Validation ---
    def advanced_check(self, *args):
        pwd = self.password_var.get()
        if not pwd:
            self.reset_ui()
            return

        score = 0
        feedback = []

        # Logic for Google-style complexity
        if len(pwd) >= 8: score += 1
        else: feedback.append("Too short")

        has_upper = re.search(r"[A-Z]", pwd)
        has_lower = re.search(r"[a-z]", pwd)
        has_digit = re.search(r"\d", pwd)
        has_special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", pwd)

        variety_count = sum(bool(x) for x in [has_upper, has_lower, has_digit, has_special])
        
        if variety_count >= 3: score += 2
        elif variety_count == 2: score += 1
        
        if len(pwd) >= 12 and variety_count >= 2: score += 1
        if len(pwd) >= 16 and variety_count >= 3: score += 1

        if variety_count <= 1:
            score = min(score, 1) 
            feedback.append("Needs numbers/symbols")

        strength_map = [
            (0, "DANGEROUS", RED_ALERT),
            (1, "WEAK", RED_ALERT),
            (2, "FAIR", AMBER_WARN),
            (3, "GOOD", "#B2FF59"),
            (4, "STRONG", CYBER_GREEN),
            (5, "SECURE", CYBER_GREEN)
        ]

        score = max(0, min(score, 5))
        level = strength_map[score]

        self.progress.set(score / 5)
        self.progress.configure(progress_color=level[2])
        self.status_label.configure(text=f"STATUS: {level[1]}", text_color=level[2])
        self.symbol_label.configure(text_color=level[2]) # Symbol color changes with strength!
        
        self.tips_label.configure(text=" | ".join(feedback) if feedback else "Security requirements satisfied.")

    def reset_ui(self):
        self.progress.set(0)
        self.progress.configure(progress_color="#333")
        self.status_label.configure(text="READY", text_color="#444")
        self.symbol_label.configure(text_color=CYBER_GREEN)
        self.tips_label.configure(text="Awaiting input for heuristic analysis.")

if __name__ == "__main__":
    app = PassCheckApp()
    app.mainloop()
