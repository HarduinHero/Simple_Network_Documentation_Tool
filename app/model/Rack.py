from typing import Any, Optional

class Rack :

    def __init__(self, data:dict) :
        self.id_rack : str = data.get('id_rack', None)

        self.label_1 : str = data['label_1']
        self.label_2 : str = data['label_2']
        self.description : str = data['description']
        self.height : int = data['height']
        self.device_list : list[int] = []

        self.edited:bool = False

    def __str__(self) -> str:
        return f'Rack({self.id_rack}, {self.label_1})'
    
    def __repr__(self) -> str:
        return self.__str__()