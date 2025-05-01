import tkinter as tk
from tkinter import messagebox
import subprocess
import sys

def install_package():
    package = entry.get().strip()
    if not package:
        messagebox.showwarning("Input Required", "Please enter a package name.")
        return

    output_text.delete(1.0, tk.END)
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", package],
            capture_output=True,
            text=True
        )

        output = result.stdout + "\n" + result.stderr
        output_text.insert(tk.END, output)

        if result.returncode == 0:
            messagebox.showinfo("Success", f"'{package}' installed successfully!")
        else:
            messagebox.showerror("Error", f"Failed to install '{package}'.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def show_installed_packages():
    output_text.delete(1.0, tk.END)
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "list"],
            capture_output=True,
            text=True
        )
        output_text.insert(tk.END, result.stdout)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Pip Package Installer")
root.geometry("550x350")

tk.Label(root, text="Enter Package Name:").pack(pady=5)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Install", command=install_package, bg="blue", fg="white").pack(side="left", padx=5)
tk.Button(button_frame, text="Show Installed Packages", command=show_installed_packages, bg="green", fg="white").pack(side="left", padx=5)

output_text = tk.Text(root, wrap="word", height=12)
output_text.pack(fill="both", expand=True, padx=10, pady=10)

root.mainloop()
