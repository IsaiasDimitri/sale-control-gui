from .base_model import BaseModel

class Venda(BaseModel):
    _VALID_KEYWORDS = [
        'cliente', 'data_criacao', 'relacao_produtos', 'valor_venda', 'status'
        ]
    def __init__(self, **kwargs):
        super().__init__(table= "vendas")
        for k, v in kwargs.items():
            if k in self._VALID_KEYWORDS:
                setattr(self, k, v)
            else:
                raise ValueError(
                    "Parametro desconhecido: {!r}".format(k))
