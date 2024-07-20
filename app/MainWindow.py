from typing import Optional, Union
from pathlib import Path

from model.Project import Project
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QFileDialog, QMainWindow, QTreeWidgetItem, QMessageBox
from ui.mainwindow import Ui_main_window
from NavigationTree import NavigationTree
from EditProjectDialog import EditProjectWindow

ERROR_TIMEOUT = 2500

class MainWindow(QMainWindow, Ui_main_window) :

    def __init__(self, *args, obj=None, project_path:Optional[str]=None, **kwargs) :
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Initializing the current project
        self.current_project = None

        # Open with command arg
        if project_path is not None :
            self.current_project = Project.load_from_file(Path(project_path))

        # Ataching menubar action
        self.init_menu_load_example_project()

        self.action_new_project.triggered.connect(self.action_new_project_handler)
        self.action_open_project.triggered.connect(self.action_open_project_handler)

        self.action_user_guide.triggered.connect(self.action_not_handled_yet('action_user_guide'))
        self.action_about.triggered.connect(self.action_not_handled_yet('action_about'))

        # Setup nav tree
        # self.navigation_tree = NavigationTree(self.current_project, parent=self.nav_tree_frame)
        # self.nav_tree_frame_layout.addWidget(self.navigation_tree)
        # self.navigation_tree.show()
        # self.navigation_tree.itemClicked.connect(self.select_element_in_nav_tree_handler)
        # self.navigation_tree.update_ui()

        # Setup central zone 
        self.current_editing_frame = None

        






##########################################
#                   UI                   #
##########################################

    def init_menu_load_example_project(self) :
        self.action_list_load_project = []
        EXAMPLES = ['a', 'b']
        for ex in EXAMPLES :
            current_action = QAction(parent=self)
            current_action.setObjectName(f'action_{ex}')
            current_action.setText(ex)
            current_action.triggered.connect(self.action_load_example_project)
            
            self.menu_load_example_project.addAction(current_action)
            self.action_list_load_project.append(current_action)

    # def set_editing_frame(self, new_frame:Union[RackEdit, DeviceEdit, None]) :
    #     if self.current_editing_frame is not None :
    #         self.current_editing_frame.setParent(None)
    #     if new_frame is not None :
    #         self.current_editing_frame = new_frame
    #         self.current_editing_frame.setParent(self.editing_frame)
    #         self.current_editing_frame.show()







##########################################
#                HANDLERS                #
##########################################


    def action_not_handled_yet(self, msg) :
        return lambda: print(f'ACTION NOT HANDLED YET : {msg}')
    
    def action_new_project_handler(self) :
        if self.current_project is not None and not(self.current_project._is_saved) :
            ok_new_project = QMessageBox.warning(self, 
                                'Curent project is not saved',
                                'Your current project has not been saved.\nIf you continue changes will be lost.',
                                QMessageBox.StandardButton.Cancel | QMessageBox.StandardButton.Ignore
                            ) == QMessageBox.StandardButton.Ignore
        else :
            ok_new_project = True
            
        if ok_new_project :
            dlg = EditProjectWindow(self, project=self.current_project)
            if dlg.exec() :
                self.current_project = dlg.project
        # self.navigation_tree.set_project(self.current_project)

    def action_open_project_handler(self) :
        filename = QFileDialog.getOpenFileName(self, 'Open project', str(Path.home()), 'SNDT project (*.sndp *.zip)')[0]
        # nothing if selection canceled
        if filename == '' :
            return None
        self.current_project = Project.load_from_file(Path(filename))
        # self.navigation_tree.set_project(self.current_project)

    def action_load_example_project(self) :
        #TODO self.current_project.load_example_project(action.text())
        #self.navigation_tree.update_ui()
        pass

    def select_element_in_nav_tree_handler(self, e:QTreeWidgetItem) :
        item_value = e.data(1, Qt.ItemDataRole.UserRole)
        print('NotImplemented', item_value)

        # if isinstance(item_value, Rack) :
        #     self.set_editing_frame(RackEdit(item_value))
            
        # if isinstance(item_value, Device) :
        #     self.set_editing_frame(DeviceEdit(item_value))
