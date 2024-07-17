from typing import Optional, Union
from pathlib import Path

from model.Project import Project
from PyQt6.QtWidgets import QDialog, QFileDialog
from ui.edit_project_dialog import Ui_edit_project_dialog

class EditProjectWindow(QDialog, Ui_edit_project_dialog) :

    def __init__(self, *args, obj=None, project:Project, **kwargs) -> None :
        super(EditProjectWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        self.project = project

        self.BT_F_filename_browse.clicked.connect(self.bt_f_filename_browse_handler)
        self


    
    def bt_f_filename_browse_handler(self) -> None:
        if self.project.filename is None :
            filename:str = QFileDialog.getSaveFileName(self, 'New project path', str(Path.home()), 'SNDT project (*.sndp *.zip)')[0]
        else :
            filename:str = QFileDialog.getSaveFileName(self, 'Project path', self.project.filename, 'SNDT project (*.sndp *.zip)')[0]
        self.F_filename.setText(filename)