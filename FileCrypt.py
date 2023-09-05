import tkinter as tk
from tkinter import filedialog
from cryptography.fernet import Fernet
import os

# Function to generate or load the encryption key
def generate_or_load_key(key_file_path):
    if os.path.isfile(key_file_path):
        with open(key_file_path, "rb") as key_file:
            key = key_file.read()
    else:
        key = Fernet.generate_key()
        with open(key_file_path, "wb") as key_file:
            key_file.write(key)
    return key

# Function to encrypt a file
def encrypt_file():
    file_path = entry_path.get()
    try:
        with open(file_path, "rb") as file:
            file_data = file.read()
            encrypted_data = cipher_suite.encrypt(file_data)
        
        encrypted_file_path = file_path + ".encrypted"
        with open(encrypted_file_path, "wb") as encrypted_file:
            encrypted_file.write(encrypted_data)
        
        os.remove(file_path)  # Remove the original file after encryption
        
        label_status.config(text="File encrypted successfully.")
    except Exception as e:
        label_status.config(text=f"Error: {str(e)}")

# Function to decrypt a file
def decrypt_file():
    file_path = entry_path.get()
    try:
        with open(file_path, "rb") as encrypted_file:
            encrypted_data = encrypted_file.read()
            decrypted_data = cipher_suite.decrypt(encrypted_data)
        
        decrypted_file_path, _ = os.path.splitext(file_path)
        with open(decrypted_file_path, "wb") as decrypted_file:
            decrypted_file.write(decrypted_data)
        
        os.remove(file_path)  # Remove the old encrypted file after decryption
        
        label_status.config(text="File decrypted successfully.")
    except Exception as e:
        label_status.config(text=f"Error: {str(e)}")

# Create a GUI window
window = tk.Tk()
window.title("File Encryption/Decryption Tool")

# Create and place widgets in the window
label_developer = tk.Label(window, text="Developed by 71 from Blackdot", font=("Helvetica", 10, "italic"))
label_developer.pack(anchor="nw")

label_instructions = tk.Label(window, text="Enter the path of the file to encrypt/decrypt:")
label_instructions.pack()

entry_path = tk.Entry(window, width=50)
entry_path.pack()

button_browse = tk.Button(window, text="Browse", command=lambda: entry_path.insert(0, filedialog.askopenfilename()))
button_browse.pack()

button_encrypt = tk.Button(window, text="Encrypt", command=encrypt_file)
button_encrypt.pack()

button_decrypt = tk.Button(window, text="Decrypt", command=decrypt_file)
button_decrypt.pack()

label_status = tk.Label(window, text="")
label_status.pack()

# Generate or load the encryption key
key_file_path = "encryption_key.key"
key = generate_or_load_key(key_file_path)
cipher_suite = Fernet(key)

# Start the GUI event loop
window.mainloop()
