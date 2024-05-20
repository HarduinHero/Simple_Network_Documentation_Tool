from typing import Any, Optional, Union

from model.Device import Device
from model.LocalFile import LocalFile
from model.Rack import Rack

class Project :

    def __init__(self, local_file_path:str) -> None:

        self.local_file_path = local_file_path
        self._local_file = LocalFile(local_file_path)

        self._changed_elements:set[Union[Device, Rack, dict]] = set()

        self.metadata : dict[str, Any] = self._local_file.get_metadata()[0]
        
        self.racks:list[Rack] = self._local_file.get_rack_lazy()
        self.devices:list[Device] = self._local_file.get_device_lazy()

        self.device_models = None #TODO
        self.device_types = None #TODO
        self.interface_types = None #TODO

    @staticmethod
    def new_project(local_file_path:str) :
        result = Project(local_file_path)
        result._local_file.initialize_new_blank_project()
        return result

    def has_changed(self) -> bool :
        return len(self._changed_elements) > 0
    
    def set_edited_element(self, element:Union[Device, Rack, dict]) :
        self._changed_elements.add(element)
    
    def save(self) :
        # TODO
        pass


    
