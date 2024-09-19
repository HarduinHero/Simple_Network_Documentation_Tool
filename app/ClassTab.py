from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QTreeWidgetItem, QComboBox
from ui.class_tab import Ui_class_tab
from model.Project import Project
from model.enums import Item_field_type


class Class_tab(QWidget, Ui_class_tab):

    project: Project
    class_id: int
    _is_saved: bool
    field_counter: int
    
    
    def __init__(self, project:Project, class_id:int|None,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.project = project
        self._set_is_saved(True)

        if class_id != None :

            self.class_id = class_id
            self.F_class_id.setValue(self.class_id)
            #TODO
        
        else :
            self.field_counter = 0
            self.ref_counter   = 0

        self.BT_apply.clicked.connect(self.apply_handler)
        self.BT_cancel.clicked.connect(self.cancel_handler)

        self.BT_add_field.clicked.connect(self.add_field_handler)
        self.BT_sub_field.clicked.connect(self.sub_field_handler)

        self.BT_add_ref.clicked.connect(self.add_ref_handler)
        self.BT_sub_ref.clicked.connect(self.sub_ref_handler)



    def _set_is_saved(self, is_saved:bool) :
        self._is_saved = is_saved
        self.BT_apply.setEnabled(not(self._is_saved))
        self.BT_cancel.setEnabled(not(self._is_saved))

    def apply_handler(self) :
        pass

    def cancel_handler(self) :
        pass



    def tree_widget_item_cb_changed_handler(self) :
        self._set_is_saved(False)




    def add_field_handler(self) :
        new_field_item = QTreeWidgetItem([f'New field {self.field_counter}', '', '', '', ''])
        new_field_item.setFlags(new_field_item.flags()|Qt.ItemFlag.ItemIsEditable)
        self.fields_list.addTopLevelItem(new_field_item)
        self.fields_list.setCurrentItem(new_field_item)

        CB_field_type = QComboBox()
        CB_field_type.addItems([t.value for t in Item_field_type])
        self.fields_list.setItemWidget(new_field_item, 1, CB_field_type)

        CB_mandatory = QComboBox()
        CB_mandatory.addItems(['False', 'True'])
        self.fields_list.setItemWidget(new_field_item, 2, CB_mandatory)

        self.field_counter += 1
        self._set_is_saved(False)

    def sub_field_handler(self) :        
        item_index_to_remove = self.fields_list.indexOfTopLevelItem(self.fields_list.currentItem())
        self.fields_list.takeTopLevelItem(item_index_to_remove)





    def add_ref_handler(self) :
        new_ref_item = QTreeWidgetItem([f'New ref {self.ref_counter}', '', '', '', ''])
        new_ref_item.setFlags(new_ref_item.flags()|Qt.ItemFlag.ItemIsEditable)
        self.ref_list.addTopLevelItem(new_ref_item)
        self.ref_list.setCurrentItem(new_ref_item)

        CB_mandatory = QComboBox()
        CB_mandatory.addItems(['False', 'True'])
        self.ref_list.setItemWidget(new_ref_item, 1, CB_mandatory)
        new_ref_item.setData(1, 0, False)

        CB_mandatory = QComboBox()
        CB_mandatory.addItems(['False', 'True'])
        self.ref_list.setItemWidget(new_ref_item, 2, CB_mandatory)
        new_ref_item.setData(2, 0, False)

        CB_field_type = QComboBox()
        CB_field_type.setPlaceholderText('-----')
        CB_field_type.addItems([t.value for t in Item_field_type])
        self.ref_list.setItemWidget(new_ref_item, 3, CB_field_type)
        new_ref_item.setData(3, 0, False)

        self.ref_counter += 1
        self._set_is_saved(False)

        
        print([new_ref_item.data(i, 0) for i in range(self.ref_list.columnCount())])


    def sub_ref_handler(self) :
        item_index_to_remove = self.ref_list.indexOfTopLevelItem(self.ref_list.currentItem())
        self.ref_list.takeTopLevelItem(item_index_to_remove)


