# 🔢 Bisection Method in Python

This project implements the **Bisection Method** for finding the root of a given function in **Python**.  
The user provides the initial interval `[a, b]` and the tolerance `epsilon` to compute an approximate root.

---

## 📌 Features

- Implements the numerical **Bisection Method** to find roots  
- Allows user-defined precision through `epsilon`  
- Output is formatted with decimal places matching the given `epsilon`  
- Checks that `f(a)` and `f(b)` have opposite signs before starting  

---

## ⚠️ Input Format

- Enter `a` and `b` as **decimal numbers** (e.g., `2`, `3`, `0.5`)  
- Enter `epsilon` **in decimal format, not scientific notation** (e.g., `0.0001` instead of `1e-4`)  
- If `f(a)` and `f(b)` do not have opposite signs, the method will fail  

---

## 🛠️ How to Run

1. Clone or download the project:  
```bash
git clone <project-link>
cd <project-folder>
