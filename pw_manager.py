import tkinter as tk
import json
from cryptography.fernet import Fernet
import random
import string
import os

class PasswordManager:
    current_directory = os.getcwd()
    folder_directory = f"{current_directory}\\pw_manager_files"
    pw_json_file_path = f"{folder_directory}\\passwords.json"    
    
    def __init__(self, master):
        self.master = master
        self.master.title("Password Manager")
        self.master.geometry("400x400")

        self.load_encryption_key()
        self.load_passwords()

        self.create_widgets()

    def load_encryption_key(self):
        # Check if the key file exists
        try:
            with open('key.key', 'rb') as key_file:
                self.encryption_key = key_file.read()
        except FileNotFoundError:
            # Generate a new key if it doesn't exist
            self.encryption_key = Fernet.generate_key()
            with open('key.key', 'wb') as key_file:
                key_file.write(self.encryption_key)

        self.cipher_suite = Fernet(self.encryption_key)

    def load_passwords(self):
        try:
            with open(self.pw_json_file_path, 'r') as f:
                self.passwords = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            self.passwords = {}

    def save_passwords(self):
        with open(self.pw_json_file_path, 'w') as f:
            json.dump(self.passwords, f, indent=4)

    def generate_password(self):
        password_length = 12  # You can adjust the password length as needed
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(password_length))
        encrypted_password = self.cipher_suite.encrypt(password.encode())
        url = self.url_entry.get()
        username = self.username_entry.get()
        self.passwords[url] = {
            "username": username,
            "password": encrypted_password.decode()
        }
        self.save_passwords()
        self.screen2.destroy()
        self.update_url_list()

    def open_screen2(self):
        self.screen2 = tk.Toplevel(self.master)
        self.screen2.title("Create New Password")

        tk.Label(self.screen2, text="URL:").pack()
        self.url_entry = tk.Entry(self.screen2)
        self.url_entry.pack()

        tk.Label(self.screen2, text="Username:").pack()
        self.username_entry = tk.Entry(self.screen2)
        self.username_entry.pack()

        tk.Button(self.screen2, text="Generate Password", command=self.generate_password).pack()

    def open_screen3(self, url):
        screen3 = tk.Toplevel(self.master)
        screen3.title(f"Password for {url}")

        decrypted_password = self.cipher_suite.decrypt(self.passwords[url]["password"].encode())

        tk.Label(screen3, text=f"Username: {self.passwords[url]['username']}").pack()
        tk.Label(screen3, text=f"Password: {decrypted_password.decode()}").pack()

    def update_url_list(self):
        self.url_listbox.delete(0, tk.END)
        for url in self.passwords:
            self.url_listbox.insert(tk.END, url)

    def create_widgets(self):
        self.url_listbox = tk.Listbox(self.master)
        self.url_listbox.pack()
        self.update_url_list()

        tk.Button(self.master, text="Create New", command=self.open_screen2).pack()
        tk.Button(self.master, text="Close", command=self.master.quit).pack()

        self.url_listbox.bind("<Double-Button-1>", lambda event: self.open_screen3(self.url_listbox.get(self.url_listbox.curselection())))

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManager(root)
    root.mainloop()