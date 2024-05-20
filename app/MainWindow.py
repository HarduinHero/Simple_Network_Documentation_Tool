from typing import Optional, Union

from DeviceEdit import DeviceEdit
from model.Device import Device
from model.LocalFile import EXAMPLES
from model.Project import Project
from model.Rack import Rack
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QFileDialog, QMainWindow, QTreeWidgetItem
from RackEdit import RackEdit
from ui.mainwindow import Ui_main_window
from NavigationTree import NavigationTree

ERROR_TIMEOUT = 2500

class MainWindow(QMainWindow, Ui_main_window) :

    def __init__(self, *args, obj=None, open_project=None, **kwargs) :
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Open with command arg
        self.current_project : Optional[Project]
        if open_project is not None :
            self.current_project = Project(open_project)
        else :
            self.current_project = None

        # Ataching menubar action
        self.init_menu_load_example_project()

        self.action_new_project.triggered.connect(self.action_new_project_handler)
        self.action_open_project.triggered.connect(self.action_open_project_handler)

        self.action_user_guide.triggered.connect(self.action_not_handled_yet('action_user_guide'))
        self.action_about.triggered.connect(self.action_not_handled_yet('action_about'))

        # Setup Navigation Tree
        self.navigation_tree = NavigationTree(self.current_project, parent=self.nav_tree_frame)
        self.nav_tree_frame_layout.addWidget(self.navigation_tree)
        self.navigation_tree.show()
        self.navigation_tree.itemClicked.connect(self.select_element_in_nav_tree_handler)
        self.navigation_tree.update_ui()

        #
        self.current_editing_frame = None

        






##########################################
#                   UI                   #
##########################################

    def init_menu_load_example_project(self) :
        self.action_list_load_project = []
        for ex in EXAMPLES :
            current_action = QAction(parent=self)
            current_action.setObjectName(f'action_{ex}')
            current_action.setText(ex)
            current_action.triggered.connect(self.action_load_example_project)
            
            self.menu_load_example_project.addAction(current_action)
            self.action_list_load_project.append(current_action)

    def set_editing_frame(self, new_frame:Union[RackEdit, DeviceEdit, None]) :
        if new_frame is None :
            pass
        else :
            if self.current_editing_frame is not None :
                self.current_editing_frame.setParent(None)
            self.current_editing_frame = new_frame
            self.current_editing_frame.setParent(self.editing_frame)
            self.current_editing_frame.show()







##########################################
#                HANDLERS                #
##########################################


    def action_not_handled_yet(self, msg) :
        return lambda: print(f'ACTION NOT HANDLED YET : {msg}')
    
    def action_new_project_handler(self) :
        filename = QFileDialog.getSaveFileName(self, 'New project')[0]
        self.current_project = Project.new_project(filename)
        self.navigation_tree.update_ui()

    def action_open_project_handler(self) :
        filename = QFileDialog.getOpenFileName(self, 'Open project')[0]
        self.current_project = Project(filename)
        self.navigation_tree.update_ui()  

    def action_load_example_project(self) :
        if self.current_project == None :
            self.statusBar().showMessage('Error : you have to create a new project first !', ERROR_TIMEOUT)
        else :
            action = self.sender()
            #TODO self.current_project.load_example_project(action.text())
            self.navigation_tree.update_ui()

    def select_element_in_nav_tree_handler(self, e:QTreeWidgetItem) :
        item_value = e.data(1, Qt.ItemDataRole.UserRole)

        if isinstance(item_value, Rack) :
            print(item_value, 'Rack')
            self.set_editing_frame(RackEdit(item_value))
            
        if isinstance(item_value, Device) :
            print(item_value, 'Device')
            self.set_editing_frame(DeviceEdit(item_value))
