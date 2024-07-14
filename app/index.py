import sys, os
from PyQt6 import QtWidgets
from MainWindow import MainWindow
from Context import Context

Context().data = {
    Context.SNDTVER : '0.0.0',
    Context.WD      : os.path.dirname(__file__),
    Context.LANG    : 'fr',
}

app = QtWidgets.QApplication([])

if len(sys.argv) > 1 :
    file:str = sys.argv[1]
    window = MainWindow(open_project=file)

else :
    window = MainWindow()

window.show()
app.exec()