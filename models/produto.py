from .base_model import BaseModel

class Produto(BaseModel):
    _VALID_KEYWORDS = ['codigo', 'nome', 'valor', 'caracteristicas', 'empresa']
    _COLUMNS_OF_TABLE = ['codigo', 'nome', 'valor', 'empresa']
    _TABLE = 'produtos'
    def __init__(self, **kwargs):
        super().__init__(table= _TABLE)
        for k, v in kwargs.items():
            if k in self._VALID_KEYWORDS:
                setattr(self, k, v)
            else:
                raise ValueError(
                    "Parametro desconhecido: {!r}".format(k))