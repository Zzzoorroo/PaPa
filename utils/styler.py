
from PyQt5.QtCore import QFile, QTextStream

def apply_dark_theme(app):
    file = QFile(':/dark/style.qss')
    if file.open(QFile.ReadOnly | QFile.Text):
        stream = QTextStream(file)
        app.setStyleSheet(stream.readAll())
