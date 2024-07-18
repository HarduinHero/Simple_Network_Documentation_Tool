import sys, os
from PyQt6 import QtWidgets
from MainWindow import MainWindow
from Config import Config

Config().data = {
    Config.SNDTVER : '0.0.0',
    Config.WD      : os.path.dirname(__file__),
    Config.LANG    : 'fr',
}

app = QtWidgets.QApplication([])

if len(sys.argv) > 1 :
    file:str = sys.argv[1]
    window = MainWindow(open_project=file)

else :
    window = MainWindow()

window.show()
app.exec()