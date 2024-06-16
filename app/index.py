import sys
from PyQt6 import QtWidgets
from MainWindow import MainWindow

app = QtWidgets.QApplication([])

if len(sys.argv) > 1 :
    file = sys.argv[1]
    window = MainWindow(open_project=file)

else :
    window = MainWindow()

window.show()
app.exec()