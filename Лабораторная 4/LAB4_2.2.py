from bs4 import BeautifulSoup
import requests


# ---- Web version ----
# url = 'https://yandex.ru/pogoda/2?utm_source=serp&utm_campaign=helper&utm_medium=desktop&utm_content=helper_desktop_main&utm_term=title'
# response = requests.get(url)
# print(response.text)
# print(response.status_code)
# bs4 = BeautifulSoup(response.text,"lxml")
# ------------------------

# ---- Local version ----
with open('index.html', 'rb') as file:
    data = file.read().decode()
bs4 = BeautifulSoup(data,"lxml")
# ------------------------

all_days = bs4.find_all('a', 'link link_theme_normal text forecast-briefly__day-link i-bem')

weather_forecast = {}

for day in all_days:
    date = day.find('time', 'time forecast-briefly__date').get_text()

    weather_forecast[date] = {
        'value': day.find('span', 'temp__value temp__value_with-unit').get_text(),
        'desc': day['aria-label']
    }

print('Прогноз погоды доступен для:')

# Программа выводит список погоды на месяц
for date in weather_forecast:
    print(date, ':', weather_forecast[date]['value'], f'({weather_forecast[date]["desc"]})')

# Выводит отдельно выбор пользователя
# date_chosen = input('Выберите дату: ')
# print(f'Прогноз на {date_chosen}: {weather_forecast[date_chosen]}')
