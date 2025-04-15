# #3 компонента через контроллер
# # перенос модуля currenсуrates в каталог model.py
# # реализация всей программы в main(money) через run
#
# from money import CurrencyRates
#
# from controllers import databasescontroller
# from controllers import viewcontroller
#
# c_r = CurrencyRates(['USD','EUR'])
# c_r_controller = databasescontroller.CurrencyRatesCRUD()
# c_r.values = [('2025-04-02 11:10', 'USD', '84.8707'), ('2025-04-02 11:11', 'EUR', '84.8707')]
#
# c_r_controller._create()
# import sqlite3
# c = sqlite3.connect((':memory:'))
# c = c.execute(('SELECT * FROM currencies'))
# for _row in cur:
#     print(_row)
#
# input("Проверка добавилось ли")
#
# from controllers.init import CurrencyRatesCRUD
#
# if __name__ == "__main__":
#     controller = CurrencyRatesCRUD()
#     controller.get_and_display_rates(["USD", "EUR", "GBP"])