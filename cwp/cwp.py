__author__ = 'mFoxRU'

import sys

from PyQt4.QtGui import QApplication

from gui import GuiApp


def main():
    app = QApplication(sys.argv)
    gui = GuiApp()
    gui.show()
    app.exec_()

if __name__ == "__main__":
    main()
