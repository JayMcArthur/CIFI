import json

from PyQt6.QtWidgets import QMainWindow, QSpinBox, QPushButton, QLineEdit, QWidget, QTabWidget, QSizePolicy, QVBoxLayout, QGridLayout, QLabel
from pyqtconfig import ConfigManager
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QIcon, QIntValidator


class App(QMainWindow):
    def __init__(self, size):
        super().__init__()
        self.title = 'CIFI Helper'
        self.width = 786
        self.height = 650
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

    def closeEvent(self, event):
        self.table_widget.save_all_configs()


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

        self.tab_paths = [
            './settings/settings.json',
            './settings/player.json',
            './settings/token.json',
            './settings/diamond.json',
            './settings/gens.json',
            './settings/fleet.json',
            './settings/tech.json',
            './settings/loop.json',
            './settings/shard.json',
            './settings/research.json',
            './settings/academy.json'
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
        self.setup_tokens_tab()

        # Post Tabs
        self.layout.addWidget(self.tab_widget)
        self.setLayout(self.layout)

    def setup_main_tab(self):
        working_tab = 0
        self.create_layout(working_tab)

        # Create Priorities Text
        priorities_label = QLabel('Priorities:')
        priorities_label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.tabs[working_tab].layout.addWidget(priorities_label, 0, 0, 1, 1)

        # Create Cells
        self.create_text_num_input(working_tab, 'Cells:', 1, 0, 10000, 'priorities_Cells')

        # Create Mods
        self.create_text_num_input(working_tab, 'Mods:', 2, 0, 10000, 'priorities_Mods')

        # Create Shards
        self.create_text_num_input(working_tab, 'Shards:', 3, 0, 10000, 'priorities_Shards')

        # Create Research Points
        self.create_text_num_input(working_tab, 'Research Points:', 4, 0, 10000, 'priorities_RP')

        # Create Academy Points
        self.create_text_num_input(working_tab, 'Academy Points:', 5, 0, 10000, 'priorities_AP')

        # Create Mission Materials
        self.create_text_num_input(working_tab, 'Mission Materials:', 6, 0, 10000, 'priorities_MM')

        # Create Ouroboros Points
        self.create_text_num_input(working_tab, 'Ouroboros Points:', 7, 0, 10000, 'priorities_OP')

        # Create Cost Reduction Text
        self.create_text_num_input(working_tab, 'Cost Reduction', 8, 0, 10000, 'priorities_Cost Reduction')

        # Create Rank Points Text
        self.create_text_num_input(working_tab, 'Rank Points', 9, 0, 10000, 'priorities_Rank Points')

        # Create Active Play Text
        self.create_text_num_input(working_tab, 'Active Play Time:', 10, 0, 1440, 'priorities_active play')

        # Create Save Button
        export_button = QPushButton('Save')
        export_button.clicked.connect(self.save_all_configs)
        self.tabs[working_tab].layout.addWidget(export_button, 11, 0, 1, 1)

    def setup_player_tab(self):
        working_tab = 1
        self.create_layout(working_tab)

        # Create Level
        self.create_text_num_input(working_tab, 'Level:', 0, 0, 1000, 'Level')

        # Create LP Bar
        self.create_text_num_input(working_tab, 'LP Bar:', 1, 0, 9, 'LP Bar')

    def setup_tokens_tab(self):
        working_tab = 2
        self.create_layout(working_tab)

        # Create Tokens
        self.create_text_num_input(working_tab, 'Tokens:', 0, 0, 100000, 'Tokens')

    def create_layout(self, tab_number):
        with open(self.tab_paths[tab_number], 'r') as file:
            self.configs[tab_number].set_defaults(json.load(file))
        self.tabs[tab_number].layout = QGridLayout()
        self.tabs[tab_number].setLayout(self.tabs[tab_number].layout)

    def create_text_num_input(self, working_tab, text, row, min_i, max_i, key):
        label = QLabel(text)
        label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.tabs[working_tab].layout.addWidget(label, row, 0, 1, 1)

        spin = QSpinBox()
        spin.setRange(min_i, max_i)
        self.configs[working_tab].add_handler(key, spin)
        self.tabs[working_tab].layout.addWidget(spin, row, 1, 1, 1)

    def save_all_configs(self):
        # Example on how to edit a var
        self.configs[1].set('Level', self.configs[1].get('Level') * 2)

        # Real Save function
        for config, path in zip(self.configs, self.tab_paths):
            if config.as_dict():
                with open(path, 'w') as f:
                    dict_data = config.as_dict()
                    json_data = json.dumps(dict_data, indent=4)
                    f.write(json_data)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
