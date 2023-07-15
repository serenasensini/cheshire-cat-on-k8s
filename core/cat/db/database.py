from tinydb import TinyDB

#TODO can we add a verbose level for logging?

class Database:

    _instance = None
    file_name = "metadata.json"

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            from cat.log import log
            log(f"Connecting to {cls.file_name}", "ERROR")
            cls._instance.db = TinyDB(cls.file_name)
        return cls._instance.db