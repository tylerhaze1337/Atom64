import sys
import base64
import os
import random
import string
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QLineEdit, QMessageBox, QComboBox
from PyQt5.QtGui import QIcon

class ObfuscatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.languages = {
            'en': {
                'file_label': "Select your file:",
                'fake_size_label': "Fake size to add (in KB):",
                'browse_button': "Browse",
                'obfuscate_button': "Obfuscate",
                'error_file': "Please select a valid file.",
                'error_format': "Unsupported file format.",
                'success_message': "Obfuscated file saved at: ",
            },
            'fr': {
                'file_label': "Selectionner votre fichier :",
                'fake_size_label': "Taille fictive a ajouter (en KB) :",
                'browse_button': "Parcourir",
                'obfuscate_button': "Obfusquer",
                'error_file': "Veuillez selectionner un fichier valide.",
                'error_format': "Format de fichier non supporte.",
                'success_message': "Fichier obfusque enregistre a : ",
            }
        }
        self.current_language = 'en'  # Default language
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Atom64")
        self.setWindowIcon(QIcon("atom64.jpg"))
        self.resize(400, 300)

        # Style spatial
        self.setStyleSheet("""
            QWidget {
                background-color: #0f172a;
                color: #e0f2fe;
                font-family: 'Segoe UI', sans-serif;
                font-size: 14px;
            }

            QLabel {
                margin-top: 10px;
                margin-bottom: 5px;
                color: #bae6fd;
            }

            QLineEdit {
                background-color: #1e293b;
                border: 1px solid #3b82f6;
                border-radius: 8px;
                padding: 6px 10px;
                color: #e0f2fe;
            }

            QPushButton {
                background-color: #3b82f6;
                border: none;
                border-radius: 8px;
                padding: 8px 12px;
                color: white;
                font-weight: bold;
                margin-top: 10px;
            }

            QPushButton:hover {
                background-color: #2563eb;
            }

            QPushButton:pressed {
                background-color: #1d4ed8;
            }
        """)

        self.layout = QVBoxLayout()

        # Language Selector
        self.language_selector = QComboBox(self)
        self.language_selector.addItem("English", 'en')
        self.language_selector.addItem("Francais", 'fr')
        self.language_selector.currentIndexChanged.connect(self.change_language)
        self.layout.addWidget(self.language_selector)

        # Labels and Inputs
        self.label = QLabel(self.languages[self.current_language]['file_label'])
        self.layout.addWidget(self.label)

        self.file_input = QLineEdit(self)
        self.layout.addWidget(self.file_input)

        self.browse_button = QPushButton(self.languages[self.current_language]['browse_button'], self)
        self.browse_button.clicked.connect(self.browse_file)
        self.layout.addWidget(self.browse_button)

        self.fake_size_label = QLabel(self.languages[self.current_language]['fake_size_label'])
        self.layout.addWidget(self.fake_size_label)

        self.fake_size_input = QLineEdit(self)
        self.layout.addWidget(self.fake_size_input)

        self.obfuscate_button = QPushButton(self.languages[self.current_language]['obfuscate_button'], self)
        self.obfuscate_button.clicked.connect(self.obfuscate_file)
        self.layout.addWidget(self.obfuscate_button)

        self.setLayout(self.layout)

    def change_language(self):
        """Change the language of the interface"""
        selected_lang = self.language_selector.currentData()
        if selected_lang != self.current_language:
            self.current_language = selected_lang
            self.update_ui()

    def update_ui(self):
        """Update all labels and buttons to the selected language"""
        self.label.setText(self.languages[self.current_language]['file_label'])
        self.fake_size_label.setText(self.languages[self.current_language]['fake_size_label'])
        self.browse_button.setText(self.languages[self.current_language]['browse_button'])
        self.obfuscate_button.setText(self.languages[self.current_language]['obfuscate_button'])

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, self.languages[self.current_language]['file_label'], "", "Scripts (*.bat *.cmd *.ps1 *.sh *.js *.php)"
        )
        if file_path:
            self.file_input.setText(file_path)

    def generate_random_name(self, ext):
        return ''.join(random.choices("IlI1l", k=16)) + ext

    def obfuscate_file(self):
        file_path = self.file_input.text()
        fake_size = self.fake_size_input.text()

        if not file_path or not os.path.isfile(file_path):
            QMessageBox.critical(self, "Error", self.languages[self.current_language]['error_file'])
            return

        try:
            with open(file_path, "r") as f:
                content = f.read()

            encoded = base64.b64encode(content.encode()).decode()

            if fake_size.isdigit():
                padding_size = int(fake_size) * 1024
                encoded += base64.b64encode(os.urandom(padding_size)).decode()

            extension = os.path.splitext(file_path)[1].lower()

            if extension in ['.bat', '.cmd']:
                txt_name = self.generate_random_name(".txt")
                script_name = self.generate_random_name(".bat")
                obfuscated_script = (
                    f"@echo off\n"
                    f"echo {encoded} > {txt_name}\n"
                    f"certutil -decode {txt_name} {script_name} >nul 2>&1\n"
                    f"call {script_name}\n"
                    f"del {txt_name}\n"
                    f"del {script_name}\n"
                )

            # Similar code for other formats like .ps1, .sh, .js, .php...

            obfuscated_file_path = file_path + ".obfuscated" + extension
            with open(obfuscated_file_path, "w") as f:
                f.write(obfuscated_script)

            QMessageBox.information(self, "Success", self.languages[self.current_language]['success_message'] + obfuscated_file_path)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ObfuscatorApp()
    window.show()
    sys.exit(app.exec_())
