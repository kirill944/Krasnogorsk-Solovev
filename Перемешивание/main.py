import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextBrowser, QPushButton


class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Перемешивание')
        self.setGeometry(100, 100, 300, 300)

        self.button = QPushButton("Загрузить", self)
        self.button.move(10, 10)
        self.button.resize(100, 30)
        self.button.clicked.connect(self.download)

        self.text = QTextBrowser(self)
        self.text.resize(250, 250)
        self.text.move(10, 45)

    def download(self):
        with open('text.txt') as file:
            text_pl = file.read().split('\n')
            fir = []
            sec = []
            for i in range(len(text_pl)):
                if i % 2 == 0:
                    sec.append(text_pl[i])
                else:
                    fir.append(text_pl[i])
            text_pl = fir + sec
            self.text.setText('\n'.join(text_pl))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())