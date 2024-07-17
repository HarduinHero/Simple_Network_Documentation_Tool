from bs4 import BeautifulSoup
from typing import Optional
from Context import Context

class Project :

#########################################
#               ATTRIBUTS               #
#########################################

    metadata: dict[str,str]     = {}
    filename: Optional[str]     = None
    data_objects_classes: dict  = {}
    data_objects: dict          = {}

#########################################
#              CONSTRUCTOR              #
#########################################

    @staticmethod
    def new_project(filename:str, title:str) -> 'Project' :
        project = Project()
        project.metadata ={
            Context.SNDTVER : Context().data[Context.SNDTVER],
            Context.LANG    : Context().data[Context.LANG],
            'title'         : title,
        }
        project.filename = filename
        return project
    
    @staticmethod
    def open_project(filename:str) -> 'Project' :
        return Project()
    
#########################################
#                METHODES               #
#########################################

    def save(self) -> None :
        pass

    def save_as(self, filename:str) -> None :
        pass