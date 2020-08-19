from abc import ABCMeta

class IDatabase(ABCMeta):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    
    @classmethod
    def insert(self, table, data):
        raise NotImplementedError

    @classmethod
    def select_all(self, table):
        raise NotImplementedError

    @classmethod
    def select(self, table, query):
        raise NotImplementedError
    
    @classmethod
    def update(self, table, query, new_values):
        raise NotImplementedError
    
    @classmethod
    def delete(self, table, query):
        raise NotImplementedError

    @classmethod
    def truncate_all(self):
        raise NotImplementedError