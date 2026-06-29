import tkinter as tk

def calculate_km():
  miles = float(input.get())
  km = round(miles * 1.609, 2)
  result_label.config(text=f"{km}")

window = tk.Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=500, height=300)

miles_label = tk.Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = tk.Label(text="Km")
km_label.grid(column=2, row=1)

equal_label = tk.Label(text="is equal to")
equal_label.grid(column=0, row=1)

result_label = tk.Label(text="0")
result_label.grid(column=1, row=1)

input = tk.Entry(width=10)
input.grid(column=1, row=0)

calculate_button = tk.Button(text="Calculate", command=calculate_km)
calculate_button.grid(column=1, row=2)

window.mainloop()