from flask import Flask, render_template, request, flash
from forex_python.converter import CurrencyRates, RatesNotAvailableError
from utils import is_valid_amount, get_currency_symbol, is_valid_currency

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        from_currency = request.form.get('from_currency').upper()
        to_currency = request.form.get('to_currency').upper()
        amount = request.form.get('amount')

        if not is_valid_amount(amount):
            flash('Invalid amount. Please input a valid number.', 'error')
            return render_template('index.html')

        if not is_valid_currency(from_currency) or not is_valid_currency(to_currency):
            flash('Invalid currency code. Please input a valid currency code.', 'error')
            return render_template('index.html')

        try:
            c = CurrencyRates()
            converted_amount = c.convert(from_currency, to_currency, float(amount))
            symbol = get_currency_symbol(to_currency)
            result = f"{symbol} {converted_amount:.2f}"
            return render_template('index.html', result=result)
        except RatesNotAvailableError:
            flash('Error occurred while fetching rates. Please try again later.', 'error')
            return render_template('index.html')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
