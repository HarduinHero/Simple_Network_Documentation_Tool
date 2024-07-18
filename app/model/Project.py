from bs4 import BeautifulSoup
from typing import Any, Optional
from Config import Config
from pathlib import Path

class Project :

#########################################
#               ATTRIBUTS               #
#########################################
    _is_initialized: bool        = False
    _is_saved: bool              = False

    sndt_version: Optional[str] = None
    lang: Optional[str]         = None

    title: Optional[str]        = None
    file_path: Optional[Path]   = None
    description: Optional[str]  = None

    data_objects_classes: dict  = {}
    data_objects: dict          = {}

#########################################
#              CONSTRUCTOR              #
#########################################

    def init_new(self, file_path:Path, title:str, description:str) -> None :
        self.file_path      = file_path
        self.title          = title
        self.description    = description
        self.lang           = Config().data[Config.LANG]
        self.sndt_version   = Config().data[Config.SNDTVER]
        self._is_initialized = True
        self.save()

    
    def init_open(self, file_path:Path) -> None :
        self.file_path      = file_path
        self._is_initialized = True

    
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
    
