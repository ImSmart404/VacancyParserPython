import requests
from typing import List

from Dto.VacancyDTO import VacancyDTO


class Parser:
    url_hh = 'https://api.hh.ru/vacancies'
    url_sj = 'https://api.superjob.ru/2.0/vacancies/'

    def get_vacancies_from_hh(search_query: str, search_area: int) -> List[dict]:
        params = {
            "text": search_query,
            "area": search_area,
            "per_page": 100,
            "only_with_salary": True,
            "search_fields": "name"
        }

        # Отправляем запрос с установленными параметрами.
        response = requests.get(Parser.url_hh, params=params)

        # Успешный сценарий
        if response.status_code == 200:
            data_vacancy = response.json().get('items', [])
            return VacancyDTO.parse_vacancy_data_hh(data_vacancy)
        else:
            # Обработка ошибок
            response.raise_for_status()

    def get_vacancies_from_sj(search_query: str, search_area: int) -> List[dict]:

        params = {
            "keyword": search_query,
            "page": 0,
            "count": 10,
            "town": search_area
        }
        headers = {
            'X-Api-App-Id': "v3.r.137972890.e5a3326073e58868f15fad4c58ea7f01e3d14b4b.b909ab9219ba150389509ee075a384a41331fddf"}

        # Отправляем запрос с установленными параметрами.
        response = requests.get(Parser.url_sj, headers=headers, params=params)
        print(response.json())

        # Успешный сценарий
        if response.status_code == 200:
            data_vacancy = response.json().get('objects', [])
            return VacancyDTO.parse_vacancy_data_sj(data_vacancy)  # Добавлен возврат результата
        else:
            # Обработка ошибок
            response.raise_for_status()
