from .base_model import BaseModel

class Cliente(BaseModel):
    _VALID_KEYWORDS = [
        'nome', 'cpf/cnpj', 'email', 'telefone', 'telefone_alt', 
        'endereco', 'data_criacao']
    def __init__(self, **kwargs):
        super().__init__(table= "clientes")
        for k, v in kwargs.items():
            if k in self._VALID_KEYWORDS:
                setattr(self, k, v)
            else:
                raise ValueError(
                    "Parametro desconhecido: {!r}".format(k))


