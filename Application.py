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

        # Create Cells Text
        cells_label = QLabel('Cells:')
        cells_label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.tabs[working_tab].layout.addWidget(cells_label, 1, 0, 1, 1)
        # Create Cells Input
        cells_edit = QSpinBox()
        cells_edit.setRange(0, 10000)
        self.configs[working_tab].add_handler('priorities-Cells', cells_edit)
        self.tabs[working_tab].layout.addWidget(cells_edit, 1, 1, 1, 1)

        # Create Mods Text
        mods_label = QLabel('Mods:')
        mods_label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.tabs[working_tab].layout.addWidget(mods_label, 2, 0, 1, 1)
        # Create Mods Input
        mods_edit = QSpinBox()
        mods_edit.setRange(0, 10000)
        self.configs[working_tab].add_handler('priorities-Mods', mods_edit)
        self.tabs[working_tab].layout.addWidget(mods_edit, 2, 1, 1, 1)

        # Create Shards Text
        shards_label = QLabel('Shards:')
        shards_label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.tabs[working_tab].layout.addWidget(shards_label, 3, 0, 1, 1)
        # Create Shards Input
        shards_edit = QSpinBox()
        shards_edit.setRange(0, 10000)
        self.configs[working_tab].add_handler('priorities-Shards', shards_edit)
        self.tabs[working_tab].layout.addWidget(shards_edit, 3, 1, 1, 1)

        # Create RP Text
        rp_label = QLabel('Research Points:')
        rp_label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.tabs[working_tab].layout.addWidget(rp_label, 4, 0, 1, 1)
        # Create RP Input
        rp_edit = QSpinBox()
        rp_edit.setRange(0, 10000)
        self.configs[working_tab].add_handler('priorities-RP', rp_edit)
        self.tabs[working_tab].layout.addWidget(rp_edit, 4, 1, 1, 1)

        # Create AP Text
        ap_label = QLabel('Academy Points:')
        ap_label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.tabs[working_tab].layout.addWidget(ap_label, 5, 0, 1, 1)
        # Create AP Input
        ap_edit = QSpinBox()
        ap_edit.setRange(0, 10000)
        self.configs[working_tab].add_handler('priorities-AP', ap_edit)
        self.tabs[working_tab].layout.addWidget(ap_edit, 5, 1, 1, 1)

        # Create MM Text
        mm_label = QLabel('Mission Materials:')
        mm_label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.tabs[working_tab].layout.addWidget(mm_label, 6, 0, 1, 1)
        # Create MM Input
        mm_edit = QSpinBox()
        mm_edit.setRange(0, 10000)
        self.configs[working_tab].add_handler('priorities-MM', mm_edit)
        self.tabs[working_tab].layout.addWidget(mm_edit, 6, 1, 1, 1)

        # Create OP Text
        op_label = QLabel('Ouroboros Points:')
        op_label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.tabs[working_tab].layout.addWidget(op_label, 7, 0, 1, 1)
        # Create Level Input
        op_edit = QSpinBox()
        op_edit.setRange(0, 10000)
        self.configs[working_tab].add_handler('priorities-OP', op_edit)
        self.tabs[working_tab].layout.addWidget(op_edit, 7, 1, 1, 1)

        # Create Cost Reduction Text
        cr_label = QLabel('Cost Reduction:')
        cr_label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.tabs[working_tab].layout.addWidget(cr_label, 8, 0, 1, 1)
        # Create Cost Reduction Input
        cr_edit = QSpinBox()
        cr_edit.setRange(0, 10000)
        self.configs[working_tab].add_handler('priorities-Cost Reduction', cr_edit)
        self.tabs[working_tab].layout.addWidget(cr_edit, 8, 1, 1, 1)

        # Create Rank Points Text
        rank_label = QLabel('Rank Points:')
        rank_label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.tabs[working_tab].layout.addWidget(rank_label, 9, 0, 1, 1)
        # Create Level Input
        rank_edit = QSpinBox()
        rank_edit.setRange(0, 1000)
        self.configs[working_tab].add_handler('priorities-Rank Points', rank_edit)
        self.tabs[working_tab].layout.addWidget(rank_edit, 9, 1, 1, 1)

        # Create Active Play Text
        active_label = QLabel('Active Play Time:')
        active_label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.tabs[working_tab].layout.addWidget(active_label, 10, 0, 1, 1)
        # Create Level Input
        active_edit = QSpinBox()
        active_edit.setRange(0, 1440)
        self.configs[working_tab].add_handler('priorities-active play', active_edit)
        self.tabs[working_tab].layout.addWidget(active_edit, 10, 1, 1, 1)

        # Create Save Button
        export_button = QPushButton('Save')
        export_button.clicked.connect(self.save_all_configs)
        self.tabs[working_tab].layout.addWidget(export_button, 11, 0, 1, 1)

    def setup_player_tab(self):
        working_tab = 1
        self.create_layout(working_tab)

        # Create Level Text
        player_label = QLabel('Level:')
        player_label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.tabs[working_tab].layout.addWidget(player_label, 0, 0, 1, 1)
        # Create Level Input
        player_edit = QSpinBox()
        player_edit.setRange(0, 1000)
        self.configs[working_tab].add_handler('Level', player_edit)
        self.tabs[working_tab].layout.addWidget(player_edit, 0, 1, 1, 1)

        # Create LP Bar Text
        lp_bar_label = QLabel('LP Bar:')
        lp_bar_label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.tabs[working_tab].layout.addWidget(lp_bar_label, 1, 0, 1, 1)
        # Create LP Bar Input
        lp_bar_edit = QSpinBox()
        lp_bar_edit.setRange(0, 9)
        self.configs[working_tab].add_handler('LP Bar', lp_bar_edit)
        self.tabs[working_tab].layout.addWidget(lp_bar_edit, 1, 1, 1, 1)

    def setup_tokens_tab(self):
        working_tab = 2
        self.create_layout(working_tab)

        # Create Level Text
        player_label = QLabel('Level:')
        player_label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        # self.tabs[working_tab].layout.addWidget(player_label, 0, 0, 1, 1)
        # Create Level Input
        player_edit = QSpinBox()
        player_edit.setRange(0, 1000)
        # self.configs[working_tab].add_handler('Level', player_edit)
        # self.tabs[working_tab].layout.addWidget(player_edit, 0, 1, 1, 1)

    def create_layout(self, tab_number):
        with open(self.tab_paths[tab_number], 'r') as file:
            self.configs[tab_number].set_defaults(json.load(file))
        self.tabs[tab_number].layout = QGridLayout()
        self.tabs[tab_number].setLayout(self.tabs[tab_number].layout)

    def save_all_configs(self):
        # Example on how to edit a var
        self.configs[1].set('Level', self.configs[1].get('Level') * 2)

        # Real Save function
        for config, path in zip(self.configs, self.tab_paths):
            if config.as_dict():
                # This path would need to be dynamic
                with open(path, 'w') as f:
                    dict_data = config.as_dict()
                    json_data = json.dumps(dict_data, indent=4)
                    f.write(json_data)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
