import sqlite3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect("coffee.db")
        self.update_result()

    def update_result(self):
        cur = self.con.cursor()
        result = cur.execute("SELECT * FROM coffee").fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        #self.titles = [description[0] for description in cur.description]
        self.titles = ["Номер", "Имя", "Степень обжарки", "Молотый", "В зернах", "Описание вкуса", "Цена", "Объём"]
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


app = QApplication(sys.argv)
ex = MainWindow()
ex.show()
sys.exit(app.exec_())