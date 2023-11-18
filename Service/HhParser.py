import requests
from Dto.VacancyDTO import VacancyDTO


class HeadHunterParser:
    url = 'https://api.hh.ru/vacancies'

    @staticmethod
    def get_vacancies(search_query: str, search_area: int) -> list[dict]:
        params = {
            "text": search_query,
            "area": search_area,
            "per_page": 100,
            "only_with_salary": True,
            "search_fields": "name"
        }

        # Отправляем запрос с установленными параметрами.
        response = requests.get(HeadHunterParser.url, params=params)

        # Успешный сценарий
        if response.status_code == 200:
            data_vacancy = response.json().get('items', [])
            return VacancyDTO.parse_vacancy_data(data_vacancy)  # Добавлен возврат результата
        else:
            # Обработка ошибок
            response.raise_for_status()
