from typing import Optional, Any
from model.Rack import Rack

class Device :

    def __init__(self, data:dict) :
        self.id_device : str = data.get('id_device', None)

        self.label_1 : str = data['label_1']
        self.label_2 : str = data['label_2']
        self.description : str = data['description']
        self.height : int = data['height']

        self.rack_location : Optional[Rack] = None
        self.rack_position : Optional[int] = data['rack_position']

        self.interface_list : list[int] = []

        self.edited:bool = False


    def __str__(self) -> str:
        return f'Device({self.id_device}, {self.label_1})'
    
    def __repr__(self) -> str:
        return self.__str__()