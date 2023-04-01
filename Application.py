import pickle

from PyQt6.QtWidgets import QMainWindow, QSpinBox, QPushButton, QLineEdit, QWidget, QTabWidget, QSizePolicy, QVBoxLayout, QGridLayout, QLabel
from pyqtconfig import ConfigManager
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QIcon, QIntValidator
from settings.player import PlayerSettings


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
        self.configs = [
            ConfigManager(),
            ConfigManager(),
            ConfigManager(),
            ConfigManager(),
            ConfigManager(),
            ConfigManager(),
            ConfigManager(),
            ConfigManager(),
            ConfigManager(),
            ConfigManager(),
            ConfigManager()
        ]

        # Create Tabs
        for tab, name in zip(self.tabs, self.tab_names):
            self.tab_widget.addTab(tab, name)

        # Call each Tab setup
        self.setup_main_tab()
        self.setup_player_tab()

        # Post Tabs
        self.layout.addWidget(self.tab_widget)
        self.setLayout(self.layout)

    def setup_main_tab(self):
        working_tab = 0
        self.tabs[working_tab].layout = QGridLayout()
        self.tabs[working_tab].setLayout(self.tabs[working_tab].layout)

        # Create Save BUtton
        export_button = QPushButton('Save')
        export_button.clicked.connect(self.save_all_configs)
        self.tabs[working_tab].layout.addWidget(export_button, 0, 0, 1, 1)

    def setup_player_tab(self):
        working_tab = 1
        self.configs[working_tab].set_defaults(PlayerSettings)
        self.tabs[working_tab].layout = QGridLayout()
        self.tabs[working_tab].setLayout(self.tabs[working_tab].layout)

        # Create Level Text
        player_label = QLabel('Level:')
        player_label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.tabs[working_tab].layout.addWidget(player_label, 0, 0, 1, 1)
        # Create Level Input
        player_edit = QSpinBox()
        player_edit.setRange(0, 1000)
        self.configs[working_tab].add_handler('Level', player_edit)
        self.tabs[working_tab].layout.addWidget(player_edit, 0, 1, 1, 3)

        # Unfinished LP Bar Text
        lp_bar_label = QLabel('LP Bar:')
        lp_bar_label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

    def save_all_configs(self):
        # Example on how to edit a var
        self.configs[1].set('Level', self.configs[1].get('Level') * 2)

        # Real Save function
        for config in self.configs:
            if config.as_dict():
                # This path would need to be dynamic
                with open('./person_data.py', 'w') as f:
                    f.write(str(config.as_dict()))

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
