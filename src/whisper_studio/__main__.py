"""
WhisperStudio Pro - Main Entry Point
"""

import sys
from PyQt6.QtWidgets import QApplication
from .gui.main_window import WhisperStudioGUI

def main():
    """Application entry point"""
    app = QApplication(sys.argv)
    window = WhisperStudioGUI()
    window.show()
    return app.exec()

if __name__ == '__main__':
    sys.exit(main())