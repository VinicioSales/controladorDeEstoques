import datetime

def somar_dias_uteis(dias_a_somar):
    #NOTE - somar_dias_uteis
    """
    Esta função soma dias úteis a partir de uma data inicial.

    param:
    - int: dias_a_somar (número de dias úteis a serem somados)

    return:
    - datetime.date: data_atual (data somada com os dias úteis)
    """
    dias_uteis = 0
    data_atual = datetime.date.today()

    while dias_uteis < dias_a_somar:
        data_atual += datetime.timedelta(days=1)
        if data_atual.weekday() not in (5, 6):
            dias_uteis += 1

    data_vencimento = data_atual
    return data_vencimento

data_vencimento = somar_dias_uteis(20)
data_vencimento = data_vencimento.strftime("%d/%m/%Y")
print(data_vencimento)
