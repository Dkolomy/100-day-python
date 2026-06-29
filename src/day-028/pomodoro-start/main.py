from cgitb import reset
import tkinter as tk
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
  global reps
  global timer
  window.after_cancel(timer)
  reps = 0
  title_label.config(text="Timer", fg=GREEN)
  canvas.itemconfig(timer_text, text="00:00")
  checkmarks.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
  global reps
  reps += 1
  if reps % 8 == 0:
    countdown(LONG_BREAK_MIN * 60)
    title_label.config(text="Break", fg=RED)
  elif reps % 2 == 0:
    countdown(SHORT_BREAK_MIN * 60)
    title_label.config(text="Break", fg=PINK)
  else:
    countdown(WORK_MIN * 60)
    title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
  global timer
  count_min = math.floor(count / 60)
  count_sec = count % 60

  canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")
  if count > 0:
    timer = window.after(1000, countdown, count - 1)
  else:
    start_timer()
    mark = ""
    work_sessions = math.floor(reps / 2)
    for _ in range(work_sessions):
      mark += "✔"
    checkmarks.config(text=mark)
  
# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = tk.Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = tk.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# checkmarks = tk.Label(text="✔", font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN, highlightthickness=0)
checkmarks = tk.Label(font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN, highlightthickness=0)
checkmarks.grid(column=1, row=3)

window.mainloop()