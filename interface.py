import base
from Place import Place

def start():
    def showPlaceData(place):
        info = place.getInfo()
        print("Актуальная информация о заведении: ")
        data = f"Название: {info['name']}\n" \
               f"Описание: {info['description']}\n" \
               f"Город: {info['city']}\n" \
               f"Средняя оценка: {round(info['rate'], 2)}\n" \
               f"Количество оценок: {info['ratesCount']}\n" \
               f"Количество просмотров: {info['visits']}\n" \
               f"Количество отзывов: {info['commentsCount']}\n"
        print(data)


    name = input("Введите название заведения (из карточки в приложении): ")
    places = base.searchPlace(name)

    if len(places) > 0:
        if len(places) >= 10:
            print(f"Количество найденных заведений: {len(places)}")
            cities = sorted(set(x.city for x in places if x.city))
            if (len(cities) > 100):
                print("Заведений слишком много. Уточните название и попробуйте снова")
                exit(0)

            for i, city in enumerate(cities):
                print(f"{i + 1}) {city}")
            cityNameNum = int(input("Введите цифру в соответствии с городом заведения: "))
            print()
            places = base.searchPlaceByCity(places, cities[cityNameNum - 1])
    else:
        print("Заведений не надено")
        exit(0)

    for i, place in enumerate(places):
        if i + 1 > 9:
            print(f"{i + 1}) {place.name} - {place.description} ({place.city})")
        else:
            print(f"{i + 1})  {place.name} - {place.description} ({place.city})")

    placeNum = int(input("\nВведите цифру в соответствии с номером заведения: "))
    place = Place(places[placeNum - 1].id)
    showPlaceData(place)

    mark = int(input("Введите оценку для накрутки (от 1 до 5): "))
    num = int(input("Введите количество оценок: "))
    place.flood(mark, num)
    print("Накрутка завершена\n")
    showPlaceData(place)
