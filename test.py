from PyQt5.QtWidgets import QApplication, QWidget
import sys

print("Script started...")

app = QApplication(sys.argv)
print("QApplication initialized")

window = QWidget()
window.setWindowTitle("Test Window")
window.resize(300, 200)
window.show()
print("Window displayed")

sys.exit(app.exec_())
