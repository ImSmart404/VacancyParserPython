import requests

class HhParser:
    @staticmethod
    def get_data(vacancy_title):
        url = "https://api.hh.ru/vacancies"
        params = {
            'text': vacancy_title,
            'area': 1,  # Код региона (1 - Москва)
            'per_page': 5  # Количество вакансий на одной странице
        }

        headers = {
            'User-Agent': 'VacancyParserPython (withfuckinglove@mail.ru)'
        }

        response = requests.get(url, params=params, headers=headers)

        if response.status_code == 200:
            data = response.json()
            vacancies = data.get('items', [])
            return vacancies
        else:
            return None
