from typing import Optional, Union
from pathlib import Path

from model.Project import Project
from PyQt6.QtWidgets import QDialog, QFileDialog, QMessageBox
from ui.edit_project_dialog import Ui_edit_project_dialog

class EditProjectWindow(QDialog, Ui_edit_project_dialog) :

    def __init__(self, *args, obj=None, project:Project, **kwargs) -> None :
        super(EditProjectWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        self.project = project

        self.BT_F_filename_browse.clicked.connect(self.bt_f_filename_browse_handler)
        self.BT_cancel.clicked.connect(self.bt_cancel_handler)
        self.BT_execute.clicked.connect(self.bt_execute_handler)

        if self.project._is_initialized :
            self.setWindowTitle('Edit project')
            self.F_filename.setText(self.project.file_path.as_posix()) # type: ignore
            self.F_name.setText(self.project.title)
            self.F_description.setText(self.project.description)
        else :
            self.setWindowTitle('New project')

    def bt_execute_handler(self) -> None:
        # Checks for EMPTY fields
        if self.F_filename.text() == '' :
            QMessageBox.warning(self, 'Empty field', 'Project cannot have empty filename')
            return None
        if self.F_name.text() == '' :
            QMessageBox.warning(self, 'Empty field', 'Project cannot have empty title')
            return None
        if Path(self.F_filename.text()).is_dir() :
            QMessageBox.warning(self, 'Filename is wrong', 'You must specify a file')
            return None
        
        # Si tout ok edit project
        if self.project._is_initialized :
            self.project.file_path   = Path(self.F_filename.text())
            self.project.title       = self.F_name.text()
            self.project.description = self.F_description.toPlainText()
        else :
            self.project.init_new(
                Path(self.F_filename.text()),
                self.F_name.text(),
                self.F_description.toPlainText()
            )

        self.accept()
    
    def bt_cancel_handler(self) -> None:
        self.reject()

    def bt_f_filename_browse_handler(self) -> None:
        if self.project.file_path is None :
            filename:str = QFileDialog.getSaveFileName(self, 'New project path', str(Path.home()), 'SNDT project (*.sndp *.zip)')[0]
        else :
            filename:str = QFileDialog.getSaveFileName(self, 'Project path', self.project.file_path.as_posix(), 'SNDT project (*.sndp *.zip)')[0]
        
        # nothing if selection canceled
        if filename == '' :
            return None

        # Fix extension if needed
        if Path(filename).suffix not in ['.sndp', '.zip'] :
            filename += '.sndp'
        
        self.F_filename.setText(filename)
        self.F_name.setText(Path(filename).stem)