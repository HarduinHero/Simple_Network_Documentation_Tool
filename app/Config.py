class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Config(metaclass=SingletonMeta):
    
    SNDTVER = 'sndt_version'
    WD      = 'working_directory'
    LANG    = 'lang'

    data:dict = {
        SNDTVER : None,
        WD      : None,
    }
