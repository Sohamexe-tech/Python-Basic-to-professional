import tkinter as tk
from tkinter import messagebox

def convert():
    try:
        value = entry_value.get()

        # Empty field check
        if value == "":
            raise ValueError("Input field cannot be empty")

        value = float(value)

        choice = conversion.get()

        if choice == 1:
            result = value / 60
            output.set(f"{value} Seconds  -->  {result:.2f} Minutes")

        elif choice == 2:
            result = value / 60
            output.set(f"{value} Minutes  -->  {result:.2f} Hours")

        elif choice == 3:
            result = value / 1000
            output.set(f"{value} Meters  -->  {result:.2f} Kilometers")

        elif choice == 4:
            result = value * 0.621371
            output.set(f"{value} Kilometers  -->  {result:.2f} Miles")

        elif choice == 5:
            result = value * 3.6
            output.set(f"{value} m/s  -->  {result:.2f} km/h")

        elif choice == 6:
            result = value * 0.621371
            output.set(f"{value} km/h  -->  {result:.2f} mph")

        else:
            raise ValueError("Please select a conversion type")

    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))


root = tk.Tk()
root.title("Unit Converter")
root.geometry("500x550")
root.configure(bg="#2b2b2b")

conversion = tk.IntVar()
output = tk.StringVar()

tk.Label(root, text="Unit Converter", fg="white", bg="#2b2b2b",
         font=("Arial", 20, "bold")).pack(pady=10)

tk.Label(root, text="Enter Value", fg="white", bg="#2b2b2b",
         font=("Arial", 12)).pack()

entry_value = tk.Entry(root, font=("Arial", 14), justify="center")
entry_value.pack(pady=10)

tk.Label(root, text="Choose Conversion (From --> To)",
         fg="white", bg="#2b2b2b", font=("Arial", 12)).pack(pady=10)

tk.Label(root, text="Time", fg="yellow", bg="#2b2b2b",
         font=("Arial", 12, "bold")).pack(anchor="w", padx=80)

tk.Radiobutton(root, text="Seconds --> Minutes", variable=conversion,
               value=1, bg="#2b2b2b", fg="white",
               selectcolor="#2b2b2b").pack(anchor="w", padx=100)

tk.Radiobutton(root, text="Minutes --> Hours", variable=conversion,
               value=2, bg="#2b2b2b", fg="white",
               selectcolor="#2b2b2b").pack(anchor="w", padx=100)

tk.Label(root, text="Distance", fg="yellow", bg="#2b2b2b",
         font=("Arial", 12, "bold")).pack(anchor="w", padx=80, pady=5)

tk.Radiobutton(root, text="Meters --> Kilometers", variable=conversion,
               value=3, bg="#2b2b2b", fg="white",
               selectcolor="#2b2b2b").pack(anchor="w", padx=100)

tk.Radiobutton(root, text="Kilometers --> Miles", variable=conversion,
               value=4, bg="#2b2b2b", fg="white",
               selectcolor="#2b2b2b").pack(anchor="w", padx=100)


tk.Label(root, text="Speed", fg="yellow", bg="#2b2b2b",
         font=("Arial", 12, "bold")).pack(anchor="w", padx=80, pady=5)

tk.Radiobutton(root, text="m/s --> km/h", variable=conversion,
               value=5, bg="#2b2b2b", fg="white",
               selectcolor="#2b2b2b").pack(anchor="w", padx=100)

tk.Radiobutton(root, text="km/h --> mph", variable=conversion,
               value=6, bg="#2b2b2b", fg="white",
               selectcolor="#2b2b2b").pack(anchor="w", padx=100)

tk.Button(root, text="Convert", command=convert,
          font=("Arial", 12, "bold"), bg="gray", width=12).pack(pady=20)

tk.Label(root, textvariable=output, fg="yellow",
         bg="#2b2b2b", font=("Arial", 14, "bold")).pack()

root.mainloop()
