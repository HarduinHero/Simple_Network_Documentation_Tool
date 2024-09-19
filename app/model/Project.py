from bs4 import BeautifulSoup
from typing import Any, Optional
from Config import Config
from pathlib import Path
from model.enums import Views
from model.Item_class import Item_class

class Project :

#########################################
#               ATTRIBUTS               #
#########################################
    _is_saved: bool     = False
    sndt_version: str
    lang: str
    title: str
    file_path: Path
    description: str

    id_counter: int

    item_classes: dict[int, Item_class]
    items: list  = []

#########################################
#              CONSTRUCTOR              #
#########################################

    def __init__(self, file_path:Path, title:str, description:str) -> None:
        self.file_path      = file_path
        self.title          = title
        self.description    = description
        self.lang           = Config().data[Config.LANG]
        self.sndt_version   = Config().data[Config.SNDTVER]
        self.id_counter     = 0

        self.save()

    @staticmethod
    def load_from_file(file_path:Path) -> 'Project' :
        return Project(file_path, 'loading not implemented yet', 'TODO')

    
#########################################
#                METHODES               #
#########################################

    def save(self) -> None :
        #TODO
        self._is_saved = True

    def __setattr__(self, name: str, value: Any) -> None:
        self.__dict__['_is_saved'] = False
        self.__dict__[name] = value

    def __str__(self) -> str:
        return f'{self.title} {self.file_path} \n {self.description}'
    
#########################################
#                  EDIT                 #
#########################################

    

    def add_class(self, new_item_class:Item_class) :
        pass

    def set_item_class(self, index:int, new_item_class:Item_class) :
        pass

    def get_classes(self) -> list[Item_class] :
        return []

    def get_views(self) :
        return [Views.View5.value, Views.View6.value]








#########################################
#            OBSERVER PATTERN           #
#########################################

    observers = []

    def attach(self, new_observer: object) -> None:
        assert callable(getattr(new_observer, 'project_update_handler', None))
        
        for o in self.observers :
            if new_observer is o :
                break
        else :
            self.observers.append(new_observer)
    
    def detach(self, observer: object) -> None:
        for o in self.observers :
            if observer is o :
                break
        else :
            return None
        self.observers.remove(observer)

    def notify(self) -> None:
        for o in self.observers:
            o.project_update_handler()