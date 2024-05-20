import sqlite3
from typing import Any

from model.Device import Device
from model.Rack import Rack

SQL_DIRECTORY = '/'.join(__file__.split('/')[0:-1]) + '/sql/'
INITIALISATION_SCRIPT_PATH = SQL_DIRECTORY + 'init_db_file.sql'
EXAMPLES = {
    'Lord of the ring (basic)' : SQL_DIRECTORY + 'examples/lotr_basic.sql',
    'Harry Potter (complex)'   : SQL_DIRECTORY + 'examples/hp_complex'
}

class LocalFile :

    def __init__(self, path:str) -> None :
        self.path = path
        self.connection = sqlite3.connect(self.path)

    def __del__(self) :
        self.connection.close()
        
    def initialize_new_blank_project(self) -> None :
        cursor = self.connection.cursor()
        with open(INITIALISATION_SCRIPT_PATH, 'r') as script_file:
            script = script_file.read()
            cursor.executescript(script)
            self.connection.commit()

    def load_example_project(self, example_project_name) -> None :
        cursor = self.connection.cursor()
        with open(EXAMPLES[example_project_name], 'r') as script_file:
            script = script_file.read()
            cursor.executescript(script)
            self.connection.commit()

##########################################
#                 GETTER                 #
##########################################

    def _get_data_as_dict(self, request, data:dict=None) -> list[dict[str, Any]]:
        cursor = self.connection.cursor()
        if data is None :
            cursor.execute(request)
        else :
            cursor.execute(request, data)
        rows = cursor.fetchall()
        cols_names = [col[0] for col in cursor.description]
        result = [dict(zip(cols_names, row)) for row in rows]
        return result

    def get_metadata(self) :
        return self._get_data_as_dict('SELECT * FROM METADATA WHERE _ROWID_ = 1;')
    
    def get_rack_lazy(self, id_rack:int=None) :
        if id_rack is None :
            request = 'SELECT * FROM RACK;'
            result = self._get_data_as_dict(request)
        else :
            request = 'SELECT * FROM RACK WHERE id_rack = :id_rack;'
            result = self._get_data_as_dict(request, {'id_rack':id_rack})
        return [Rack(r) for r in result]
    
    def get_device_lazy(self, id_device:int=None) :
        if id_device is None :
            request = 'SELECT * FROM DEVICE;'
            result = self._get_data_as_dict(request)
        else :
            request = 'SELECT * FROM DEVICE WHERE id_device = :id_device;'
            result = self._get_data_as_dict(request, {'id_device':id_device})
        return [Device(r) for r in result]
    
##########################################
#                 SETTER                 #
##########################################



