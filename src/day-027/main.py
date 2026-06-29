# https://docs.python.org/3/library/tkinter.html
import tkinter as tk

window = tk.Tk()

window.title("My First GUI Program")

window.minsize(width=500, height=300)

my_label = tk.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label.config(text="New Text")

def button_clicked():
  # my_label.config(text="Button got clicked")
  # print("I got clicked")
  my_label.config(text=input.get())

button = tk.Button(text="Click Me", command=button_clicked)
button.pack()

input = tk.Entry(width=50)
input.pack()













window.mainloop()