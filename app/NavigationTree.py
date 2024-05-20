from PyQt6.QtWidgets import QTreeWidget, QTreeWidgetItem
from PyQt6.QtCore import Qt
from model.Project import Project
from model.Rack import Rack
from model.Device import Device

class NavigationTree (QTreeWidget) :

    def __init__(self, project:Project, *args, **kwargs) :
        super(NavigationTree, self).__init__(*args, **kwargs)
        self.setupUi()

        self.project:Project = project

    def setupUi(self) :
        self.setObjectName("navigation_tree")
        self.headerItem().setText(0, "1")
        self.header().setVisible(False)
        self.header().setCascadingSectionResizes(False)

    def update_ui(self) :

        # No file open so no navigation tree neded
        if self.project is None :
            return None
        
        # Building the tree data
        project_title:str = self.project.metadata['title']
        rack_list:list[Rack] = self.project.racks
        device_list:list[Device] = self.project.devices

        # Building UI items from tree data
        project_top_level_item  = QTreeWidgetItem([project_title])
        rack_top_level_item     = QTreeWidgetItem(project_top_level_item, ['Rack'])
        device_top_level_item   = QTreeWidgetItem(project_top_level_item, ['Device'])

        self.insertTopLevelItem(0, project_top_level_item)

        for rack in rack_list :
            item = QTreeWidgetItem([rack.label_1])
            item.setData(1, Qt.ItemDataRole.UserRole, rack)
            rack_top_level_item.addChild(item)

        for device in device_list :
            item = QTreeWidgetItem([device.label_1])
            item.setData(1, Qt.ItemDataRole.UserRole, device)
            device_top_level_item.addChild(item)