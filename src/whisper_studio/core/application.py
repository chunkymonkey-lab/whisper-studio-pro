from PyQt6.QtWidgets import QMainWindow
from ..utils.system import SystemMonitor

class WhisperStudioGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WhisperStudio Pro")
        self.setup_ui()

    def setup_ui(self):
        # UI implementation will go here
        pass