from PyQt6.QtWidgets import QFrame
from ui.rackedit import Ui_rack_edit
from model.Rack import Rack

from typing import Optional

class RackEdit(QFrame, Ui_rack_edit) :
    def __init__(self, rack:Optional[Rack]=None, *args, **kwargs) :
        super(RackEdit, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.rack:Optional[Rack] = rack
        self.changes_not_applyed:bool = False


        if self.rack is not None :
            self.i_rack_id.setValue(self.rack.id_rack)
            self.i_label_1.setText(self.rack.label_1)
            self.i_label_2.setText(self.rack.label_2)
            self.i_height.setValue(self.rack.height)
            self.i_description.setText(self.rack.description)

        # Slots/Signals setups
        self.bt_cancel.clicked.connect(self.cancel)
        self.bt_save.clicked.connect(self.apply)

        self

    def field_edit(self) :
        self.changes_not_applyed = True




    def cancel(self) :
        self.changes_not_applyed = False

        self.i_rack_id.setValue(self.rack.id_rack)
        self.i_label_1.setText(self.rack.label_1)
        self.i_label_2.setText(self.rack.label_2)
        self.i_height.setValue(self.rack.height)
        self.i_description.setText(self.rack.description)

    def apply(self) :
        self.changes_not_applyed = False
        
        self.rack.label_1 = self.i_label_1.text()
        self.rack.label_2 = self.i_label_2.text()
        self.rack.height  = self.i_height.value()
        self.rack.description = self.i_description.text()
        



    
