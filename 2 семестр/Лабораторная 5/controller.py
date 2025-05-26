from flask import Flask, render_template, request
from model import CurrencyRates

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    rates = {}
    if request.method == 'POST':
        selected_currencies = request.form.getlist('currency')
        if selected_currencies:
            rates_obj = CurrencyRates()
            rates = { k : v for k, v in rates_obj.rates.items() if k in selected_currencies }
    else:
        rates_obj = CurrencyRates()
        rates = rates_obj.rates

    return render_template('index.html', rates=rates, CODES = CurrencyRates.CODES)

if __name__ == '__main__':
    app.run(debug=True)