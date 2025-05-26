from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import requests
from xml.etree import ElementTree
from datetime import datetime
import threading

Base = declarative_base()
engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
session = Session()

class Currency(Base):
    __tablename__ = 'currencies'
    id = Column(Integer, primary_key=True)
    code = Column(String(3))
    rate = Column(Float)
    last_updated = Column(String)

Base.metadata.create_all(engine)

class Singleton(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class CurrencyRates(metaclass=Singleton):
    URL = "https://www.cbr.ru/scripts/XML_daily.asp"
    CODES = ["USD", "EUR", "GBP"]

    def __init__(self):
        self._rates = {}
        self._fetch_rates()

    def _fetch_rates(self):
        try:
            Session = sessionmaker(bind=engine)
            with Session() as session:
                response = requests.get(self.URL)
                response.raise_for_status()
                tree = ElementTree.fromstring(response.content)
                today = datetime.now().strftime("%Y-%m-%d")

                new_rates = {}  # create a new dictionary for this fetch.
                for valute in tree.findall(".//Valute"):
                    char_code = valute.find("CharCode").text.strip()
                    if char_code in self.CODES:
                        value_element = valute.find("Value")
                        value = float(value_element.text.replace(",", "."))
                        new_rates[char_code] = value  # store in new rates.
                        print(f'Added currency {char_code} with value {value}')

                        existing_rate = session.query(Currency).filter_by(code=char_code).first()
                        if existing_rate:
                            existing_rate.rate = value
                            existing_rate.last_updated = today
                        else:
                            new_rate = Currency(code=char_code, rate=value, last_updated=today)
                            session.add(new_rate)
                session.commit()
                print(f'Database commited, added currencies')
                self._rates = new_rates

        except Exception as e:
            print(f"Ошибка при получении курсов валют: {e}")

    @property
    def rates(self):
        return self._rates.copy()