import json


def get_city_id(city_type, city_name):
    with open('resources/region.json', 'r', encoding='utf-8') as file:
        areas_data = json.load(file)
    areas = areas_data.get(city_type)
    if areas is None:
        return 4                                                    ##Вернем регион 4 при неправильных параметрах

    return areas.get(city_name)
