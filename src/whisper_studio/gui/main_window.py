from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt
from ..core.transcription import TranscriptionWorker

class WhisperStudioGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('WhisperStudio Pro')
        self.setMinimumSize(800, 600)
        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        title_label = QLabel('WhisperStudio Pro')
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        start_button = QPushButton('Start Transcription')
        start_button.clicked.connect(self.start_transcription)
        layout.addWidget(start_button)

    def start_transcription(self):
        # Placeholder for transcription functionality
        pass
