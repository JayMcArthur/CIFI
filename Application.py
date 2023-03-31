from PyQt6.QtWidgets import QMainWindow, QPushButton, QWidget, QTabWidget,QVBoxLayout, QGridLayout, QLabel
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import pyqtSlot


class App(QMainWindow):
    def __init__(self, size):
        super().__init__()
        self.title = 'CIFI Helper'
        self.width = 786
        self.height = 500
        self.setMinimumSize(self.width, self.height)
        self.left = int((size.width() / 2) - (self.width / 2))
        self.top = int((size.height() / 2) - (self.height / 2))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.icon = './Icon.webp'
        self.setWindowIcon(QIcon(self.icon))

        self.table_widget = CustomTable(self)
        self.setCentralWidget(self.table_widget)

        self.show()


class CustomTable(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.tab_names = [
            'Main',
            'Player',
            'Tokens',
            'Diamonds',
            'Gens',
            'Fleet',
            'Tech Upgrades',
            'Loop Mods',
            'Shards',
            'Research',
            'Academy'
        ]

        self.tab_widget = QTabWidget()
        self.tabs = [
            QWidget(),
            QWidget(),
            QWidget(),
            QWidget(),
            QWidget(),
            QWidget(),
            QWidget(),
            QWidget(),
            QWidget(),
            QWidget(),
            QWidget()
        ]

        self.tab_widget.resize(300, 200)

        for tab, name in zip(self.tabs, self.tab_names):
            self.tab_widget.addTab(tab, name)

        self.setup_main_tab()

        self.layout.addWidget(self.tab_widget)
        self.setLayout(self.layout)

    def setup_main_tab(self):
        working_tab = 0
        self.tabs[working_tab].layout = QGridLayout()
        pushButton1 = QPushButton("PyQt5 button")
        self.tabs[working_tab].layout.addWidget(pushButton1, 0, 0)
        self.tabs[working_tab].setLayout(self.tabs[working_tab].layout)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
