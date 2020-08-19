from .base_model import BaseModel

class Produto(BaseModel):
    _VALID_KEYWORDS = ['nome', 'valor', 'caracteristicas', 'empresa']
    def __init__(self, **kwargs):
        super().__init__(table= "produtos")
        for k, v in kwargs.items():
            if k in self._VALID_KEYWORDS:
                setattr(self, k, v)
            else:
                raise ValueError(
                    "Parametro desconhecido: {!r}".format(k))