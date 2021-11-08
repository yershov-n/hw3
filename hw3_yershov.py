# Создать view-функцию, которая выводит курс биткоина для заданной валюты. Название валюты передаётся через строковый
# параметр currency. Параметр должен быть задан как необязательный. Если его нет в запросе, view-функция должна
# использовать валюту по умолчанию USD.
#
# Данные о курсе можно получить по адресу https://bitpay.com/api/rates. Для выполнения запроса, по указанному адресу,
# вам понадобится библиотека requests. В этой библиотеке есть функция get которая поможет отправить запрос и получить
# ответ:
#
# response = requests.get('https://bitpay.com/api/rates')
# Данные из ответа выбирать надо используя метод json.
#
# data = response.json()
# Разместить view-функцию в модуле app, а бизнес-логику в модуле utils.

from flask import Flask
from webargs.flaskparser import use_kwargs
from webargs import fields, validate
from utils import get_rate

app = Flask(__name__)


@app.route('/')
@use_kwargs(
    {
        'currency': fields.Str(
            required=False,
            missing='USD',
            validate=[validate.Length(equal=3)]
        )
    },
    location='query'
)
def get_currency(currency):
    currency = currency.upper()
    return f'<p>1 BTC = {get_rate(currency)} {currency}</p>'


app.run(debug=True)
