from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QButtonGroup
from Button import Button
from logick import Logic


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.buttons = []
        self.init_ui()
        self.logic = Logic(self.buttons)

    def create_button_click_handler(self, button_id):
        return lambda: self.click(button_id)

    def init_ui(self):
        self.setGeometry(300, 300, 600, 480)
        self.setWindowTitle('Tic Tac Toe')
        x, y = 70, 90

        for i in range(0, 9):
            btn = Button('', i, self)
            btn.clicked.connect(
                self.create_button_click_handler(i)
            )
            btn.resize(90, 90)
            if i in (3, 6):
                x = 160
                y += 90
            else:
                x += 90
            btn.move(x, y)
            self.buttons.append(btn)

        self.show()

    def click(self, index_btn):
        btn = self.buttons[index_btn]
        btn.setEnabled(False)
        btn.setStyleSheet("background-image : url(src/o.png);")
        self.buttons[index_btn].id = 0
        self.logic.check_game_state()

        # send data to server
