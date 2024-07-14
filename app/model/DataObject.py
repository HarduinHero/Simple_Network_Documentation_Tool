from DataObjectModel import AbstractDataObjectModel

class DataObject :
    def __init__(self, model:AbstractDataObjectModel, id:int, name_1:str, name_2:str, description:str) -> None:
        self.model  = model
        self.id     = id
        self.name_1 = name_1
        self.name_2 = name_2
        self.description = description

    