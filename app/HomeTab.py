from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QTreeWidgetItem
from ui.home_tab import Ui_home_tab
from model.Project import Project, Views


class Home_tab(QWidget, Ui_home_tab):

    def __init__(self, project:Project|None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.project = project

        if self.project is not None :
            self.project_item = QTreeWidgetItem([self.project.title, self.project.description, '', ''])

            self.views_item = []
            for view in Views :
                current_view = QTreeWidgetItem(self.project_item, [view.value, '', '', ''])



            self.project_tree.addTopLevelItem(self.project_item)