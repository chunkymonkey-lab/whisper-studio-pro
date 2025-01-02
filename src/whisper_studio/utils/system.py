import psutil
from PyQt6.QtCore import QThread, pyqtSignal

class SystemMonitor(QThread):
    resources_updated = pyqtSignal(dict)
    
    def __init__(self):
        super().__init__()
        self.monitoring = True