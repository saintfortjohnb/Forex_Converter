import unittest
from forex_python.converter import CurrencyCodes
from flask_testing import TestCase
from app import app, is_valid_currency

class TestCurrencyConverter(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_home_route(self):
        response = self.client.get("/")
        self.assert200(response)
        self.assert_template_used("index.html")

    def test_valid_currency(self):
        valid_code = "USD"
        invalid_code = "XYZ"

        self.assertTrue(is_valid_currency(valid_code))
        self.assertFalse(is_valid_currency(invalid_code))

    def test_same_currency_conversion(self):
        response = self.client.post("/", data={
            "from_currency": "USD",
            "to_currency": "USD",
            "amount": "1"
        })

        self.assert200(response)
        self.assertIn("Converted Amount:$ 1.00", response.data.decode())

if __name__ == "__main__":
    unittest.main()
