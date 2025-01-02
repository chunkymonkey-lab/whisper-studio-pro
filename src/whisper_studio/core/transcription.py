from PyQt6.QtCore import QThread, pyqtSignal
import whisper

class TranscriptionWorker(QThread):
    progress = pyqtSignal(str, int)
    finished = pyqtSignal(str, dict)
    error = pyqtSignal(str, str)

    def __init__(self, file_path, model_name, options):
        super().__init__()
        self.file_path = file_path
        self.model_name = model_name
        self.options = options

    def run(self):
        try:
            self.progress.emit(self.file_path, 10)
            model = whisper.load_model(self.model_name)
            self.progress.emit(self.file_path, 30)
            result = model.transcribe(self.file_path, **self.options)
            self.progress.emit(self.file_path, 100)
            self.finished.emit(self.file_path, result)
        except Exception as e:
            self.error.emit(self.file_path, str(e))
