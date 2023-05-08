from forex_python.converter import CurrencyCodes, RatesNotAvailableError

def is_valid_currency(currency_code):
    currency_codes = CurrencyCodes()
    return currency_codes.get_symbol(currency_code) is not None

def is_valid_amount(amount):
    try:
        float(amount)
        return True
    except ValueError:
        return False

def get_currency_symbol(currency_code):
    try:
        c = CurrencyCodes()
        return c.get_symbol(currency_code)
    except RatesNotAvailableError:
        return None
