import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        self.zn = 'X'
        super().__init__()
        uic.loadUi('Toe.ui', self)
        self.but = [[self.B1, self.B2, self.B3], [self.B4, self.B5, self.B6], [self.B7, self.B8, self.B9]]
        self.board = [['', '', ''], ['', '', ''], ['', '', '']]
        for i in self.but:
            for j in i:
                j.setEnabled(False)
                j.clicked.connect(self.do_sq)
        self.new_2.clicked.connect(self.new_game)
        self.One.setChecked(True)

    def do_sq(self):
        for i in range(3):
            for j in range(3):
                if self.sender() == self.but[i][j]:
                    self.board[i][j] = self.zn
                    self.sender().setText(self.zn)
        w = self.win()
        if w:
            self.new_2.setText(w)
            for i in self.but:
                for j in i:
                    j.setEnabled(False)
        if self.zn == 'X':
            self.zn = 'O'
        else:
            self.zn = 'X'

    def new_game(self):
        self.board = [['', '', ''], ['', '', ''], ['', '', '']]
        for i in self.but:
            for j in i:
                j.setText('')
                j.setEnabled(True)
        self.new_2.setText('Новая игра')
        if self.One.isChecked():
            self.zn = 'X'
        else:
            self.zn = 'O'

    def win(self):
        for i in self.board:
            if i.count('X') == 3:
                return 'Выиграл X'
            elif i.count('O') == 3:
                return 'Выиграл O'
        for i in range(3):
            cx = 0
            co = 0
            for j in range(3):
                if self.board[j][i] == 'X':
                    cx += 1
                elif self.board[j][i] == 'O':
                    co += 1
            if cx == 3:
                return 'Выиграл X'
            elif co == 3:
                return 'Выиграл O'
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            if self.board[0][0] == 'X':
                return 'Выиграл X'
            elif self.board[0][0] == 'O':
                return 'Выиграл O'
        elif self.board[0][2] == self.board[1][1] == self.board[2][0]:
            if self.board[1][1] == 'X':
                return 'Выиграл X'
            elif self.board[1][1] == 'O':
                return 'Выиграл O'
        for i in self.board:
            for j in i:
                if j == '':
                    return
        return 'Ничья'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())