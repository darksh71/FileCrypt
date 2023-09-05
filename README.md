# FileCrypt

## Overview

FileCrypt is a Python application that provides a graphical user interface (GUI) for encrypting and decrypting files using the Fernet symmetric key encryption algorithm from the `cryptography` library. It allows you to secure your files with strong encryption and easily decrypt them when needed.

## Key Features

- **Encryption**: You can select a file, and FileCrypt will encrypt it using a randomly generated encryption key. The original file is removed after successful encryption.

- **Decryption**: To decrypt a file, simply select the encrypted file, and FileCrypt will decrypt it using the correct encryption key. The decrypted file retains its original extension.

## Technologies Used

- Python
- tkinter (for the GUI)
- cryptography (for encryption and decryption)

## Usage

1. **Installation**:
    - Clone or download this repository.
    - Install the required libraries using `pip install cryptography` if you haven't already.
    - Run the `encryption_tool.py` script to launch the application.

2. **Encryption**:
    - Launch the application.
    - Click the "Browse" button to select a file.
    - Click the "Encrypt" button to encrypt the file.
    - The original file is removed after successful encryption.

3. **Decryption**:
    - To decrypt a file, click the "Browse" button again and select the encrypted file.
    - Click the "Decrypt" button.
    - The decrypted file retains its original extension.

## Project Details

The project successfully provides a user-friendly way to encrypt and decrypt files, enhancing data security.

### Your Contribution

As the sole developer of this project, my contributions included:
- Designing the user interface.
- Implementing the file encryption and decryption functionalities.
- Testing and refining the application.
