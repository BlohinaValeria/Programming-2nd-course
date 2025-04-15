from model import CurrencyRates
from controllers.init import CurrencyRatesCRUD

if __name__ == "__main__":
    currency_rates = CurrencyRates(["USD", "EUR", "GBP"])
    crud_manager = CurrencyRatesCRUD(currency_rates)

    print("\n Курсы валют через базу данных:")

    data_to_insert = [
        ('USD', '2025-04-02', 84),
        ('EUR', '2023-04-02', 83),
        ('GBR', '2023-04-02', 78)
        ]
    crud_manager.create(data_to_insert)
    crud_manager.read()

    print("\nАктуальные курсы валют:")
    for code, details in currency_rates.rates.items():
        print(f"{code}: {details['value']} ({details['date']})")

    crud_manager.close()