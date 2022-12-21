import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QStatusBar


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Anti.ui', self)
        self.runner.clicked.connect(self.run)

    def run(self):
        k = 0
        a = self.text1.toPlainText().split('\n')
        b = self.text2.toPlainText().split('\n')
        for i in range(min(len(a), len(b))):
            if a[i] == b[i]:
                k += 1
        print(k / max(len(a), len(b)) * 100, self.spin.value())
        if k / max(len(a), len(b)) * 100 >= self.spin.value():
            self.stat.setStyleSheet('QLabel {background-color: red;}')
        else:
            self.stat.setStyleSheet('QLabel {background-color: green;}')
        self.stat.setText(f'Схожесть {k / max(len(a), len(b)) * 100}%')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())