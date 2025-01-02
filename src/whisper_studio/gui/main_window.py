from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog
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

        # Add title
        title_label = QLabel('WhisperStudio Pro')
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        # Add file selection button
        select_file_button = QPushButton('Select Audio File')
        select_file_button.clicked.connect(self.select_file)
        layout.addWidget(select_file_button)

        # Add transcription button
        self.transcribe_button = QPushButton('Start Transcription')
        self.transcribe_button.clicked.connect(self.start_transcription)
        self.transcribe_button.setEnabled(False)
        layout.addWidget(self.transcribe_button)

        # Add status label
        self.status_label = QLabel('Select an audio file to begin')
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.status_label)

    def select_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Select Audio File', '',
            'Audio Files (*.mp3 *.wav *.m4a *.ogg);;All Files (*)')
        if file_name:
            self.audio_file = file_name
            self.transcribe_button.setEnabled(True)
            self.status_label.setText(f'Selected file: {file_name}')

    def start_transcription(self):
        self.status_label.setText('Transcription in progress...')
        self.transcribe_button.setEnabled(False)
