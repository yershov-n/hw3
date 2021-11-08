def get_rate(currency):
    import requests

    response = requests.get('https://bitpay.com/api/rates')
    data = response.json()
    dct = {}

    for _ in data:
        dct.update({_['code']: _['rate']})

    return dct[currency]
