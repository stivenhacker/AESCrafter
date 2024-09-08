
# 🔐 AESCrafter - Secure Key Generation Tool

**AESCrafter** is a lightweight, highly efficient Python script developed to generate secure 128-bit AES keys for cryptographic purposes. Whether you're developing encryption algorithms, securing communications, or creating secure API keys, AESCrafter is a fast, simple, and reliable solution.

---

## ✨ Features

- **Secure Key Generation:** Creates a 16-byte (128-bit) AES key using Python's cryptographically secure random generator `os.urandom`.
- **Hexadecimal Conversion:** Converts the raw binary key into a 32-character hexadecimal string for easy use in various applications.
- **Key Verification:** Automatically verifies that the generated key has the correct length of 32 characters to ensure cryptographic validity.
- **Quick and Simple:** Generates and outputs the key in a matter of seconds, with no complicated setup required.

---

## ⚙️ Usage

Running **AESCrafter** is straightforward and requires no special configuration:

1. **Clone the repository:**  
   ```bash
   git clone https://github.com/stivenhacker/AESCrafter.git
   ```

2. **Navigate to the project directory:**  
   ```bash
   cd AESCrafter
   ```

3. **Run the script:**  
   ```bash
   python AESKeyGen32.py
   ```

4. **Receive your 32-character AES key!**

The output will display the key and its length, confirming that the key generation was successful:
```
32-character AES key: [Your AES Key]
Key length: 32
```

---

## 💻 Requirements

AESCrafter is extremely lightweight and has minimal dependencies:

- **Python 3.x**: Required to run the script. You can install Python from the official website if needed: [python.org](https://www.python.org/downloads/)

No external libraries are needed to run this script. Simply download and execute!

---

## ⚠️ Disclaimer

This script is designed for educational and legitimate cryptographic purposes only. Misuse of AESCrafter for illegal activities is strictly prohibited. The author **@Stiven.Hacker** takes no responsibility for any damage or misuse caused by this code.

---

## 🛠️ Contributions

We welcome any contributions or suggestions! Feel free to submit a pull request or open an issue for improvement. Let's make cryptography simple and secure for everyone.