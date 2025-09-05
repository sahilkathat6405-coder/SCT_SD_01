import tkinter as tk
from tkinter import ttk

# ----------------- Conversion Logic -----------------
def convert_temperature():
    try:
        temp = float(entry_temp.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()

        # Convert to Celsius
        if from_unit == "Celsius":
            celsius = temp
        elif from_unit == "Fahrenheit":
            celsius = (temp - 32) * 5 / 9
        elif from_unit == "Kelvin":
            celsius = temp - 273.15

        # Convert from Celsius
        if to_unit == "Celsius":
            result = celsius
        elif to_unit == "Fahrenheit":
            result = (celsius * 9 / 5) + 32
        elif to_unit == "Kelvin":
            result = celsius + 273.15

        result_var.set(f"{temp:.2f} {from_unit} = {result:.2f} {to_unit}")
    except ValueError:
        result_var.set("❗ Invalid input. Enter a number.")

def clear_fields():
    entry_temp.delete(0, tk.END)
    result_var.set("")

# ----------------- GUI Setup -----------------
root = tk.Tk()
root.title("🌡️ Temperature Converter")
root.geometry("420x300")
root.configure(bg="#1e1e1e")  # Dark background

# ----- Styling -----
style = ttk.Style()
style.theme_use("clam")

style.configure("TLabel", background="#1e1e1e", foreground="white", font=("Segoe UI", 11))
style.configure("TButton", background="#333333", foreground="white", font=("Segoe UI", 11))
style.configure("TCombobox", fieldbackground="#333333", background="#333333", foreground="white")
style.map("TButton", background=[("active", "#444444")])

# ----- Widgets -----
ttk.Label(root, text="Enter Temperature:").pack(pady=(15, 5))
entry_temp = ttk.Entry(root, font=("Segoe UI", 11), width=20)
entry_temp.pack(pady=5)

ttk.Label(root, text="From:").pack(pady=(10, 2))
combo_from = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly", width=18)
combo_from.current(0)
combo_from.pack()

ttk.Label(root, text="To:").pack(pady=(10, 2))
combo_to = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly", width=18)
combo_to.current(1)
combo_to.pack()

ttk.Button(root, text="Convert", command=convert_temperature).pack(pady=15)
ttk.Button(root, text="Clear", command=clear_fields).pack()

result_var = tk.StringVar()
ttk.Label(root, textvariable=result_var, font=("Segoe UI", 12)).pack(pady=15)

# ----------------- Run App -----------------
root.mainloop()
