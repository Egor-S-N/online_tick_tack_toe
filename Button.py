from PyQt5.QtWidgets import QPushButton


class Button(QPushButton):
    def __init__(self, text, button_id, parent=None):
        super().__init__(text, parent)
        self.id = button_id
