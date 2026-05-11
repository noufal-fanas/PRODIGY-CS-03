# 🛡️ PassCheck v4.4 | Real-time Identity Analyzer

**PRODIGY INFOTECH • CYBERSECURITY INTERNSHIP • TASK 03**

---

## 🔒 PassCheck
**Advanced Password Strength Checker • Python GUI**

![Python 3.13+](https://img.shields.io/badge/Python-3.13+-blue?style=flat-square) 
![CustomTkinter GUI](https://img.shields.io/badge/CustomTkinter-GUI-green?style=flat-square) 
![Pillow](https://img.shields.io/badge/Pillow-Image--Processing-blueviolet?style=flat-square&logo=python&logoColor=white)
![MIT License](https://img.shields.io/badge/License-MIT-orange?style=flat-square) 
![Security Checked](https://img.shields.io/badge/Local-No--Dependencies-lightgrey?style=flat-square)

**Developer:** NOUFAL N S  
**Organization:** Prodigy Infotech  


---

### 📋 OVERVIEW
**About the Project**
PassCheck is a real-time password strength analyzer built with Python and CustomTkinter. It evaluates passwords using length checks, character variety, and heuristic entropy calculations. Unlike standard checkers, v4.4 implements a "monoculture penalty" to ensure that long but predictable passwords (like alphabet-only strings) are correctly identified as weak.

### ⚙️ WHAT IT DOES
* **Real-time strength bar** (Dynamic color transitions from Critical to Secure).
* **Heuristic Entropy analysis** (Assesses mathematical complexity).
* **8-point criteria checklist** (Covers symbols, numbers, and case sensitivity).
* **Smart improvement suggestions** (Explains exactly what is missing).
* **Dynamic Symbol feedback** (The central shield icon reacts to your input).
* **Privacy-First** (All analysis runs 100% locally; no data leaves your device).

---

### 🛠️ HOW IT WORKS

| Step | Action | Detail |
| :--- | :--- | :--- |
| **01** | **Scan** | Each character type is scanned using regex patterns. |
| **02** | **Score** | Base score is tallied over core complexity criteria. |
| **03** | **Logic** | Heuristic variety check ensures high entropy. |
| **04** | **Map** | Strength percentage maps to dynamic labels and colors. |
| **05** | **Feedback** | Specific suggestions are generated for security gaps. |
| **06** | **Finalize** | UI updates to "SECURE" only when all criteria are met. |

---

### 📊 STRENGTH LEVELS

| 🔴 **Critical** | 🔴 **Weak** | 🟠 **Fair** | 🟢 **Strong** | 🟢 **Secure** |
| :--- | :--- | :--- | :--- | :--- |
| < 20% | 20-40% | 40-60% | 60-80% | 90-100% |

---

### ✅ CRITERIA CHECKED

* [x] **8+ characters** (Base complexity)
* [x] **12+ characters** (Enhanced length)
* [x] **16+ characters** (Maximum length bonus)
* [x] **Uppercase (A-Z)**
* [x] **Lowercase (a-z)**
* [x] **Numbers (0-9)**
* [x] **Symbols (!@#$%^)**
* [x] **Diversity Hard-Cap** (Prevents alphabet-only "false positives")

---

### 🚀 INSTALLATION

1. **Clone the repository**
   ```bash
   git clone [https://github.com/noufal-fanas/PRODIGY-CS-03.git]
   ```
2. **Install dependencies**

    ```Bash
    pip install -r requirements.txt
    ```
3. **Run the application**

    ```Bash
    python pass-check.py
    ```

### 🤝 Credits & Branding

   **Developer:** NOUFAL N S  
   **Organization:** Prodigy Infotech  
   **TASK:** TASK 03
    
This tool is for educational and security assessment purposes only.
