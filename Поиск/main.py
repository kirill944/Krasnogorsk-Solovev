import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Sqrs(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('finder.ui', self)
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle('Поиск по фильмам')
        self.connection = sqlite3.connect("films_db.sqlite")
        self.but.clicked.connect(self.finder)
        self.lines = [self.line1, self.line2, self.line3, self.line4, self.line5]

    def finder(self):
        if self.line.text() == '':
            self.status.setText('Пустой запрос')
            for i in range(5):
                self.lines[i].setText('')
        else:
            cur = self.connection.cursor()
            result = ''
            if self.combo.currentText() == 'Название':
                result = cur.execute("""SELECT * FROM films
                        WHERE title = ?""", (self.line.text(), )).fetchall()
            if self.combo.currentText() == 'Год выпуска':
                result = cur.execute("""SELECT * FROM films
                        WHERE year = ?""", (self.line.text(), )).fetchall()
            if self.combo.currentText() == 'Продолжительность':
                result = cur.execute("""SELECT * FROM films
                        WHERE duration = ?""", (self.line.text(), )).fetchall()
            if result:
                self.status.setText('')
                for i in range(5):
                    self.lines[i].setText(str(result[0][i]))
            else:
                self.status.setText('Ничего не найдено')
                for i in range(5):
                    self.lines[i].setText('')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Sqrs()
    ex.show()
    sys.exit(app.exec())