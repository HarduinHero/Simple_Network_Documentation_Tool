import sys, os
from PySide6 import QtWidgets
from MainWindow import MainWindow
from Config import Config

import ui.ressources_rc

Config().data = {
    Config.SNDTVER : '0.0.0',
    Config.WD      : os.path.dirname(__file__),
    Config.LANG    : 'fr',
}

app = QtWidgets.QApplication([])

if len(sys.argv) > 1 :
    file:str = sys.argv[1]
    window = MainWindow(project_path=file)

else :
    window = MainWindow()

window.show()
app.exec()