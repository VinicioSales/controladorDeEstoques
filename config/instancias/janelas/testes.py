from datetime import datetime, timedelta

def compare_dates(date_string):
    today = datetime.now().date()
    input_date = datetime.strptime(date_string, '%d/%m/%Y').date()
    thirty_days_later = today + timedelta(days=30)
    
    if input_date < today:
        return "Data é menor que hoje"
    elif input_date > thirty_days_later:
        return "Data é maior que 30 dias a partir de hoje"
    else:
        return "Data está dentro de 30 dias a partir de hoje"

date_string = "17/03/2023"
print(compare_dates(date_string))
