
import sqlite3

class CurrencyRatesCRUD:
    def __init__(self, currency_rates_obj):
        self.__con = sqlite3.connect('data.sqlite3')
        self.__cursor = self.__con.cursor()
        self.__currency_rates_obj = currency_rates_obj
        self.__create_table()

    def __create_table(self):
        try:
            self.__cursor.execute(
                "CREATE TABLE IF NOT EXISTS currency("
                "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "cur TEXT,"
                "date TEXT,"
                "value FLOAT);"
            )
            self.__con.commit()
            print("Таблица 'currency' создана или уже существует.")
        except sqlite3.Error as e:
            print(f"Ошибка при создании таблицы: {e}")

    def create(self, data):
        try:
            sqlquery = "INSERT INTO currency(cur, date, value) VALUES(?, ?, ?)"
            self.__cursor.executemany(sqlquery, data)
            self.__con.commit()
            print(f"{len(data)} валютных курсов было вставлено.")
        except sqlite3.Error as e:
            print(f"Ошибка вставки: {e}")
            self.__con.rollback()

    def read(self, currency_code=None):
        try:
            if currency_code:
                sqlquery = "SELECT * FROM currency WHERE cur = ?"
                self.__cursor.execute(sqlquery, (currency_code,))
            else:
                sqlquery = "SELECT * FROM currency"
                self.__cursor.execute(sqlquery)
            rows = self.__cursor.fetchall()
            for row in rows:
                print(row)
            return rows
        except sqlite3.Error as e:
            print(f"Ошибка чтения: {e}")
            return None

    def update(self, currency_code, new_value):
        try:
            sqlquery = "UPDATE currency SET value = ? WHERE cur = ?"
            self.__cursor.execute(sqlquery, (new_value, currency_code))
            self.__con.commit()
            print(f"Курс валюты {currency_code} обновлен до {new_value}.")
        except sqlite3.Error as e:
            print(f"Ошибка обновления: {e}")
            self.__con.rollback()

    def delete(self, currency_code):
        try:
            sqlquery = "DELETE FROM currency WHERE cur = ?"
            self.__cursor.execute(sqlquery, (currency_code,))
            self.__con.commit()
            print(f"Курс валюты {currency_code} удалён.")
        except sqlite3.Error as e:
            print(f"Ошибка удаления: {e}")
            self.__con.rollback()

    def close(self):
        if self.__con:
            self.__con.close()
            print("Подключение к базе данных закрыто.")

    def __del__(self):
        self.close()