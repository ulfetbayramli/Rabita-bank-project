from datetime import datetime
import requests

def convert(to , from_b , amount):
    url = f"https://api.apilayer.com/fixer/convert?to={to}&from={from_b}&amount={amount}"

    payload = {}
    headers= {
    "apikey": "ifngs2e7SCPc4Pb45K2fa5alERIZsLn5"
    }

    response = requests.get(url, headers=headers)

    json_response = response.json()
    result = json_response['info']['rate']
    date = datetime.today().strftime('%Y-%m-%d')
    return result , date


USD = convert('AZN', 'USD', 1)
GBP = convert('AZN', 'GBP', 1)
EUR = convert('AZN', 'EUR', 1)




# USD = [1.7, "02.06.2022"]
# GBP = [1.7, "02.06.2022"]
# EUR = [1.7, "02.06.2022"]
