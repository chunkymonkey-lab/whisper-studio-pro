#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import QApplication
from whisper_studio.gui.main_window import WhisperStudioGUI

def main():
    app = QApplication(sys.argv)
    window = WhisperStudioGUI()
    window.show()
    return app.exec()

if __name__ == '__main__':
    sys.exit(main())
