# **XO Game (Tic-Tac-Toe) – Python**

A simple console-based XO (Tic-Tac-Toe) game built during **Day 7 of my Hands-on Python Internship under Linux World**.
This mini-project focuses on Python basics, game logic, and interactive user input.

---

## **📌 Features**

* Two-player console gameplay
* Clean and simple interface
* Checks for wins, draws, and invalid moves
* Easy-to-read and beginner-friendly code
* Fully terminal-based, no external libraries

---

## **📂 Project Structure**

```
xo_game.py   # Main game file
README.md    # Project documentation
```

---

## **🕹️ How to Play**

1. Run the script in any Python environment.
2. Players take turns entering positions (1–9).
3. Game shows the updated board after each move.
4. Winner is declared when any row, column, or diagonal matches.
5. If all spots fill with no winner — it's a draw.

---

## **🚀 Run the Game**

Open a terminal and type:

```bash
python xo_game.py
```

---

## **📜 Code Snippet**

Here’s a small preview:

```python
board = [" " for _ in range(9)]

def print_board():
    print(f" {board[0]} | {board[1]} | {board[2]} ")
```

(Full code inside the file)

---



## **💡 Improvements for Future**

* Add AI opponent
* GUI using Tkinter
* Sound effects
* Move history / scoreboard

---

If you want, I can also generate a **GitHub-optimized version**, a **short version**, or add **badges, license, or installation steps**.
