import csv
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget, QLabel


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Чек')
        self.table = QTableWidget(self)
        self.table.resize(500, 450)
        self.loadTable('price.csv')
        self.table.itemChanged.connect(self.itog)
        self.sumLab = QLabel('Итого:    0', self)
        self.sumLab.move(100, 460)

    def loadTable(self, table_name):
        with open(table_name, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            title = next(reader)
            self.table.setColumnCount(len(title) + 1)
            self.table.setHorizontalHeaderLabels(title + ['Количество'])
            self.table.setRowCount(0)
            for i, row in enumerate(reader):
                self.table.setRowCount(
                    self.table.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.table.setItem(
                        i, j, QTableWidgetItem(elem))
                self.table.setItem(
                    i, 2, QTableWidgetItem('0'))
        self.table.resizeColumnsToContents()

    def itog(self):
        summ = 0
        f = 0
        for i in range(self.table.rowCount()):
            if float(self.table.item(i, 1).text()) < 0 or float(self.table.item(i, 2).text()) < 0:
                f = 1
            summ += float(self.table.item(i, 1).text()) * float(self.table.item(i, 2).text())
        if f:
            self.sumLab.setText('Введено отрицательное количество или цена!')
            self.sumLab.adjustSize()
        else:
            self.sumLab.setText('Итого:    ' + str(summ))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())