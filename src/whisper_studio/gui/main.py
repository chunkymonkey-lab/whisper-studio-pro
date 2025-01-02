import sys
from PyQt6.QtWidgets import QApplication
from whisper_studio.core.application import WhisperStudioGUI

def main():
    app = QApplication(sys.argv)
    window = WhisperStudioGUI()
    window.show()
    sys.exit(app.exec())