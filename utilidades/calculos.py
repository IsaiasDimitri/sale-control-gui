def calc_valor_final(valor_und: float, qnt: int, desconto: float)->float:
    if valor_und <= 0 or qnt <= 0:
        return 0
    if desconto > 0:
        valor_und = (valor_und - (valor_und * desconto / 100))
    return round(valor_und * qnt, 2)
