import tkinter as tk
import json
import os
from cryptography.fernet import Fernet

# Initialize the tkinter app
app = tk.Tk()
app.title("Password Manager")

# Load encryption key or generate a new one
encryption_key = "ipq-LBY9YAMjiM-V_PPAxIOD5elZso09Yg0UhjUVUNY="
cipher_suite = Fernet(encryption_key)

current_directory = os.getcwd()
folder_directory = f"{current_directory}\\pw_manager_files"
pw_file_path = f"{folder_directory}\\password.txt"

# Load existing passwords from the file
try:
    with open(pw_file_path, 'r') as f:
        passwords = json.load(f)
except (json.JSONDecodeError, FileNotFoundError):
    passwords = {}

# Functions
def save_password(url, username, password):
    passwords[url] = {
        "username": username,
        "password": password.decode()
    }
    
    with open(pw_file_path, 'w') as f:
        json.dump(passwords, f)

def generate_password():
    password = b'generated_password_here'
    encrypted_password = cipher_suite.encrypt(password)
    save_password(url_entry.get(), username_entry.get(), encrypted_password)
    screen2.destroy()
    update_url_list()

def open_screen2():
    global screen2
    screen2 = tk.Toplevel(app)
    screen2.title("Create New Password")
    
    tk.Label(screen2, text="URL:").pack()
    global url_entry
    url_entry = tk.Entry(screen2)
    url_entry.pack()
    
    tk.Label(screen2, text="Username:").pack()
    global username_entry
    username_entry = tk.Entry(screen2)
    username_entry.pack()
    
    tk.Button(screen2, text="Generate Password", command=generate_password).pack()

def open_screen3(url):
    screen3 = tk.Toplevel(app)
    screen3.title(f"Password for {url}")
    
    decrypted_password = cipher_suite.decrypt(passwords[url]["password"].encode())
    
    tk.Label(screen3, text=f"Username: {passwords[url]['username']}").pack()
    tk.Label(screen3, text=f"Password: {decrypted_password.decode()}").pack()
    
    tk.Button(screen3, text="Close", command=screen3.destroy).pack()

def update_url_list():
    url_listbox.delete(0, tk.END)
    for url in passwords:
        url_listbox.insert(tk.END, url)

# Screen 1
url_listbox = tk.Listbox(app)
url_listbox.pack()

update_url_list()

tk.Button(app, text="Create New", command=open_screen2).pack()
tk.Button(app, text="Close", command=app.quit).pack()

url_listbox.bind("<Double-Button-1>", lambda event: open_screen3(url_listbox.get(url_listbox.curselection())))

# Start the tkinter main loop
app.mainloop()