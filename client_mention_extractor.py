import tkinter as tk
from tkinter import filedialog, messagebox
import os

def extract_sentences(keyword, input_path, output_path):
    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            text = file.read()

        sentences = text.replace('\n', ' ').split('.')
        matched_sentences = [sentence.strip() + '.' for sentence in sentences if keyword.lower() in sentence.lower()]

        with open(output_path, 'w', encoding='utf-8') as file:
            for sentence in matched_sentences:
                file.write(sentence + '\n')

        messagebox.showinfo("Success", f"Found {len(matched_sentences)} sentences. Saved to {output_path}")

    except Exception as e:
        messagebox.showerror("Error", str(e))

def select_input_file():
    file_path = filedialog.askopenfilename(title="Select input text file", filetypes=[("Text Files", "*.txt")])
    if file_path:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, file_path)

def select_output_file():
    file_path = filedialog.asksaveasfilename(title="Save output as", defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, file_path)

def start_extraction():
    keyword = keyword_entry.get()
    input_path = input_entry.get()
    output_path = output_entry.get()

    if not keyword or not input_path or not output_path:
        messagebox.showwarning("Missing Information", "Please fill in all fields.")
        return

    extract_sentences(keyword, input_path, output_path)

# GUI setup
root = tk.Tk()
root.title("Client Mention Extractor")
root.geometry("500x250")

# Input file selection
tk.Label(root, text="Input File:").pack(pady=5)
input_entry = tk.Entry(root, width=50)
input_entry.pack()
tk.Button(root, text="Browse", command=select_input_file).pack(pady=5)

# Output file selection
tk.Label(root, text="Output File:").pack(pady=5)
output_entry = tk.Entry(root, width=50)
output_entry.pack()
tk.Button(root, text="Save As", command=select_output_file).pack(pady=5)

# Keyword entry
tk.Label(root, text="Keyword:").pack(pady=5)
keyword_entry = tk.Entry(root, width=50)
keyword_entry.pack()

# Start button
tk.Button(root, text="Extract Sentences", command=start_extraction, bg="green", fg="white").pack(pady=10)

root.mainloop()
