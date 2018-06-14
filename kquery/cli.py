import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSettings
from .kquery import MainWindow

def cli():
    app = QtWidgets.QApplication(sys.argv)
    app.setOrganizationName('kquery')
    app.setOrganizationDomain('github.com/samambaman')

    settings = QSettings(app)

    my_mainWindow = MainWindow(settings)
    my_mainWindow.show()

    sys.exit(app.exec_())
