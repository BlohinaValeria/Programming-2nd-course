countries_with_cities = {
    "Россия": ["Москва", "Санкт-Петербург", "Рязань"],
    "Испания": ["Барселона", "Мадрид"],
    "Португалия": ["Порту", "Лиссабон", "Эвора"],
    "Германия": ["Берлин", "Бремен", "Мюнхен"]
}


def find_country(city, countries_with_cities):
    for country, cities in countries_with_cities.items():
        if city in cities:
            return country
    return "Город не найден"


def list_available_cities(countries_with_cities):
    cities = []
    for city_list in countries_with_cities.values():
        cities.extend(city_list)
    return cities


while True:
    # Вывод доступных городов
    available_cities = list_available_cities(countries_with_cities)
    print("Доступные города:", ", ".join(available_cities))

    city = input("Введите название города: ")
    country = find_country(city, countries_with_cities)
    print(f"Город {city} находится в стране {country}")

if __name__ == "__main__":
    main()
