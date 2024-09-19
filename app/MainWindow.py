from typing import Optional, Union
from pathlib import Path

from HomeTab import Home_tab
from model.Project import Project
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (QFileDialog,QMainWindow,QMessageBox,)
from ui.mainwindow import Ui_main_window
from EditProjectDialog import EditProjectWindow
from ClassTab import Class_tab

ERROR_TIMEOUT = 2500

class MainWindow(QMainWindow, Ui_main_window):

    def __init__(self, *args, project_path: Optional[str] = None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Initializing the current project
        self.current_project = None

        # Open with command arg
        if project_path is not None:
            self.current_project = Project.load_from_file(Path(project_path))
            self.current_project.attach(self)

        # Ataching menubar action
        self.init_menu_load_example_project()

        self.action_new_project.triggered.connect(self.action_new_project_handler)
        self.action_open_project.triggered.connect(self.action_open_project_handler)

        self.action_home.triggered.connect(self.action_home_handler)
        self.action_new_class.triggered.connect(self.action_new_class_handler)


        # Make tabs closable
        self.tabWidget.tabCloseRequested.connect(lambda index: self.tabWidget.removeTab(index))

    ##########################################
    #                   UI                   #
    ##########################################

    def init_menu_load_example_project(self):
        self.action_list_load_project = []
        EXAMPLES = ["a", "b"]
        for ex in EXAMPLES:
            current_action = QAction(parent=self)
            current_action.setObjectName(f"action_{ex}")
            current_action.setText(ex)
            #current_action.triggered.connect(self.action_load_example_project)

            self.menu_load_example_project.addAction(current_action)
            self.action_list_load_project.append(current_action)

    ##########################################
    #                HANDLERS                #
    ##########################################

    def project_update_handler(self) :
        pass

    def action_new_project_handler(self):
        if self.current_project is not None and not (self.current_project._is_saved):
            ok_new_project = (
                QMessageBox.warning(
                    self,
                    "Curent project is not saved",
                    "Your current project has not been saved.\nIf you continue changes will be lost.",
                    QMessageBox.StandardButton.Cancel
                    | QMessageBox.StandardButton.Ignore,
                )
                == QMessageBox.StandardButton.Ignore
            )
        else:
            ok_new_project = True

        if ok_new_project:
            dlg = EditProjectWindow(self, project=self.current_project)
            if dlg.exec():
                self.current_project = dlg.project
                self.current_project.attach(self) # type: ignore
        

    def action_open_project_handler(self):
        filename = QFileDialog.getOpenFileName(self, "Open project", str(Path.home()), "SNDT project (*.sndp *.zip)")[0]
        # nothing if selection canceled
        if filename == "":
            return None
        self.current_project = Project.load_from_file(Path(filename))
        self.current_project.attach(self)
        # self.navigation_tree.set_project(self.current_project)

    def action_home_handler(self):
        new_home_tab = Home_tab(self.current_project)
        new_tab_index = self.tabWidget.addTab(new_home_tab, 'Home')
        icon = QIcon(":/icons/home.png")
        self.tabWidget.setTabIcon(new_tab_index, icon)
        self.tabWidget.setCurrentIndex(new_tab_index)

    def action_new_class_handler(self) :
        if self.current_project is None :
            QMessageBox.warning(
                self,
                "No open project",
                "To create a new class you first\nneed to open or create a project.",
                QMessageBox.StandardButton.Close
            )
        else :
            new_class_tab = Class_tab(self.current_project, None)
            new_tab_index = self.tabWidget.addTab(new_class_tab, 'New class')
            icon = QIcon(":/icons/blue-document-block.png")
            self.tabWidget.setTabIcon(new_tab_index, icon)
            self.tabWidget.setCurrentIndex(new_tab_index)
        
