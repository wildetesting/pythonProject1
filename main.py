import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(400, 300)
        self.result_display = QLineEdit(self)
        self.result_display.setGeometry(10, 10, 380, 50)
        self.result_display.setAlignment(Qt.AlignRight)
        self.result_display.setReadOnly(True)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', '*', '0', '.', '=', '/'
        ]
        pos_x = 10
        pos_y = 70
        for button in buttons:
            if button == '=':
                self.create_button(button, pos_x, pos_y, 160, 40, self.evaluate)
                break
            elif button == '0':
                self.create_button(button, pos_x, pos_y, 160, 40, self.update_display)
                pos_x += 170
            else:
                self.create_button(button, pos_x, pos_y, 80, 40, self.update_display)
                pos_x += 90
            if pos_x > 260:
                pos_x = 10
                pos_y += 50

    def create_button(self, text, pos_x, pos_y, width, height, function):
        button = QPushButton(text, self)
        button.setGeometry(pos_x, pos_y, width, height)
        button.clicked.connect(function)

    def update_display(self):
        sender = self.sender()
        self.result_display.setText(self.result_display.text() + sender.text())

    def evaluate(self):
        result = eval(self.result_display.text())
        self.result_display.setText(str(result))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
