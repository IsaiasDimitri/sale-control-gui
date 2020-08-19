import pymongo
from .interfaces.database_interface import IDatabase

class DBMongo(metaclass=IDatabase):
    def __init__(self):
        ''' Implementacao de uma interface para consumir
            um banco Mongo. '''
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = myclient["alpha"]

    def insert(self, tabela: str, data: list)->list:
        ''' Insere todas as colecoes contidas no parametro data.
            Retorna uma lista com os ObjectIds das colecoes 
            inseridas. '''
        result = self.mydb[tabela].insert_many(data)
        return result.inserted_ids

    def select_all(self, table: str) -> tuple:
        ''' Seleciona todas as colecoes.
            Retorna uma tupla com as colecoes encontradas. '''
        f = self.mydb[table].find()
        return tuple(x for x in f)

    def select(self, table: str, query: dict) -> tuple:
        ''' Seleciona colecoes que atendem ao paramtro query.
            Retorna uma tupla com as colecoes encontradas. '''

        result = self.mydb[table].find(query)
        return tuple(doc for doc in result)

    def update(self, table: str, query: dict, new_values: dict) -> bool:
        ''' Atualiza colecoes que atendem ao paramtro query.
            Retorna True se açguma colecao for atualizada, 
            e False caso contrario. '''

        count = self.mydb[table].update_many(query, new_values)
        if 0 in (count.modified_count, count.matched_count):
            return False
        return True

    def delete(self, table: str, query: dict) -> int:
        ''' Deleta colecoes que atendem ao paramatro query.
            Retorna o numero de colecoes deletados. '''

        result = self.mydb[table].delete_many(query)
        return result.deleted_count

    def truncate_all(self):
        collections = self.mydb.collection_names(include_system_collections=False)
        map(self.mydb.drop_collection, collections)
    