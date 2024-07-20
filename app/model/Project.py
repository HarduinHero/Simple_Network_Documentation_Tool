from bs4 import BeautifulSoup
from typing import Any, Optional
from Config import Config
from pathlib import Path

class Project :

#########################################
#               ATTRIBUTS               #
#########################################
    _is_saved: bool              = False
    sndt_version: str
    lang: str
    title: str
    file_path: Path
    description: str
    data_objects_classes: dict
    data_objects: dict

#########################################
#              CONSTRUCTOR              #
#########################################

    def __init__(self, file_path:Path, title:str, description:str) -> None:
        self.file_path      = file_path
        self.title          = title
        self.description    = description
        self.lang           = Config().data[Config.LANG]
        self.sndt_version   = Config().data[Config.SNDTVER]
        self._is_initialized = True
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
    
