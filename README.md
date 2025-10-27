# Lab5_Static_Code_Analysis
# Lab 5 – Static Code Analysis

## Objective
To analyze and improve Python code quality, security, and style using **Pylint**, **Flake8**, and **Bandit**.  
These tools helped detect logic, formatting, and security issues in `inventory_system.py`.

---

## Tools Used
| Tool | Purpose |
|------|----------|
| **Pylint** | Detects coding convention, logic, and quality issues |
| **Flake8** | Checks code formatting based on PEP8 |
| **Bandit** | Detects security vulnerabilities |

---

## Issue Documentation Table

| Tool | Type | Issue Found | Line(s) | Severity | Fix Applied |
|------|------|--------------|----------|-----------|--------------|
| **Pylint** | Documentation | Missing module and function docstrings | 1, 8, 14, 22, 25, 31, 36, 41 | Low | Added descriptive docstrings |
| **Pylint** | Naming | Function names not in `snake_case` | 8–41 | Low | Renamed all to follow naming convention |
| **Pylint** | Logic | Dangerous default value `[]` as argument | 8 | Medium | Changed to `None` and initialized inside function |
| **Pylint** | Error Handling | Bare `except:` used | 19 | Medium | Replaced with `except KeyError as e:` |
| **Pylint / Bandit** | Security | Use of `eval()` function | 59 | High | Removed and replaced with `ast.literal_eval()` |
| **Bandit** | Error Handling | Try/Except/Pass detected | 19 | Medium | Added proper exception handling |
| **Flake8** | Import | Unused `logging` import | 2 | Low | Removed unused import |
| **Flake8** | Formatting | Missing blank lines | 8–61 | Low | Added blank lines between functions |

---

## Summary of Fixes
✅ Added docstrings for clarity  
✅ Renamed functions to follow Python conventions  
✅ Removed unsafe `eval()` and bare `except:`  
✅ Used encoding in file operations  
✅ Removed unused imports  
✅ Improved code formatting and readability  

---

## Reflection Questions

### **1. Which issues were the easiest to fix, and which were the hardest? Why?**
The easiest issues were missing docstrings and formatting (Flake8), since they only required simple text edits.  
The hardest were fixing `eval()` and bare `except:` because they needed understanding of the program’s logic and safe replacements.

---

### **2. Did the static analysis tools report any false positives?**
Yes. *Pylint* warned about using a global variable. In this small script, it didn’t actually cause problems.  
It was more of a suggestion than a true error — showing that some warnings depend on context.

---

### **3. How would you integrate static analysis tools into a real development workflow?**
I would set them up in **VS Code** for local checking and also in **GitHub Actions (CI)** to run automatically whenever code is pushed.  
This way, new commits can’t introduce poor style or insecure code.

---

### **4. What tangible improvements did you observe after applying the fixes?**
The code became easier to read, better documented, and more secure.  
Error handling is safer, function names are consistent, and formatting matches professional Python standards.  
It feels like production-ready code instead of a basic script.

---

## Deliverables
- `inventory_system.py` (fixed code)  
- `pylint_report.txt`, `flake8_report.txt`, `bandit_report.txt`  
- `Static_Code_Analysis_Report.pdf`  
- `README.md` (this file)

---

*Authored by:* **[Lasya Sriya]**  
*Date:* 27 October 2025
