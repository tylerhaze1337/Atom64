# Atom64 - File Obfuscation Tool 🚀

![atom64 - Copie](https://github.com/user-attachments/assets/acf6f008-8d13-427c-8597-805a156405b4)


**Atom64** is a file obfuscation tool designed to **secure and protect your scripts** by adding fake sizes and encoding content in base64. Whether you're a developer looking to hide the internal logic of your scripts or a security enthusiast who wants to obfuscate code for privacy 🔒✨

## Features 🌟

- **Obfuscate various scripts**: Works with `.bat`, `.cmd`, `.ps1`, `.sh`, `.js`, and `.php` files.
- **Easy-to-use GUI**: Built with PyQt5, the app has a sleek, space-inspired interface. 🚀
- **Customizable obfuscation**: You can choose to add **fake file sizes** in kilobytes for extra security. 💼
- **Cross-platform**: Works on Windows, Linux, and macOS.

## How it Works 🔧

### Steps to Obfuscate a File 🔐

1. **Select a file** 🖥️  
   Click on the "Browse" button to choose the file you want to obfuscate.
   
2. **Set fake size** 📏  
   Enter the fake size in kilobytes (KB) to make the file appear larger than it actually is.

3. **Click "Obfuscate"** 🎉  
   Hit the "Obfuscate" button, and Atom64 will take care of encoding the file and adding the fake size.

---

### Demo Screenshot

![image](https://github.com/user-attachments/assets/40dc7ee9-0de3-433e-ac93-240d61a7bebb)


---

## Code Walkthrough 🧑‍💻

Here’s how the app works behind the scenes:

### 1. **GUI Setup** ✨

The program uses **PyQt5** to create a user-friendly interface. The window allows users to input a file and a fake size.

```python
self.setWindowTitle("Atom64")
self.setWindowIcon(QIcon("atom64.jpg"))
self.resize(400, 300)
```

We set up some basic styling to make it look **futuristic and sleek** using QSS (Qt Style Sheets).

### 2. **File Browsing** 🗂️

Users can browse their filesystem to select a script file (`.bat`, `.sh`, `.ps1`, etc.):

```python
file_path, _ = QFileDialog.getOpenFileName(self, "Select a file", "", "Scripts (*.bat *.cmd *.ps1 *.sh *.js *.php)")
```

### 3. **Obfuscation Logic** 🔒

The core functionality of the app encodes the file’s content in **base64** and optionally adds some random padding (based on the fake size). 

```python
with open(file_path, "r") as f:
    content = f.read()

encoded = base64.b64encode(content.encode()).decode()

if fake_size.isdigit():
    padding_size = int(fake_size) * 1024
    encoded += base64.b64encode(os.urandom(padding_size)).decode()
```

This encoding makes it harder for someone to easily read or reverse the script content.

### 4. **Script Generation** 📝

For each supported file type, the program generates an obfuscated version with appropriate decoding commands:

- **Batch Scripts** (`.bat`):
  ```python
  obfuscated_script = f"@echo off\n"
                      f"echo {encoded} > {txt_name}\n"
                      f"certutil -decode {txt_name} {script_name} >nul 2>&1\n"
                      f"call {script_name}\n"
                      f"del {txt_name}\n"
                      f"del {script_name}\n"
  ```

- **PowerShell Scripts** (`.ps1`):
  ```python
  obfuscated_script = f"$b64 = \"{encoded}\"\n"
                      f"Set-Content -Path {txt_name} -Value $b64\n"
                      f"$decoded = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String((Get-Content {txt_name})))\n"
                      f"Set-Content -Path {script_name} -Value $decoded\n"
                      f"powershell -ExecutionPolicy Bypass -File {script_name}\n"
                      f"Remove-Item {txt_name}, {script_name}\n"
  ```

### 5. **Saving the Obfuscated File** 💾

Finally, the obfuscated script is saved to a new file with a `.obfuscated` extension, making it easy to identify.

```python
obfuscated_file_path = file_path + ".obfuscated" + extension
with open(obfuscated_file_path, "w") as f:
    f.write(obfuscated_script)
```

---

## Installation 🚀

### Requirements 🛠️

To run **Atom64**, you'll need Python 3 and PyQt5. Here's how to get everything up and running:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Atom64.git
   cd Atom64
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   python atom64.py
   ```

---

## License 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contributing 🤝

Feel free to fork this project, open issues, or submit pull requests. Contributions are always welcome! 🎉

---

## Final Thoughts 💭

**Atom64** is a powerful yet easy-to-use tool for file obfuscation. It provides an extra layer of security by encoding your scripts and adding fake data, helping protect against unauthorized access or reverse-engineering. Whether you're a developer or a security enthusiast, this tool is a simple and effective way to keep your scripts secure! 🔐💻

---

Voilà ! Ce **README** est à la fois informatif, convivial et clair. Il guide l’utilisateur à travers le fonctionnement du programme et lui permet d’installer et d’utiliser le programme facilement. Si tu as d'autres questions ou des détails supplémentaires à ajouter, je suis là pour t'aider ! 😊
