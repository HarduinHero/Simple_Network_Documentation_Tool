from PyQt6.QtWidgets import QFrame
from ui.deviceedit import Ui_device_edit
from model.Device import Device
from typing import Optional

class DeviceEdit(QFrame, Ui_device_edit) :
    def __init__(self, device:Optional[Device]=None, *args, **kwargs) :
        super(DeviceEdit, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.device:Optional[Device] = device

        if self.device is not None :
            self.i_device_id.setValue(self.device.id_device)
            self.i_label_1.setText(self.device.label_1)
            self.i_label_2.setText(self.device.label_2)
            self.i_description.setText(self.device.description)