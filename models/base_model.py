from database.db_mongo import DBMongo as DB

class BaseModel:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        desc = ''
        for k, v in vars(self):
            desc += f'{k} = {v}\t'

    def save(self) -> None:
        value = vars(self).copy()
        value.pop('table')
        if not hasattr(self, '_id') and hasattr(self, 'table'):
            lista = [value]
            result = DB().insert(self.table, lista)
            self._id = result[0]
        elif hasattr(self, '_id') and hasattr(self, 'table'):
            self.update(value)

    def update(self, values: dict) -> bool:
        if hasattr(self, '_id'):
            new_values = {
                "$set": values
            }
            query = { 
                "_id": self._id
            }
            result = DB().update(self.table, query, new_values)
            return True if result > 0 else False
        return False
        
    def select_all(self):
        return DB().select_all(self.table)


