import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Bot Interface")
        self.setGeometry(100, 100, 400, 300)

        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(50, 50, 300, 150)

        self.button = QPushButton("Send", self)
        self.button.setGeometry(150, 220, 100, 30)
        self.button.clicked.connect(self.send_request)

    def send_request(self):
        user_input = self.text_edit.toPlainText()
        # Code to interact with the AI bot goes here
        # You can process the user input and display the bot's response


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
