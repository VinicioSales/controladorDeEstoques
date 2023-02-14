import datetime
dias_uteis = 0
data_atual = datetime.date.today()

while dias_uteis < 2:
    data_atual += datetime.timedelta(days=1)
    if data_atual.weekday() not in (5, 6):
        dias_uteis += 1
data_vencimento = str(data_atual)
date = datetime.datetime.strptime(data_vencimento, "%Y-%m-%d")
br_date = date.strftime("%d/%m/%Y")
print(br_date)