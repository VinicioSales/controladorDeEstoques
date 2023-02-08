import datetime

def verificar_data_func(date_string):
    try:
        datetime.datetime.strptime(date_string, '%d-%m-%Y')
        return True
    except ValueError:
        return False

# exemplo de uso:
print(is_valid_date("01-01-2023")) # True
print(is_valid_date("2022-13-01")) # False
