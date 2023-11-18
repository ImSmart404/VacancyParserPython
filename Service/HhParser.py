import requests
from requests import Response
from requests.structures import CaseInsensitiveDict


class HeadHunterParser:
    url = 'https://api.hh.ru/vacancies'

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

        # Проверьте, является ли код состояния ответа 200 (OK), прежде чем пытаться разобрать JSON.
        if response.status_code == 200:
            data_vacancy = response.json().get('items', [])
            return HeadHunterParser.data_organize(data_vacancy)
        else:
            # Обработайте ошибку или вызовите исключение при необходимости.
            response.raise_for_status()

    @staticmethod
    def data_organize(data_vacancy) -> list[dict]:
        """
        Организация данных по вакансиям.
        Возвращает сформированный список словарей.
        """
        vacancies = []
        for vacancy in data_vacancy:
            title = vacancy['name']
            link = vacancy['alternate_url']
            requirement = vacancy['snippet'].get('requirement', None)
            salary_from = vacancy['salary'].get('from', None)
            salary_to = vacancy['salary'].get('to', None)

            # Устанавливаем значение зарплаты.
            # Если есть обе границы - устанавливаем минимальное значение.
            # В ином случае, устанавливаем то значение, которое существует.
            if salary_from and salary_to:
                salary = min(salary_from, salary_to)
            else:
                salary = salary_from or salary_to

            # Устанавливаем значение требований.
            # Если значение есть - приводим его к нижнему регистру.
            # В ином случае, устанавливаем значение, что данных нет.
            if requirement:
                requirement = requirement.lower()
            else:
                requirement = 'Нет данных.'

            # Добавляем сформированные данные в список.
            vacancies.append({
                'title': title,
                'link': link,
                'salary': salary,
                'requirement': requirement
            })

        return vacancies
