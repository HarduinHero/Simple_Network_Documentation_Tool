from PyQt6.QtWidgets import QTreeWidget, QTreeWidgetItem, QMenu, QSizePolicy, QHeaderView
from PyQt6.QtCore import Qt, QPoint
from model.Project import Project
from typing import Optional, Union


class NavigationTree (QTreeWidget) :

    def __init__(self, project:Optional[Project], *args, **kwargs) :
        super(NavigationTree, self).__init__(*args, **kwargs)
        self.setupUi()
        self.project = project

    def setupUi(self) :
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        self.setSizePolicy(sizePolicy)

        # print(self.sizeHint())
        self.setObjectName("navigation_tree")
        self.setAlternatingRowColors(True)

        self.setColumnCount(2)
        self.setHeaderLabels(['Object', 'Type'])
        self.header().setVisible(True)                                      # type: ignore
        # self.header().setStretchLastSection(False)                             # type: ignore
        # self.header().setSectionResizeMode(0, QHeaderView.ResizeMode.Interactive)# type: ignore
        # self.header().setSectionResizeMode(1, QHeaderView.ResizeMode.Interactive)# type: ignore
        
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.custom_context_menu)

    def set_project(self, project:Optional[Project]) :
        self.project = project
        self.update_ui()

    def update_ui(self) :

        # The project has not been initialized so no navigation tree neded
        if self.project is None :
            return None
        
        # Building the tree from data
        project_title:str = self.project.title # type: ignore
        # rack_list:list[Rack] = self.project.racks

        # Building UI items from tree data
        project_top_level_item  = QTreeWidgetItem([project_title])
        # rack_top_level_item   = QTreeWidgetItem(project_top_level_item, ['Rack'])

        self.insertTopLevelItem(0, project_top_level_item)
        # for rack in rack_list :
        #     item = QTreeWidgetItem([rack.label_1])
        #     item.setData(1, Qt.ItemDataRole.UserRole, rack)
        #     rack_top_level_item.addChild(item)


#######################################################################
####                          CONTEXT MENU                         ####
#######################################################################

    def custom_context_menu(self, point:QPoint) :
        # Infos about the node selected.
        index = self.indexAt(point)
        if not index.isValid():
            return

        item:QTreeWidgetItem = self.itemAt(point) # type: ignore
        

        # We build the menu.
        menu = QMenu()
        action = menu.addAction("Souris au-dessus de")
        action = menu.addAction('test')
        menu.addSeparator()
        action_1 = menu.addAction("Choix 1")
        action_2 = menu.addAction("Choix 2")
        action_3 = menu.addAction("Choix 3")
        menu.exec(self.mapToGlobal(point))