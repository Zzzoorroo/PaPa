from views.main_view import MainView
from PyQt5.QtWidgets import QMessageBox

class MainController:
    def __init__(self, view: MainView):
        self.view = view
        self.view.button.clicked.connect(self.handle_button_click)

    def handle_button_click(self):
        QMessageBox.information(self.view, "Info", "Button clicked!")
