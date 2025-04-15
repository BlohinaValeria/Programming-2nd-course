import requests
from xml.etree import ElementTree
from datetime import datetime
import threading

class Singleton(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class CurrencyRates(metaclass=Singleton):
    URL = "https://www.cbr.ru/scripts/XML_daily.asp"
    CODES = {
        "USD": "R01235",
        "EUR": "R01239",
        "GBP": "R01035"
    }

    def __init__(self, char_codes=["USD"]):
        self._char_codes = char_codes
        self._rates = {}
        self._last_update = None
        self._fetch_rates()

    def _fetch_rates(self):
        try:
            response = requests.get(self.URL)
            response.raise_for_status()
            tree = ElementTree.fromstring(response.content)
            today = datetime.now().strftime("%Y-%m-%d")

            for valute in tree.findall("./Valute"):
                char_code = valute.find("CharCode").text.strip()
                if char_code in self._char_codes:
                    value_element = valute.find("Value")
                    value = float(value_element.text.replace(",", ".") if value_element is not None else None)
                    self._rates[char_code] = {"date": today, "value": value}
            self._last_update = datetime.now()
        except Exception as e:
            print(f"Ошибка при получении курсов валют: {e}")

    @property
    def rates(self):
        return self._rates.copy()

    @property
    def char_codes(self):
        return self._char_codes

    @char_codes.setter
    def char_codes(self, new_codes):
        if isinstance(new_codes, list) and all(code in self.CODES for code in new_codes):
            self._char_codes = new_codes
            self._fetch_rates()
        else:
            raise ValueError("Некорректные коды валют переданы")

    @char_codes.deleter
    def char_codes(self):
        self._char_codes = []
        self._rates = {}