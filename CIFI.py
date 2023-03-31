import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QFont
from Application import App
import qdarktheme as theme

import pickle
from player import Player

# How to turn to EXE for distribution
# https://www.pythonguis.com/tutorials/packaging-pyqt6-applications-windows-pyinstaller/

# Using PyQtConfig for import and exporting Player
# https://github.com/pythonguis/pyqtconfig
# Alternative: https://stackoverflow.com/questions/21992849/binding-a-pyqt-pyside-widget-to-a-local-variable-in-python

# Themes
#
#


if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    theme.setup_theme()
    customFont = QFont('Arial', 12)
    app.setFont(customFont)
    ex = App(screen.size())
    sys.exit(app.exec())
